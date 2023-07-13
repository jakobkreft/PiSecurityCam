# Raspberry Pi USB Web Cam Security Camera

This is a simple Python script to record videos from a USB web camera on a Raspberry Pi. The script uses FFMPEG to record videos for a specified duration and saves them to a local directory. The script also automatically deletes old video files to prevent the disk from filling up.
## Installation

1. Clone this repository to your Raspberry Pi.
1. Install FFMPEG by running `sudo apt-get install ffmpeg`.
1. Install Python 3 if it is not already installed on your Raspberry Pi.

## Configuration

The script uses a configuration file named `config.json` to control its behavior. The following configurations are available:

- `camera_location`: The location of the USB camera. This is typically /dev/video0.
- `video_duration`: The duration of each recorded video in seconds.
- `max_files`: The maximum number of video files to keep in the videos directory. Set this based on your available disk space.
- `recording_enabled`: If set to true, the script will record videos during the specified hours.
- `recording_hours`: The start and end times for recording videos. The format is HH:MM.
- `stop_script`: If set to true, the script will stop running. Default is false.

## Usage

To start the script, run `python3 seccam.py`. The script will run indefinitely until the stop_script configuration is set to true.

To run the script in the background and keep it running after the terminal is closed, use the following command:

`nohup python3 seccam.py >> logfile.log 2>&1 &`

This redirects output to `logfile.log` and detaches the script from the terminal session. 

If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
## License

This project is licensed under the MIT License. See the LICENSE file for details.
