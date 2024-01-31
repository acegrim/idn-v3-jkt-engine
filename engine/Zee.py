import requests
import os
import subprocess
from datetime import datetime
import time

def download_live_stream(username, playback_url, output_folder):
    # Generate the output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_filename = f"{username}_{timestamp}.mp4"
    
    # Add a counter for handling duplicate filenames
    counter = 1
    while os.path.exists(os.path.join(output_folder, output_filename)):
        output_filename = f"{username}_{timestamp}_{counter}.mp4"
        counter += 1

    output_path = os.path.join(output_folder, output_filename)

    # Run ffmpeg to download the live stream
    ffmpeg_command = [
        "ffmpeg",
        "-i", playback_url,
        "-c", "copy",
        output_path
    ]

    subprocess.run(ffmpeg_command)

    print(f"Download complete: {output_filename}")

def is_stream_lagging(playback_url, max_duration=120):
    # Check if the stream duration is less than the max_duration
    try:
        response = requests.get(playback_url, timeout=5)
        data = response.json()
        duration = data.get("duration", 0)
        print(f"Stream Duration: {duration} seconds")

        if duration < max_duration:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking stream duration: {e}")
        return True  # Assume lagging in case of an error

def main():
    while True:  # Main loop
        target_username = "jkt48_zee"  # Change this to your desired username
        output_folder = "output"

        try:
            for page in range(1, 8):  # Iterate through pages 1 to 7
                print(f"Searching '{target_username}' on page {page}...")
                
                # Prepare the GraphQL query variables
                variables = {
                    "page": page,
                    "category": "all"
                }

                # Make the GraphQL request
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
                })

                data = response.json().get("data", {}).get("getLivestreams", [])

                username_found = False

                # Check each live stream in the response
                for livestream in data:
                    username = livestream["creator"]["username"]
                    playback_url = livestream["playback_url"]

                    if username == target_username:
                        username_found = True
                        print(f"Username '{target_username}' found on page {page}.")

                        while is_stream_lagging(playback_url):
                            print("Stream Lagging. Waiting...")
                            time.sleep(30)  # Wait for 30 seconds before checking again

                        download_live_stream(username, playback_url, output_folder)
                        break  # Stop searching across pages once found

                # If the username is found, exit the loop
                if username_found:
                    break

            if not username_found:
                print(f"Username '{target_username}' not found in pages 1 to 7.")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 5 seconds before continuing the process
        time.sleep(5)

if __name__ == "__main__":
    main()
