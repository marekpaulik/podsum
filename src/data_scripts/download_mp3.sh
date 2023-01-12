#!/bin/bash

filepath='../../data/V redakcii Dennika N/video_ids.txt'

while read id; do
  echo "Downlaoding $id"
  yt-dlp -x --audio-format mp3 -o "$id.mp3" $id
done < "$filepath"