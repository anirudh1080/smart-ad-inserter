import subprocess

def render_video(video_url, ad_url, qr_url, output_path):
    # Construct the bash command
    cmd = f"bash scripts/remotion_render.sh '{video_url}' '{ad_url}' '{qr_url}' '{output_path}'"
    
    try:
        # Run the command
        subprocess.run(cmd, shell=True, check=True)
        print(f"Video rendered successfully at {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
