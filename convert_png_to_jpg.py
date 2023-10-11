from PIL import Image
from pathlib import Path

def convert_png_to_jpg(png_path, jpg_path):
    # Open the .png image
    image = Image.open(png_path)
    # Convert the image to 'RGB' (removes the alpha channel)
    rgb_image = image.convert('RGB')
    # Save the image with .jpg format
    rgb_image.save(jpg_path)
    print(f"Converted {png_path} to {jpg_path}")

def main(folder_path):
    folder = Path(folder_path)

    # Create a new directory with "_jpg" appended to the original directory name
    jpg_folder = folder.parent / (folder.name + "_jpg")
    jpg_folder.mkdir(exist_ok=True)

    # Iterate over all the .png files in the folder
    for png_file in folder.glob("*.png"):
        # Get the corresponding .jpg filename
        jpg_file = jpg_folder / png_file.name.replace(".png", ".jpg")
        # Convert the .png to .jpg
        convert_png_to_jpg(png_file, jpg_file)

if __name__ == "__main__":
    # Provide the path to the folder here
    folder_path = './path_to_your_folder'
    main(folder_path)
