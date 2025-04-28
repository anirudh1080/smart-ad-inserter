#!/bin/bash

# Input Arguments: video_url, ad_url, qr_url
VIDEO_URL=$1
AD_URL=$2
QR_URL=$3
OUTPUT_PATH=$4

# Command to render the video using Remotion
npx remotion render OverlayVideo --props "{\"videoSrc\": \"$VIDEO_URL\", \"adGifSrc\": \"$AD_URL\", \"qrCodeSrc\": \"$QR_URL\"}" --output "$OUTPUT_PATH"
