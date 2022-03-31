import PIL

from fetcher import fetch_image

IMAGE_URL = "https://media.discordapp.net/attachments/959138038888419458/959143909223710740/image.png?width=48&height=48"

if __name__ == "__main__":
    fetch_image(IMAGE_URL)
