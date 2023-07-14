import os
import time
import json
from datetime import datetime, time as dtime

# Load configurations from config file
with open('config.json') as f:
    config = json.load(f)

# Get configurations
VIDEO_DURATION = config["video_duration"]  # in seconds, 5 minutes
MAX_FILES = config["max_files"]  # number of files to keep, 2 days worth of 5 min videos (60*24*2 / 5)

# Create directory to store video files if it doesn't exist
if not os.path.exists("videos"):
    os.makedirs("videos")

while True:
    # Load config file
    with open('config.json') as f:
        config = json.load(f)

    # Check if script should stop
    if config['stop_script']:
        print("Stopping script.")
        break

    # Check if recording is enabled
    if not config['recording_enabled']:
        print("Recording is disabled.")
        time.sleep(60)
        continue

    # Get current time
    current_time = datetime.now().time()

    # Check if current time is within recording hours
    start_time = dtime.fromisoformat(config['recording_hours']['start'])
    end_time = dtime.fromisoformat(config['recording_hours']['end'])
    if not start_time <= current_time <= end_time:
        print("Not within recording hours.", current_time)
        time.sleep(60)
        continue

    #camera location
    CAMERA_LOCATION = config["camera_location"]  # USB camera location
    # Generate filename with current timestamp
    filename = time.strftime("%Y%m%d-%H%M%S") + ".mp4"
    filepath = os.path.join("videos", filename)

    # Record video for specified duration with resolution 854x480 and frame rate of 5
    #os.system(f"ffmpeg -t {VIDEO_DURATION} -f v4l2 -video_size 854x480 -framerate 5 -i {CAMERA_LOCATION} {filepath}") # real speed of playback, but filesizes are larger
    os.system(f"ffmpeg -t {VIDEO_DURATION} -f v4l2 -video_size 854x480 -framerate 5 -i {CAMERA_LOCATION} -vf 'setpts=0.1667*PTS' -r 30 {filepath}") # plays at 30fps so its a speed up and file sizes are smaller.

    # Remove oldest files if maximum number of files is exceeded
    files = sorted(os.listdir("videos"))
    if len(files) > MAX_FILES:
        for file in files[:len(files) - MAX_FILES]:
            os.remove(os.path.join("videos", file))

    # Wait for 5 seconds before recording the next video
    time.sleep(1)
