import os
from PIL import Image

# Set the folder path
folder_path = "/home/nikola/projects/pxo/data/prepared/living_room/images"
folder_path_resized= "/home/nikola/projects/pxo/data/prepared/living_room/images_8"

# resize factor
resize_factor = 8

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image file
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)

        # Calculate the new dimensions
        new_width = img.width // resize_factor
        new_height = img.height // resize_factor

        # Resize the image
        img_resized = img.resize((new_width, new_height))

        # Save the resized image
        new_filename = filename
        new_img_path = os.path.join(folder_path_resized, new_filename)
        img_resized.save(new_img_path)