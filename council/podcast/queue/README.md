# Publish queues

One file per episode, `<episode>.json`, in the shape of `schema/publish-queue.schema.json`. The timer
(`.github/workflows/publish-queue.yml`) publishes from here; how it works is in `council/podcast/publish/README.md`.

Covers and day-0 images live beside the queues in `covers/<episode>/`, as JPEGs, so each has a public
raw.githubusercontent.com URL once it is on main. Clips are assets of the GitHub release `pod-<episode>`.
