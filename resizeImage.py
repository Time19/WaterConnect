import os
from PIL import Image


def resize_images(input_folder):
    # Define the size for the resized images
    new_size = (100, 100)

    # Create a new folder inside the input folder
    output_folder = os.path.join(input_folder, 'resized_images')
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a PNG image
        if filename.endswith('.png'):
            # Open an image file
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Resize the image
                img_resized = img.resize(new_size)
                # Save the resized image to the new folder
                img_resized.save(os.path.join(output_folder, filename))
                print(f"Resized and saved {filename}")

def count():
    int = 0
    for _ in range(3):
        for _ in range(3):
            print(int)
            int = int + 1
# Example usage

if __name__ == "__main__":
    input_folder = "C:/Users/gil/Desktop/images/200x200"
    resize_images(input_folder)
    count()


