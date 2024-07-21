# Load the array from the .npy file
import numpy as np

loaded_array = np.load('diffusion\How-Diffusion-Models-Work\Training\sprites_1788_16x16.npy')

#
# print(loaded_array[:5])
# Output:
# [[1 2 3]
#  [4 5 6]]


print(loaded_array[0])
