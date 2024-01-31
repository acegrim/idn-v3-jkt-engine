import requests
import os
import subprocess
from datetime import datetime
import time

def download_live_stream(username, playback_url, output_folder):
    # Generate the output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_filename = f"{username}_{timestamp}.mp4"
    output_path = os.path.join(output_folder, output_filename)

    # Run ffmpeg to download the live stream with CBR and bitrate settings
    ffmpeg_command = [
        "ffmpeg",
        "-i", playback_url,
        "-b:v", "2500k",  # Set the bitrate to 2500 kbps
        "-minrate", "2500k",  # Set the minimum bitrate
        "-maxrate", "2500k",  # Set the maximum bitrate
        "-bufsize", "5000k",  # Set the buffer size
        "-c:v", "libx264",  # Use libx264 codec
        "-c:a", "aac",  # Use AAC codec for audio
        "-b:a", "128k",  # Set the audio bitrate to 128 kbps
        "-strict", "experimental",  # Allow experimental codecs (for AAC)
        output_path
    ]

    subprocess.run(ffmpeg_command)

    print(f"Download complete: {output_filename}")

def main():
    while True:  # Main loop
        target_username = "jkt48_lulu"  # Change this to your desired username
        output_folder = "output"

        try:
            for page in range(1, 11):  # Iterate through pages 1 to 10
                print(f"Searching '{target_username}' on page {page}...")
                
                # Prepare the GraphQL query variables
                variables = {
                    "page": page,
                    "category": "all"
                }

                # Make the GraphQL request with a timeout of 1 second
                response = requests.post("https://api.idn.app/graphql", json={
                    "query": '''
                    query GetLivestreams($page: Int!, $category: String!) {
                        getLivestreams(page: $page, category: $category) {
                            slug
                            title
                            playback_url
                            creator {
                                username
                            }
                        }
                    }
                    ''',
                    "variables": variables
                }, timeout=1)

                data = response.json().get("data", {}).get("getLivestreams", [])

                username_found = False

                # Check each live stream in the response
                for livestream in data:
                    username = livestream["creator"]["username"]
                    playback_url = livestream["playback_url"]

                    if username == target_username:
                        username_found = True
                        print(f"Username '{target_username}' found on page {page}.")
                        download_live_stream(username, playback_url, output_folder)

                # Uncomment the following line if you want to wait between pages
                # time.sleep(1)

            if not username_found:
                print(f"Username '{target_username}' not found in pages 1 to 7.")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 1 minute before continuing the process
        time.sleep(5)

if __name__ == "__main__":
    main()
