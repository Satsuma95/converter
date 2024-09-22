import os
import moviepy
from moviepy.editor import *
video = VideoFileClip(r"D:\IMG_7518.MP4")
video.audio.write_audiofile("movie_sound.mp3")