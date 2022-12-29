# Mosaic Maker
Transform any image into a stunning mosaic masterpiece using Instagram images with this Python program! Simply specify the source JPEG and an Instagram username, and the program will download the images from the user's account and create a mosaic using the Pillow library.

## Features
Easily create mosaic images from a collection of JPEGs
Customize the size of the mosaic tiles
Downloads images from Instagram using the requests and BeautifulSoup libraries
Uses the Pillow library for powerful image manipulation

## Installation
To use the Mosaic Maker, you'll need to have Python and the Pillow, requests, and BeautifulSoup libraries installed on your machine. Here's how to install them:

**Download and install Python** from the Python website. Make sure to install version 3.x or higher.
Install the Pillow, requests, and BeautifulSoup libraries by running the following command in your terminal:

~~~
pip install pillow

~~~

## Usage
To create a mosaic image, simply run the main.py script and enter the path to the source JPEG and the Instagram username when prompted.
~~~
create_mosaic('target.jpg', 'source_folder', 50)
~~~
The program will create a new image called mosaic.jpg in the current directory.


