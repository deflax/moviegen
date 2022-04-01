import os
import sys
from moviepy.editor import *

H = 720
W = 1280
SIZE = (W, H)
FPS = 24
VCODEC = 'libx264'
ACODEC = 'aac'
bold_font = 'Liberation-Sans-Bold'
plain_font = 'Liberation-Sans'

img_dir = "imgtest"

slideshow = []
for file in os.listdir(img_dir):
    if file.endswith(".png"):
        fullpath = os.path.join(img_dir, file)
        slideshow.append(fullpath)

startime = 0
clips = []

audio_clip = AudioFileClip('my_sound.mp3')
print('audio duration: ' + str(audio_clip.duration))
print('images found: ' + str(len(slideshow)))
step = int(audio_clip.duration) / int(len(slideshow))
print('calculated step: ' + str(step))

# Creating a list of ImageClip instances
for item in slideshow:
    duration = startime + step
    image = ImageClip(str(item)).set_duration(duration).set_start(startime).resize(height=H, width=W)
    text = TextClip("start: " + str(startime) + " duration: " + str(duration), font=bold_font, color='white', fontsize=48, interline=9).set_duration(duration - 2).set_start(startime + 1).set_pos(('left', 360)).crossfadein(.3)
    subtext = TextClip("File: " + str(item), font=plain_font, color='white', fontsize=32, interline=9).set_duration(duration - 4).set_start(startime + 2).set_pos(('left', 440)).crossfadein(.3)
    slide = CompositeVideoClip([image, text, subtext]).set_duration(duration)
    clips.append(slide)
    # increment next starttime with the step
    startime = startime + step

final_clip = CompositeVideoClip(clips, size=SIZE)
final_clip.set_audio(audio_clip)
final_clip.set_duration(audio_clip.duration)

final_clip.write_videofile("output.mp4", fps=FPS, codec=VCODEC, audio_codec=ACODEC)
