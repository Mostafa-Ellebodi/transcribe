import moviepy.editor as mp
import sys

def add_logo(logo_dir, video_dir):
    logo_image = str(os.listdir("/content/transcribe/logo")[0])
    video_file = os.listdir("/content/transcribe/videos")

    for fn in video_file:
      video = mp.VideoFileClip(video_dir+"/"+ fn)

      logo = (mp.ImageClip(logo_dir+"/"+logo_image)
                .set_duration(video.duration)
                .resize(height=50) # if you need to resize...
                .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
                .set_pos(("right","top")))

      final = mp.CompositeVideoClip([video, logo])
      final.write_videofile("/content/transcribe/outputs_logo/"+fn)

logo_dir = sys.argv[1]
video_dir = sys.argv[2]
add_logo(logo_dir, video_dir)
