import os
from PIL import Image


def create_mosaic(target_image_path, source_folder_path, mosaic_size):
    # Open the target image and get its width and height
    target_image = Image.open(target_image_path)
    target_image_width, target_image_height = target_image.size

    # Create a blank image to hold the mosaic
    mosaic_image = Image.new('RGB', (target_image_width, target_image_height))

    # Iterate over the rows and columns of the target image
    for i in range(0, target_image_height, mosaic_size):
        for j in range(0, target_image_width, mosaic_size):
            # Get the pixel at the current position
            pixel = target_image.getpixel((j, i))

            # Find the closest matching image in the source folder
            closest_image = find_closest_image(pixel, source_folder_path)

            # Open the closest image and paste it into the mosaic
            mosaic_image.paste(Image.open(closest_image), (j, i))

    # Save the mosaic image
    mosaic_image.save('mosaic.jpg')


def find_closest_image(pixel, source_folder_path):
    # Set a large initial distance
    closest_distance = 1000000
    closest_image = None

    # Iterate over all images in the source folder
    for image_path in os.listdir(source_folder_path):
        # Open the image and get its average pixel value
        image = Image.open(os.path.join(source_folder_path, image_path))
        avg_pixel = get_average_pixel(image)

        # Calculate the distance between the pixel and the average pixel value
        distance = calculate_distance(pixel, avg_pixel)

        # If the distance is smaller than the current closest distance, update the closest image and distance
        if distance < closest_distance:
            closest_distance = distance
            closest_image = image_path

    return closest_image


def get_average_pixel(image):
    # Get the width and height of the image
    width, height = image.size

    # Initialize variables to store the sum of the red, green, and blue values
    red_sum = 0
    green_sum = 0
    blue_sum = 0

    # Iterate over all pixels in the image
    for i in range(width):
        for j in range(height):
            # Get the pixel at the current position
            pixel = image.getpixel((i, j))

            # Add the red, green, and blue values to the sums
            red_sum += pixel[0]
            green_sum += pixel[1]
            blue_sum += pixel[2]

    # Calculate the average red, green, and blue values
    avg_red = red_sum / (width * height)
    avg_green = green_sum / (width * height)
    avg_blue = blue_sum / (width * height)

    # Return the average pixel value as a tuple

    return (avg_red, avg_green, avg_blue)


def calculate_distance(pixel1, pixel2):
    # Calculate the Euclidean distance between the two pixels
    red_distance = pixel1[0] - pixel2[0]
    green_distance = pixel1[1] - pixel2[1]
    blue_distance = pixel1[2] - pixel2[2]
    distance = (red_distance ** 2 + green_distance **
                2 + blue_distance ** 2) ** 0.5

    return distance


# Example usage
# create_mosaic('target.jpg', 'source_folder', 50)
