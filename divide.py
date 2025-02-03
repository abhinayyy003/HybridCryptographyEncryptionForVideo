import cv2
import numpy as np
import os

# Input video file
input_video_file = "input_video.mp4"

# Output video file names
aes_output_file = "aes_input.mp4"
des_output_file = "des_input.mp4"

# Open the input video file
cap = cv2.VideoCapture(input_video_file)

# Get the frames per second (fps) and total number of frames
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Codec for the output videos (change to 'H264')
fourcc = cv2.VideoWriter_fourcc(*'H264')

# Calculate the frame indices for the 70% and 30% portions
aes_frame_count = int(frame_count * 0.7)
des_frame_count = frame_count - aes_frame_count

# Create VideoWriters for the output videos with the new codec
aes_writer = cv2.VideoWriter(aes_output_file, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))
des_writer = cv2.VideoWriter(des_output_file, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

# Process frames and write them to the output videos
frame_index = 0
while frame_index < frame_count:
    ret, frame = cap.read()
    if frame_index < aes_frame_count:
        aes_writer.write(frame)  # Write to aes_input video
    else:
        des_writer.write(frame)  # Write to des_input video
    frame_index += 1

# Release the VideoWriters and close the input video
aes_writer.release()
des_writer.release()
cap.release()

print("Video split and saved successfully.")
