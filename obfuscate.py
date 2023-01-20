import numpy as np

class Obfuscator:

    def __init__(self, seed, height):
        self.seed = seed
        self.height = height
    
    def __shuffle_row(self, frame):
        """
        shift the rows and columns of the numpy representation of a frame by shift_x, shift_y
        """
        original_data = frame # Some random numbers to represent the original data to be shuffled
        data_length = original_data.shape[0]

        # Here we create an array of shuffled indices
        shuf_order = np.arange(data_length)
        np.random.seed(self.seed)
        np.random.shuffle(shuf_order)

        return original_data[shuf_order]

    def __unshuffle_row(self, frame):
        """
        unshift the rows and columns of the numpy representation of a frame by shift_x, shift_y
        """
        original_data = frame
        data_length = original_data.shape[0]

        shuf_order = np.arange(data_length)
        np.random.seed(self.seed)
        np.random.shuffle(shuf_order)

        unshuf_order = np.zeros_like(shuf_order)
        unshuf_order[shuf_order] = np.arange(data_length)

        return original_data[unshuf_order]

    def shuffle_frame(self, frame):
        shuffled = self.__shuffle_row(frame)
        for x in range(self.height):
            shuffled[x] = self.__shuffle_row(shuffled[x])
        return shuffled

    def unshuffle_frame(self, frame):
        unshuffled = self.__unshuffle_row(frame)
        for x in range(self.height):
            unshuffled[x] = self.__unshuffle_row(unshuffled[x])
        return unshuffled
