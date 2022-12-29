import os
from PIL import Image
import instagram_scrape
import mosaic


def main():
    # Get the source JPEG and Instagram username from the user
    source_jpeg = input('Enter the path to the source JPEG: ')
    instagram_username = input('Enter the Instagram username: ')

    # Download the images from Instagram
    instagram_scrape.download_images(instagram_username)

    # Create the mosaic image
    mosaic.create_mosaic(source_jpeg, instagram_username, 50)


if __name__ == '__main__':
    main()
