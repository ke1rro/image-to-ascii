import PIL.Image
from file_format import get_file_format

ASCII_CHARS = ['@', '#', '$',
               '&', '?', '{',
               '}', '[', ']'
               '(', ')', '\\',
               '/',  '*', '=',
               '-' '+', ';',
               ':', ',', '.'
               ]
MAX_WIDTH = 300


def image_grayscale(image):
    image = image.convert('L')
    return image


def resize(image, new_width=MAX_WIDTH):
    current_width, current_heigth = image.size
    ratio = current_heigth / current_width / 1.6
    new_heigth = int(new_width * ratio)
    resized_image = image.resize((new_width, new_heigth))
    return resized_image


def get_pixel(image):
    pixels = image.getdata()
    pixeld_image = "".join([ASCII_CHARS[pixel // 49] for pixel in pixels])
    return pixeld_image


def get_image(new_width=MAX_WIDTH):
    while True:
        try:
            file_format = get_file_format()
            file_name = input('Please enter the file name located in the same folder as the python file: ')
            path = f'{file_name}.{file_format}'
            image_to_convert = PIL.Image.open(path)
            new_image = get_pixel(image_grayscale(resize(image_to_convert)))
            pixel_count = len(new_image)
            ascii_image = '\n'.join(new_image[i:(i+new_width)] for i in range(0, pixel_count, new_width))
            print(ascii_image)

            with open(file='ASCII_img.txt', mode='w') as file:
                for line in ascii_image:
                    file.write(line)

        except Exception as exc:
            print(f'Error: {exc}')
            print('Wrong data type or file not found. Please try again.')


get_image()
