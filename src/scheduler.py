import asyncio
import glob
import os

async def play_scheduled_videos():
    output_files = sorted(glob.glob("outputs/*.mp4"))
    
    for video in output_files:
        print(f"Now playing: {video}")
        # Use system video player (example: VLC)
        os.system(f"vlc --play-and-exit {video}")
        await asyncio.sleep(2)  # wait before next
