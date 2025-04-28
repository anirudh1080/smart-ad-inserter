import json
import asyncio
from src.video_mapper import generate_video_description, generate_ad_description, map_video_to_ad
from src.remotion_render import render_video
from src.scheduler import play_scheduled_videos
from redis import Redis
from rq import Queue
import os
from dotenv import load_dotenv

load_dotenv()

# Setup Redis queue
redis_conn = Redis()
q = Queue(connection=redis_conn)

def load_inputs(path="assets/inputs.json"):
    with open(path, "r") as f:
        return json.load(f)

async def main():
    inputs = load_inputs()
    tasks = []

    for item in inputs:
        video_url = item["video_url"]
        ad_url = item["advertisement"]
        qr_url = item["qr_cdn"]

        # Background task: prepare description and mapping
        job = q.enqueue(process_single_video, video_url, ad_url, qr_url)
        tasks.append(job)

    # Play videos one after the other
    await play_scheduled_videos()

def process_single_video(video_url, ad_url, qr_url):
    # Generate descriptions
    video_desc = generate_video_description(video_url)
    ad_desc = generate_ad_description(ad_url)

    # Match video to ad
    mapping = map_video_to_ad(video_desc, ad_desc)

    if mapping:
        # Render using remotion
        render_video(video_url, ad_url, qr_url, "../static/")

if __name__ == "__main__":
    asyncio.run(main())
