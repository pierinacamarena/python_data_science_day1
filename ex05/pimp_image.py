import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from load_image import display_image_in_plot


def ft_invert(array: np.array) -> np.array:
    """
    Inverts the color of the image received.

    Parameters:
    - array (np.array): The array of the pixels of the image recevied

    Returns:
    - np.array
    """
    inverted_image = 255 - array
    display_image_in_plot(inverted_image, "Inverted image")
    return inverted_image

def ft_red(array) -> np.array:
    """
    Applying a red color filter to an image, while keeping the image shape the same

    Parameters:
    - array (np.array): The array of the pixels of the image recevied

    Returns:
    - np.array
    """

    red_component = array.copy()
    red_component[::,::,1:3]=0
    display_image_in_plot(red_component, 'Red filter')
    return red_component


def ft_green(array) -> np.array:
    """
    Applying a red color filter to an image, while keeping the image shape the same

    Parameters:
    - array (np.array): The array of the pixels of the image recevied

    Returns:
    - np.array
    """
    green_component = array.copy()
    green_component[:,:,0]=0
    green_component[:,:,2]=0
    display_image_in_plot(green_component, 'Green filter')
    return green_component


def ft_blue(array) -> np.array:
    """
    Applying a blue color filter to an image, while keeping the image shape the same

    Parameters:
    - array (np.array): The array of the pixels of the image recevied

    Returns:
    - np.array
    """
    blue_component=array.copy()
    blue_component[::,::,0:2]=0
    display_image_in_plot(blue_component, 'Blue filter')
    return blue_component


def ft_grey(array) -> np.array:
    """
    Turning an image to grey, while keeping the image shape the same

    Parameters:
    - array (np.array): The array of the pixels of the image recevied

    Returns:
    - np.array
    """
    grey_image = array.copy()

    # Retrieve components and average them
    
    blue = grey_image[:, :, 2]*(299/1000)
    green = grey_image[:, :, 1]*(587/1000)
    red = grey_image[:, :, 0]*(114/1000)

    grey = blue + green + red

    display_image_in_plot(grey, "Grey image")
    
    return grey
