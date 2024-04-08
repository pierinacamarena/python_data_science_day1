from load_image import ft_load, get_pixel_content, display_image_in_plot
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def zoom_image(img: any) -> any:
    """
    Crops the input image to a predefined rectangular area and saves the cropped image
    as 'zoomed_image.jpg'.

    Parameters:
    - img (any): The input image to be zoomed. Must support the `crop` and `save` methods.

    Returns:
    - any: The cropped (zoomed) image.
    """
    left, upper, right, lower = 400, 100, 800, 500
    zoomed_image = img.crop((left, upper, right, lower))
    zoomed_image.save("zoomed_image.jpg")
    return zoomed_image


def set_image_to_grayscale(img: any) -> any:
    """
    Converts the input image to grayscale.

    Parameters:
    - img (any): The input image to be converted. Must support the `convert` method.

    Returns:
    - any: The grayscale image.
    """
    return img.convert("L")


def zoom_and_display_info(img: any) -> None:
    """
    Processes an input image by zooming into a predefined area, converting it to grayscale,
    and then displaying it with matplotlib. The image is displayed with the title 'Zoomed image'.

    Parameters:
    - img (any): The input image to be processed.

    Returns:
    - None
    """
    zoomed_image = zoom_image(img)
    grayscale_image = set_image_to_grayscale(zoomed_image)
    display_image_in_plot(grayscale_image, "Zoomed image")


def format_printing(arr: np.ndarray) -> None:
    bottom_arr_size = arr[-1].shape[0]
    top_array = arr[0, :3, :]
    bottom_array = arr[-1, -3:bottom_arr_size, :]
    full_arr = np.stack([top_array, bottom_array], axis=0)
    # print(full_arr)
    print(f"[{top_array}")
    print("     ...")
    print(f"{bottom_array}]")


def main():

    # Loading, treating and printing original image

    pixels_array, img_array, img = ft_load('animal.jpeg')
    print(pixels_array)
    # format_printing(pixels_array)

    # Zooming and converting to grascale

    zoomed_image = zoom_image(img)
    grayscale_image = set_image_to_grayscale(zoomed_image)
    print(f"New shape after slicing: {zoomed_image.size}")
    zoom_image_pixel_content = get_pixel_content(grayscale_image)

    # Displaying pixels array and zoomed image
    print(zoom_image_pixel_content)
    zoom_and_display_info(img)

if __name__ == "__main__":
    main()