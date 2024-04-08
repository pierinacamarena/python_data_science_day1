from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    """
    Loads and converts an image to RGB format from a specified path,
    then returns its pixels as a numpy array.

    The function prints the image's shape and format,
    handles image loading errors by printing them, and ensures
    the image is converted to RGB format.
    It returns the image pixels as a numpy array or an empty list on failure.

    Parameters:
    - path (str): Path to the image file.

    Returns:
    - numpy.ndarray: Pixels of the RGB image or an empty list if loading fails.
    """
    try:
        # Load the image
        img = Image.open(path)

        # Retrieve image shape
        img_array = np.array(img)
        shape = np.shape(img_array)
        print(f"The shape of image is: {shape}")

        # Print image format
        print(f"Image format: {img.format}")

        # Ensure the image is in RGB format
        img_rgb = img.convert("RGB")

        # Print pixels content
        pixels = list(img_rgb.getdata())
        pixels_array = np.array(pixels)
        
        return pixels_array

    except IOError as e:
        print(f"Error loading the image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []
