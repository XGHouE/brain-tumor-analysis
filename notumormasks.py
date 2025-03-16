import shutil
import os

# Define the path of the original image
image_path = "notumor/3065.jpg"  # Change this if needed

directory = os.path.dirname(image_path)  # Get the directory of the image

for i in range(3066, 4660):  # Loop from 3066 to 4659
    new_image_path = os.path.join(directory, f"{i}.jpg")
    shutil.copy(image_path, new_image_path)  # Copy the image

print("Copies created successfully.")