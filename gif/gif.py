import imageio.v3 as iio
import numpy as np

# Create a list to store images
images = []

# Use the files that actually exist in the directory
filenames = ['image.png', 'image1.png']  # Changed from team-pic1.png to actual files

# Read each image
for filename in filenames:
    images.append(iio.imread(filename))

# Save as GIF
iio.imwrite('animation.gif', images, duration=500, loop=0)
