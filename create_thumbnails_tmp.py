from google_images_download import google_images_download   #importing the library
import requests
import os
import base64
from os import listdir
from os.path import isfile, join

api_description_endpoint = "http://localhost:4000/plant-description/"
api_thumbnail_endpoint = "http://localhost:4000/plant-thumbnail/"
download_folder_path = "/home/pmicas/workspace/repositories/google-images-download/downloads"

gim = google_images_download.googleimagesdownload()   #class instantiation

r = requests.get(api_description_endpoint)
descriptions = (r.json())

for description in descriptions:
    commonName = description['commonName'].split(',')[0]
    arguments = {
        "keywords": commonName,
        "limit": 10,
        "print_urls": True,
        "usage_rights": "labeled-for-reuse"
    }
    print(arguments)
    paths = gim.download(arguments)

    images_folder_path = download_folder_path + "/" + commonName

    i = 0
      
    for filename in listdir(images_folder_path):
        extension = filename[-4:]
        dst = str(i) + extension
        src = images_folder_path + "/" + filename
        dst = images_folder_path + "/" + dst 
        os.rename(src, dst) 
        i += 1

    images = [f for f in listdir(images_folder_path) if isfile(join(images_folder_path, f))]

    print('__________________\n')
    print(images)
    print('__________________')

    for image in images:
        binary = base64.b64encode(open(images_folder_path + "/" +image, 'rb').read()).decode('ascii')
        res = requests.post(
            url=api_thumbnail_endpoint + "/" + description['_id'],
            data=binary,
            headers={'Content-Type': 'application/octet-stream'}
        )
        print(image + ' : ' + str(res.status_code))
