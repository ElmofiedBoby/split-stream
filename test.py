import cv2
import numpy as np

from obfuscate import Obfuscator

# Open the video using cv2
cap = cv2.VideoCapture('test.mp4')

# Read the first frame
_, frame = cap.read()

obfs = Obfuscator(12345, 1080)

shuffled = obfs.shuffle_frame(frame)
unshuffled = obfs.unshuffle_frame(shuffled)

cv2.imwrite("shuffled.jpg", shuffled)
cv2.imwrite("unshuffled.jpg", unshuffled)


# Release the video capture
cap.release()