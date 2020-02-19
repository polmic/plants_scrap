from google_images_download import google_images_download   #importing the library
import requests
import os
from os import listdir
from os.path import isfile, join

api_description_endpoint = "http://localhost:4000/plant-description/"
api_thumbnail_endpoint = "http://localhost:4000/plant-thumbnail/"
download_folder_path = "D:/workspace/test/google-images-download/downloads"

gim = google_images_download.googleimagesdownload()   #class instantiation

r = requests.get(api_description_endpoint)
descriptions = (r.json())

for description in descriptions:
    commonName = description['commonName']
    arguments = {
        "keywords": commonName,
        "limit": 10,
        "print_urls": True,
        "usage_rights": "labeled-for-reuse"
    }
    print(arguments)
    paths = gim.download(arguments)
    print(paths)

    images_folder_path = download_folder_path + "/" + commonName

    i = 0
      
    for filename in listdir(images_folder_path):
        dst =str(i) + ".png"
        src =images_folder_path + filename 
        dst =images_folder_path + dst 
          
        os.rename(src, dst) 
        i += 1

    images = [f for f in listdir(images_folder_path) if isfile(join(images_folder_path, f))]

    for image in images:
        print('-- - - - ')
        print(image)
        data = open(image, 'rb').read()
        res = requests.post(
            url=api_thumbnail_endpoint,
            data=data,
            headers={'Content-Type': 'application/octet-stream'}
        )
