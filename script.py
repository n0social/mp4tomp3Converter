from moviepy.editor import *

#Load
video = VideoFileClip("MP4File.mp4")
print("Converting Your Mp4 to Mp3")
#Extract
video.audio.write_audiofile("ConvertedMP3.mp3")
print("Ding! Completed.")

