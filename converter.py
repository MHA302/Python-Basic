from PIL import Image


def convert_image(input_image):
    """Gets a PIL image file and returns its grayscale version"""
    img = Image.open(input_image)
    gray_img = img.convert('L')
    return gray_img