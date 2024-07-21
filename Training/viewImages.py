import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the .npy file
file_path = 'diffusion\How-Diffusion-Models-Work\Training\sprites_1788_16x16.npy'
sprites = np.load(file_path)

# Step 2: Inspect the data
print("Shape of the array:", sprites.shape)

# Step 3: Display the images
# Assuming the sprites array is of shape (number_of_sprites, height, width, channels)
num_sprites_to_display = 10  # Number of sprites you want to display
plt.figure(figsize=(20, 2))
for i in range(num_sprites_to_display):
    plt.subplot(1, num_sprites_to_display, i + 1)
    plt.imshow(sprites[i])
    plt.axis('off')

plt.show()
