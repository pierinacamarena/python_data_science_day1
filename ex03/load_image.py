from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def display_image_in_plot(img: any, title: str) -> None:
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('on')
    plt.show()


def get_pixel_content(img: any) -> any:
    # Ensure the image is in RGB format
    img_rgb = img.convert("RGB")

    # Pixels content
    pixels = list(img_rgb.getdata())
    pixels_array = np.array(pixels)

    return pixels_array


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

        # Get the size of the image
        width, height = img.size

        print(f"Width - x axis: {width}px \nHeight - y axis: {height}px")

        # Get channel
        if img_array.ndim == 3:
            num_channels = img_array.shape[2]
        else:
            num_channels = 1
            
        print(f"Number of channels: {num_channels}")

        pixels_array = get_pixel_content(img)

        # # Ensure the image is in RGB format
        # img_rgb = img.convert("RGB")

        # # Pixels content
        # pixels = list(img_rgb.getdata())
        # pixels_array = np.array(pixels)

        #Show image
        # img.show()

        #show image in plot
        display_image_in_plot(img, "Original image")


        return pixels_array, img_array, img

    except IOError as e:
        print(f"Error loading the image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return ""
