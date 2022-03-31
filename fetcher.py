import requests

def fetch_image(url):
    filename = url.split("/")[-1]

    r = requests.get(url, stream = True)

    if r.status_code == 200:
        print('Successfully downloaded image from' + str(url))
        return r.raw
    else:
        print('Failed to download image...')
        return None
