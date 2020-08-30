# Subtiltes generation, subtitles embedding and videos watermarking

This repository serves the following purposes:

- Adding watermark to either a single or multiple videos
- Transcribing audio files from video files into .srt formatted text files for subtitling purposes using Googles Speech-to-Text and Google Cloud Storage APIs. 
- Embeding srt content into the output videos.
(some media players don't show subtitles by default, so you may need to enable it manually)


## Instructions for use
There are two options:
### 1. Google Colab
This is the most easy and convenient way 
1. In transcribe folder add the logo in logos directory and videos in videos directory
2. Upload "video_subtitles.ipynb" the notebook to google drive.
3. Upload transcribe directory to the opened notebook and run the cells.
That's it! the code will run automatically and downloads the output videos after finishing.

### 2. Running on the local machine

Use the Cloud Platform Console to create a new Cloud
Platform project and enable billing: https://console.cloud.google.com/
(Skip if project already set up)

Enable the Google Speech to Text API
in APIs and Services in new project dashboard

Set up a storage bucket in Google Cloud Storage

Download, install and set up Google SDK
https://cloud.google.com/sdk/
(authenticate your machine by following the auth instructions)

Install ffmpeg
,,,
    sudo apt update
    sudo apt install ffmpeg
,,,
Set your virtual environment

If you don't have virtualenv, install it using pip.
'''
    sudo pip install virtualenv
'''
Create an isolated Python environment, and install dependencies:
'''
virtualenv env
source env/bin/activate
pip install -r requirements.txt
'''
In goog.py change the bucket_name variable to the name of the storage bucket you wish to use

To run transcription script add video files to videos directory and logo to logo directory

Then run:

'''
    python autorun.py /path/to/logo/directory /path/to/videos/directory
'''

The script will automatically strip the audio files from the video and convert them to .ogg format

The it uploads the audio to the gcloud storage bucket and
then passes its gcs_uri to the speech to text API for processing

When finished, it outputs both the .srt formatted file and raw text file into the videos directory

The converted videos are found in a subdirectory called "converted_videos" under videos directory. 

Note that if the program errors, it terminates as to not potentially abuse any API quota limits
