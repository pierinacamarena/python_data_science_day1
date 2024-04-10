from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def display_image_in_plot(img: any, title: str) -> None:
    """
    Displays the input image using matplotlib with the specified title.
    The image is shown in grayscale when it has a single channel.

    Parameters:
    - img (any): The image to be displayed.
    - title (str): The title for the image display.

    Returns:
    - None
    """
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('on')
    plt.show()


def get_pixel_content(img: Image) -> np.array:
    """
    Converts an image to a numpy array representing its pixel content.

    Parameters:
    - img (Image): The image object to convert, supporting 'L' (grayscale)
    and 'RGB' modes.

    Returns:
    - numpy.ndarray: The image's pixel data as a numpy array
                     of shape (height, width, channels).
                     Grayscale images return a shape of (height, width, 1),
                     and RGB images return a shape of (height, width, 3).
    """
    if img.mode == "L":
        # Convert to a numpy array & reshape it to (Height, Width, 1)
        pixels_array = np.array(img).reshape(img.size[1], img.size[0], 1)
    else:
        img_rgb = img.convert("RGB")
        # Convert to a numpy array & reshape it to (Height, Width, 3)
        pixels_array = np.array(img_rgb).reshape(img.size[1], img.size[0], 3)

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

        print(f"Number of channels: {num_channels} \n")

        pixels_array = get_pixel_content(img)

        # Show image in plot
        display_image_in_plot(img, "Original image")

        return pixels_array, img

    except IOError as e:
        print(f"Error loading the image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return ""
