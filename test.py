import cv2
import numpy as np
import random

def shuffle_frame(frame):
    """
    shift the rows and columns of the numpy representation of a frame by shift_x, shift_y
    """
    original_data = frame # Some random numbers to represent the original data to be shuffled
    data_length = original_data.shape[0]

    # Here we create an array of shuffled indices
    shuf_order = np.arange(data_length)
    np.random.shuffle(shuf_order)

    shuffled_data = original_data[shuf_order] # Shuffle the original data

    # Create an inverse of the shuffled index array (to reverse the shuffling operation, or to "unshuffle")
    unshuf_order = np.zeros_like(shuf_order)
    unshuf_order[shuf_order] = np.arange(data_length)

    return (shuffled_data, unshuf_order)

def unshift_frame(order):
    """
    unshift the rows and columns of the numpy representation of a frame by shift_x, shift_y
    """
    rows, cols = shifted_frame.shape[:2]
    M = np.float32([[1, 0, -shift_x], [0, 1, -shift_y]])
    return cv2.warpAffine(shifted_frame, M, (cols, rows))


# Open the video using cv2
cap = cv2.VideoCapture('test.mp4')

# Read the first frame
_, frame = cap.read()

shuffled, unshuffled = shift_frame(frame)
for x in range(1080):
    shuffled[x],_ = shift_frame(shuffled[x])
#shuffled[10], _ = shift_frame(shuffled[10])
cv2.imwrite("shuffled.jpg", shuffled)
cv2.imwrite("unshuffled.jpg", unshuffled)


# Release the video capture
cap.release()
