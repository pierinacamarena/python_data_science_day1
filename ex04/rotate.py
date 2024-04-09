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


def zoom_and_display_info(img: any) -> any:
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
    print(f"The shape of image is: {grayscale_image.size}")
    display_image_in_plot(grayscale_image, "Zoomed image")
    return grayscale_image


def format_printing(arr: np.ndarray) -> None:
    bottom_arr_size = arr[-1].shape[0]
    top_array = arr[0, :3, :]
    bottom_array = arr[-1, -3:bottom_arr_size, :]
    full_arr = np.stack([top_array, bottom_array], axis=0)
    # print(full_arr)
    print(f"[{top_array}")
    print("     ...")
    print(f"{bottom_array}]")

def transpose_image(arr):
    axes = tuple(reversed(range(arr.ndim)))
        
    # Create an iterator over all possible index combinations in the new axes order
    new_shape = [arr.shape[axis] for axis in axes]
    result = np.empty(new_shape, dtype=arr.dtype)
    
    for index in np.ndindex(result.shape):
        # Map the new index back to the original index
        orig_index = tuple(index[axes.index(i)] for i in range(arr.ndim))
        result[index] = arr[orig_index]
        
    return result


def main():

    pixels_array, img_array, img = ft_load('animal.jpeg')
    print(pixels_array)

    grayscale_image = zoom_and_display_info(img)

    zoom_image_pixel_content = get_pixel_content(grayscale_image)

    print(zoom_image_pixel_content)

    transposed_image = transpose_image(np.array(grayscale_image))

    transpose_pil_image = Image.fromarray(transposed_image)

    print(f"\nThe new shape after traspose is: {transpose_pil_image.size}")

    display_image_in_plot(transposed_image, 'Rotated Image')

    print(transposed_image)


    

if __name__ == "__main__":
    main()