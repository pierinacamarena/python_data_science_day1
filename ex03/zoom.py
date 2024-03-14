from load_image import ft_load, display_image_in_plot, get_pixel_content
import matplotlib.pyplot as plt
from PIL import Image


def zoom_image(img: any) -> any:

    left, upper, right, lower = 400, 100, 800, 500
    zoomed_image = img.crop((left, upper, right, lower))

    zoomed_image.save("zoomed_image.jpg")

    return zoomed_image


def set_image_to_grayscale(img: any) -> any:
    return img.convert("L")


def zoom_and_display_info(img: any) -> None:
    zoomed_image = zoom_image(img)
    grayscale_image = set_image_to_grayscale(zoomed_image)

    display_image_in_plot(grayscale_image, "Zoomed image")


def main():

    pixels_array, img_array, img = ft_load('animal.jpeg')
    print(pixels_array)

    zoomed_image = zoom_image(img)
    grayscale_image = set_image_to_grayscale(zoomed_image)

    print(f"New shape after cropping: {zoomed_image.size}")

    zoom_and_display_info(img)

    zoom_image_pixel_content = get_pixel_content(grayscale_image)

    print(zoom_image_pixel_content)
    

if __name__ == "__main__":
    main()