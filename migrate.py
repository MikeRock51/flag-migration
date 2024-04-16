#!/usr/bin/env python3

from os import getenv
from dotenv import load_dotenv
import requests
import os
import pymongo

load_dotenv()

DB = getenv('DB_PROD')

def save_image_from_url(image_url, save_folder, image_name):
    # Create the save folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    try:
        # Get the image data from the URL
        response = requests.get(image_url)
        response.raise_for_status()

        # Determine the full path to save the image
        save_path = os.path.join(save_folder, image_name)

        # Save the image data to the specified path
        with open(save_path, 'wb') as f:
            f.write(response.content)

        print(f"Image saved successfully to {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")


client = pymongo.MongoClient(DB)
db = client[getenv('DATABASE')]
collection = db["countries"]
cursor = collection.find()

save_folder = "./images"

for doc in cursor:
    save_image_from_url(doc['image_path'], save_folder, f'{doc["name"].lower()}.png')

print("Mission accomplished!!")
