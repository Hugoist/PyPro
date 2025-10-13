from concurrent.futures import ProcessPoolExecutor
from PIL import Image
import os


def resize_image(filename: str) -> None:
    """ Resize and save image """
    img = Image.open(filename)
    img_resized = img.resize((128, 128))
    new_name = f"resized_{os.path.basename(filename)}"
    img_resized.save(new_name)
    print(f"{filename} оброблено у {new_name}")


# List of images to resize
images = ["file1.jpg", "file2.jpg", "file3.jpg"]

# Use multiprocessing for CPU-bound tasks
with ProcessPoolExecutor() as executor:
    executor.map(resize_image, images)

print("Усі зображення оброблено!")
