# worker.py

from multiprocessing import Process
import time
import openai

openai.api_key = "your-openai-api-key"  # Load it securely using env variable ideally

def generate_video_description(video_url):
    """Generates description for the given video using OpenAI."""
    prompt = f"Generate a concise and catchy description for the video at {video_url}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()

def generate_advertisement_description(advertisement_url):
    """Generates description for the advertisement GIF."""
    prompt = f"Write a one-line description for the advertisement GIF at {advertisement_url}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=60
    )
    return response['choices'][0]['message']['content'].strip()

def worker_function(video_data):
    """Background worker to process videos."""
    for entry in video_data:
        video_desc = generate_video_description(entry['video_url'])
        ad_desc = generate_advertisement_description(entry['advertisement'])
        print(f"[Worker] Video: {video_desc} | Ad: {ad_desc}")
        time.sleep(1)  # simulate processing time

def start_worker(video_data):
    """Starts a worker process."""
    p = Process(target=worker_function, args=(video_data,))
    p.start()
    return p
