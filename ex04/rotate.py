from load_image import ft_load, get_pixel_content, display_image_in_plot
from PIL import Image
import numpy as np


def zoom_image(img: Image) -> Image:
    """
    Crops the input image to a predefined rectangular area and saves
    the cropped image as 'zoomed_image.jpg'.

    Parameters:
    - img (Image): The input image to be zoomed.

    Returns:
    - Image: The cropped (zoomed) image.
    """
    left, upper, right, lower = 400, 100, 800, 500
    zoomed_image = img.crop((left, upper, right, lower))
    zoomed_image.save("zoomed_image.jpg")
    return zoomed_image


def set_image_to_grayscale(img: Image) -> Image:
    """
    Converts the input image to grayscale.

    Parameters:
    - img (Image): The input image to be converted.

    Returns:
    - Image: The grayscale image.
    """
    return img.convert("L")


def zoom_and_display_info(img: Image) -> Image:
    """
    Processes an input image by zooming into a predefined area,
    converting it to grayscale,and then displaying it with matplotlib.
    The image is displayed with the title 'Zoomed image'.

    Parameters:
    - img (Image): The input image to be processed.

    Returns:
    - Image
    """
    zoomed_image = zoom_image(img)
    grayscale_image = set_image_to_grayscale(zoomed_image)
    print(f"\n The shape of image after zoom is: {grayscale_image.size}")
    display_image_in_plot(grayscale_image, "Zoomed image")
    return grayscale_image


def format_printing(arr: np.ndarray) -> None:
    """
    Prints the top 3 elements of the first sub-array, an ellipsis,
    and the bottom 3  elements of the last sub-array from the input
    numpy array. Designed for numpy arrays with at least one sub-array
    and elements to support the slicing.

    Parameters:
    - arr (np.ndarray): The input numpy array to format and print.

    Returns:
    - None: This function does not return any value.
    """
    bottom_arr_size = arr[-1].shape[0]
    top_array = arr[0, :3, :]
    bottom_array = arr[-1, -3:bottom_arr_size, :]
    full_arr = np.stack([top_array, bottom_array], axis=0)
    print(full_arr)
    print(f"[{top_array}")
    print("     ...")
    print(f"{bottom_array}]")


def ft_transpose_image(arr: np.ndarray) -> np.ndarray:
    """
    Transposes the given numpy array by reversing its axes. This flips
    the array's dimensions, similar to rotating or flipping an image.

    Parameters:
    - arr (np.ndarray): Input array to be transposed.

    Returns:
    - np.ndarray: A new numpy array with the same elements as `arr` but with
      its axes reversed.
    """

    # Reverse the elements of the range of the array dimension
    # Crucial step because it sets up how the array will be reoriented
    axes = tuple(reversed(range(arr.ndim)))

    # New size of each dimension of new array, with flipped order
    new_shape = [arr.shape[axis] for axis in axes]

    # Set up new "empty" array with the specified shape and dtype
    result = np.empty(new_shape, dtype=arr.dtype)

    # Iterate over every possible coordinate of the array
    for index in np.ndindex(result.shape):
        # Retrieve the corresponding value in the original array
        orig_index = tuple(index[axes.index(i)] for i in range(arr.ndim))
        result[index] = arr[orig_index]

    return result


def main():

    # Loading original image and printing its pixels
    pixels_array, img = ft_load('animal.jpeg')
    print(pixels_array)

    # Zoom and grayscale + plotting it & printing its shape & pixels
    grayscale_image = zoom_and_display_info(img)
    zoom_image_pixel_content = get_pixel_content(grayscale_image)
    print(zoom_image_pixel_content)

    # Transpose(rotate) the image + plotting it & print its shape & pixels
    transposed_image = ft_transpose_image(np.array(grayscale_image))
    transpose_pil_image = Image.fromarray(transposed_image)
    print(f"\nThe new shape after traspose is: {transpose_pil_image.size}")
    display_image_in_plot(transposed_image, 'Rotated Image')
    print(transposed_image)


if __name__ == "__main__":
    main()
