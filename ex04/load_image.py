from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def display_image_in_plot(img: any, title: str) -> None:
    """
    Displays the input image using matplotlib with the specified title. The image is shown in grayscale.

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


def extract_edges(arr: np.ndarray) -> np.ndarray:
    """
    Extracts the edges of an image array. For a grayscale image (assumed to be encapsulated as a 3D array with depth 1),
    it extracts the first and last pixels of each row. For an RGB image, it extracts the first three and last three
    columns from each row.

    Parameters:
    - arr (np.ndarray): The input image array.

    Returns:
    - np.ndarray: An array containing the extracted edges.
    """
    # Determine if the image is grayscale (depth = 1) or RGB (depth = 3)
    depth = arr.shape[2]
    
    if depth == 1:
        # Grayscale: extract the first and last pixels from each row
        first_elements = arr[:, 0, :]
        last_elements = arr[:, -1, :]
        # Combine the first and last elements
        result = np.concatenate((first_elements, last_elements), axis=1)
    elif depth == 3:
        # RGB: extract the first three and last three columns from each row
        first_three_columns = arr[0:, :1, :]
        last_three_columns = arr[:, -3:, :]
        # Concatenate the first three and last three columns
        result = np.concatenate((first_three_columns, last_three_columns), axis=1)
    else:
        # Handle unexpected depth (not 1 or 3)
        raise ValueError("Unsupported image depth: {}. Expected 1 (grayscale) or 3 (RGB).".format(depth))
    
    return result


def get_pixel_content(img: Image) -> np.array:
    """
    Converts an image to a numpy array representing its pixel content.

    Parameters:
    - img (Image): The image object to convert, supporting 'L' (grayscale) and 'RGB' modes.

    Returns:
    - numpy.ndarray: The image's pixel data as a numpy array of shape (height, width, channels).
                     Grayscale images return a shape of (height, width, 1), and RGB images return
                     a shape of (height, width, 3).

    The function first checks the image mode. If it's grayscale ('L'), it converts the image
    directly to a numpy array with a single channel. For RGB images, or images converted to RGB,
    it converts to a numpy array with three channels. Other image modes are converted to 'RGB'.
    """
    if img.mode == "L":
        # Getting all pixels into a list
        pixels = list(img.getdata())
        # Convert to a numpy array and reshape it to have a shape of (Height, Width, 1)
        pixels_array = np.array(img).reshape(img.size[1], img.size[0], 1)
    else:
        img_rgb = img.convert("RGB")
        # Getting all pixels into a list
        pixels = list(img_rgb.getdata())
        # Convert to a numpy array and reshape it to have a shape of (Height, Width, 3)
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

        return pixels_array, img_array, img

    except IOError as e:
        print(f"Error loading the image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return ""
