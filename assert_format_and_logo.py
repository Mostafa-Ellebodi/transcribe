from pathlib import Path
import moviepy.editor as mp
import os
import shutil

def clean_mkdir(path):
    if Path(path).exists():
        shutil.rmtree(path)
    os.makedirs(path)

out_videos = "converted_videos"
clean_mkdir(out_videos)

def convert_to_mp4_and_add_logo(logo_dir, video_dir):
    logo_image = str(os.listdir(logo_dir)[0])
    video_names = os.listdir(video_dir)

    for fn in video_names:
        video = mp.VideoFileClip(video_dir+"/"+ fn)

        logo = (mp.ImageClip(logo_dir+"/"+logo_image)
                .set_duration(video.duration)
                .resize(height=50) # if you need to resize...
                .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
                .set_pos(("right","top")))

        if fn.endswith('.mp4'):
            final = mp.CompositeVideoClip([video, logo])
            final.write_videofile(out_videos+ "/" +fn)
            
        else:
            try:
                fn_trim = os.path.splitext(fn)[0]
                final = mp.CompositeVideoClip([video, logo])
                final.write_videofile(out_videos+ "/" + fn_trim + ".mp4")
            except:
                print("Sorry format of file {} is not supported!" .format(fn) )
                continue
