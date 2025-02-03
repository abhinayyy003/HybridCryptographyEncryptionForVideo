import os
from moviepy.editor import *

# load clips
clip_01 = VideoFileClip('/Users/abhinay/Desktop/cryptography_PROJECT/aes/decrypted_video.mp4')
clip_02 = VideoFileClip('/Users/abhinay/Desktop/cryptography_PROJECT/des/decrypted_video.mp4')

# join + write
result_clip = concatenate_videoclips([clip_01, clip_02])
result_clip.write_videofile('combined.mp4')