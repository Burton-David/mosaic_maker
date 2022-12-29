import requests
import os
from bs4 import BeautifulSoup


def download_images(username):
  # Make a request to the Instagram user's page
  response = requests.get(f'https://www.instagram.com/{username}/')

  # Parse the HTML of the page
  soup = BeautifulSoup(response.text, 'html.parser')

  # Find all the `img` tags
  img_tags = soup.find_all('img')

  # Create a directory to store the images
  if not os.path.exists(username):
    os.makedirs(username)

  # Iterate over the `img` tags
  for img_tag in img_tags:
    # Get the image URL
    img_url = img_tag['src']

    # Download the image
    response = requests.get(img_url)
    open(f'{username}/{img_url.split("/")[-1]}', 'wb').write(response.content)


# Example usage
download_images('instagram_username')
