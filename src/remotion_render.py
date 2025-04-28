import subprocess

def render_video_with_ad(video_url, ad_url, qr_url):
    # Pass params to remotion
    cmd = [
        "npx", "remotion", "render",
        "OverlayVideo",
        "--props", f'{{"videoSrc": "{video_url}", "adGifSrc": "{ad_url}", "qrCodeSrc": "{qr_url}"}}',
        "--output", f"outputs/{video_url.split('/')[-1].replace('.mp4', '_final.mp4')}"
    ]
    subprocess.run(cmd, check=True)
