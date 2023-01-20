import cv2
import numpy as np

from obfuscate import Obfuscator

# Open the video using cv2
cap = cv2.VideoCapture('test.mp4')
obfs = Obfuscator(12345, 1080)
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(fps, cv2.CAP_PROP_FOURCC, frameSize)

# Create video writer obj
out = cv2.VideoWriter("saved.mp4", fourcc, fps, frameSize, isColor=True)

# write to output
counter = 1
while True:
    ret, frame = cap.read()
    if not ret:
        break
    print("Writing frame ", counter)
    counter += 1
    out.write(obfs.shuffle_frame(frame))
    #out.write(frame)

#Release video writier and capture objeccts
out.release()
cap.release()