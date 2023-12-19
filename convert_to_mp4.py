from pathlib import Path
import subprocess

def convert_images_to_video(image_dir, start_num, end_num, input_prefix, output_filename, frame_rate=24):
    image_dir = Path(image_dir)
    temp_dir = image_dir / "temp_images"
    temp_dir.mkdir(exist_ok=True)

    # Rename and copy images to the temporary directory
    for i in range(start_num, end_num + 1):
        original_file = image_dir / f"{input_prefix}{i:04}.jpg"
        if original_file.exists():
            renamed_file = temp_dir / f"img{i:04d}.jpg"
            original_file.rename(renamed_file)
        else:
            print(f"File {original_file} not found.")
            return

    # Full path for the output video
    output_file = image_dir / output_filename

    # Run ffmpeg to convert images to video
    cmd = [
        "ffmpeg",
        "-framerate", str(frame_rate),
        "-i", str(temp_dir / "img%04d.jpg"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        str(output_file)
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error in ffmpeg command: {e}")
    finally:
        # Clean up the temporary directory
        for file in temp_dir.glob("*.jpg"):
            file.unlink()
        temp_dir.rmdir()

# Usage
# For example, if your images are in '/path/to/images' directory
convert_images_to_video('/path/to/images', 872, 2613, "IMG_", "output_video.mp4")
