import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_video_description(video_url):
    # Dummy version — in production, you can extract frames + describe
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Describe this video briefly: {video_url}"}]
    )
    return response['choices'][0]['message']['content']

def generate_ad_description(ad_url):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Describe this advertisement gif: {ad_url}"}]
    )
    return response['choices'][0]['message']['content']

def map_video_to_ad(video_description, ad_description):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Does this ad match this video?\nVideo: {video_description}\nAd: {ad_description}\nRespond Yes or No."}]
    )
    return response['choices'][0]['message']['content'].strip().lower() == "yes"
