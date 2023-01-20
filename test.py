import cv2
import numpy as np

from obfuscate import Obfuscator

# Open the video using cv2
frames = []
cap = cv2.VideoCapture('test.mp4')
obfs = Obfuscator(12345, 1080)

ret = True
print("Shuffling....")
for x in range(60):
    print(x)
    ret, frame = cap.read() # read one frame from the 'capture' object; img is (H, W, C)
    shuffled = obfs.shuffle_frame(frame)
    if ret:
        frames.append(shuffled)
video = np.stack(frames, axis=0) # dimensions (T, H, W, C)

# let `video` be an array with dimensionality (T, H, W, C)
num_frames, height, width, _ = video.shape
print(num_frames, height, width)

filename = "saved.mp4"
codec_id = "mp4v" # ID for a video codec.
fourcc = cv2.VideoWriter_fourcc(*codec_id)
out = cv2.VideoWriter(filename, fourcc=fourcc, fps=60, frameSize=(width, height))

print("Writing....")
for frame in np.split(video, num_frames, axis=0):
    out.write(frame)

# Release the video capture
cap.release()