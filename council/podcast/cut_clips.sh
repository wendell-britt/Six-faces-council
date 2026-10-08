#!/usr/bin/env bash
# Cuts a podcast episode's clips from its Zoom video. Step 6 of the podcast episode move
# (council/moves/podcast-episode.md), board row pod-ep1-clip-cut.
#
#   bash council/podcast/cut_clips.sh <video.mp4> <clips.tsv> --logo <logo.png|jpg> [--only 02,03] [--out <dir>]
#
# clips.tsv has one clip per line: id, start, end (tab separated; a header line naming id, start and end may come
# first and may add other columns, which are ignored; lines starting with # are skipped). Times are seconds or
# h:mm:ss(.ms).
#
# Each clip is vertical 1080x1920: the full frame over a blurred copy of itself, the show's logo at the top (Wendell,
# 2026-10-08, on pod-ep1-clip-cut: "Let's add the podcast logo to the top like the Mastering Allyship ones do"), no
# words burned in (pod-clip-no-words), half a second of padding each end. Zoom's "Recording Started" chapter is
# dropped and the audio chain ends with asetpts=N/SR/TB, or players report the wrong length. Each clip's video and
# audio length is checked after the cut, and a clip outside 30 to 90 seconds is flagged (pod-clip-length).
#
# The logo sits where the Mastering Allyship clips have it (podcast/_claude_work/ep02/render.py on his Mac): 440
# pixels tall, centred in the band above the video at y=328. LOGO_H and LOGO_Y move it; --no-logo cuts without one.
# Loudness is normalised to -14 LUFS, as those clips are.
set -euo pipefail

W=1080 H=1920
PAD=${PAD:-0.5}
PRESET=${PRESET:-medium}  # x264 speed; "fast" for a long clip on a slow machine
LOGO_H=${LOGO_H:-440}
LOGO_Y=${LOGO_Y:-328}

usage() { sed -n '4,5p' "$0" | sed 's/^# *//' >&2; exit 2; }

video=${1:-}; tsv=${2:-}
[[ -n $video && -n $tsv ]] || usage
shift 2
logo='' only='' out='' nologo=0
while (($#)); do
  case $1 in
    --logo) logo=$2; shift 2 ;;
    --no-logo) nologo=1; shift ;;
    --only) only=$2; shift 2 ;;
    --out) out=$2; shift 2 ;;
    *) usage ;;
  esac
done
[[ -f $video ]] || { echo "No video at $video" >&2; exit 1; }
[[ -f $tsv ]] || { echo "No clip list at $tsv" >&2; exit 1; }
if ((nologo == 0)); then
  [[ -n $logo ]] || { echo "Name the show's logo with --logo, or cut without one with --no-logo" >&2; exit 1; }
  [[ -f $logo ]] || { echo "No logo at $logo" >&2; exit 1; }
fi
out=${out:-$(dirname "$tsv")/cut}
mkdir -p "$out"

secs() {  # h:mm:ss(.ms), m:ss or seconds -> seconds
  awk -v t="$1" 'BEGIN { n = split(t, p, ":"); s = 0; for (i = 1; i <= n; i++) s = s * 60 + p[i]; printf "%.3f", s }'
}

# Column positions, from a header if there is one.
ci=1 cs=2 ce=3
header=$(grep -v '^#' "$tsv" | head -1)
if [[ $header =~ (^|$'\t')start($'\t'|$) ]]; then
  IFS=$'\t' read -ra cols <<<"$header"
  for i in "${!cols[@]}"; do
    case ${cols[$i],,} in id) ci=$((i + 1)) ;; start) cs=$((i + 1)) ;; end) ce=$((i + 1)) ;; esac
  done
  skip=1
else
  skip=0
fi

vf="[0:v]split[a][b];[a]scale=$W:$H:force_original_aspect_ratio=increase,crop=$W:$H,gblur=sigma=40,eq=brightness=-0.08[bg];[b]scale=$W:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2"
if ((nologo == 0)); then
  vf+="[base];[1:v]scale=-1:$LOGO_H,format=rgba[logo];[base][logo]overlay=(W-w)/2:$LOGO_Y-h/2:eof_action=repeat"
fi
vf+=",format=yuv420p[v];[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asetpts=N/SR/TB[aout]"

made=0 flagged=0
while IFS=$'\t' read -ra f; do
  id=${f[$((ci - 1))]:-}; start=${f[$((cs - 1))]:-}; end=${f[$((ce - 1))]:-}
  [[ -z $id || $id == \#* ]] && continue
  if [[ -n $only && ",$only," != *",$id,"* ]]; then continue; fi
  s=$(secs "$start"); e=$(secs "$end")
  from=$(awk -v s="$s" -v p="$PAD" 'BEGIN { x = s - p; if (x < 0) x = 0; printf "%.3f", x }')
  dur=$(awk -v s="$s" -v e="$e" -v f="$from" -v p="$PAD" 'BEGIN { printf "%.3f", e + p - f }')
  dest="$out/clip-$id.mp4"
  inputs=(-ss "$from" -t "$dur" -i "$video")
  ((nologo == 0)) && inputs+=(-i "$logo")
  ffmpeg -nostdin -hide_banner -loglevel error -y "${inputs[@]}" \
    -filter_complex "$vf" -map '[v]' -map '[aout]' -map_chapters -1 -map_metadata -1 \
    -c:v libx264 -preset "$PRESET" -crf 20 -r 30 -c:a aac -b:a 160k -ar 48000 -movflags +faststart "$dest"

  vlen=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of csv=p=0 "$dest")
  alen=$(ffprobe -v error -select_streams a:0 -show_entries stream=duration -of csv=p=0 "$dest")
  flen=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$dest")
  size=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$dest")
  chap=$(ffprobe -v error -show_chapters -of csv=p=0 "$dest" | wc -l)
  note=$(awk -v d="$dur" -v v="$vlen" -v a="$alen" -v f="$flen" 'BEGIN {
    m = ""
    if (v - d > 0.3 || d - v > 0.3 || a - d > 0.3 || d - a > 0.3 || f - d > 0.3 || d - f > 0.3) m = m " length off (asked " d "s)"
    if (f < 30) m = m " under 30s"
    if (f > 90) m = m " over 90s"
    print m }')
  [[ $size == "${W}x${H}" ]] || note+=" size $size"
  ((chap == 0)) || note+=" $chap chapters left"
  printf 'clip-%s.mp4  %ss (video %s, audio %s)  %s%s\n' "$id" "$flen" "$vlen" "$alen" "$size" "${note:+  CHECK:$note}"
  made=$((made + 1)); [[ -n $note ]] && flagged=$((flagged + 1))
done < <(grep -v '^#' "$tsv" | tail -n +$((skip + 1)))

echo "$made clips in $out, $flagged to check"
((made > 0))
