#!/usr/bin/env python3

from os import getenv
from dotenv import load_dotenv
import pymongo
import re

load_dotenv()

DB = getenv('DB_PROD')


client = pymongo.MongoClient(DB)
db = client[getenv('TEST_DATABASE')]
collection = db["players"]

pattern = re.compile(r'&euro; ')
res = collection.find({'transfers.transfer.type': {'$regex': pattern}})

for doc in res:
    try:
        if doc['transfers'] is not None:
            transfers = doc['transfers']['transfer']
            for transfer in transfers:
                if '&euro;' in transfer['type']:
                    collection.update_one({"transfers.transfer": transfer}, {'$set': {
                                          'transfers.transfer.$.type': transfer['type'].replace('&euro; ', '')}})
    except Exception as e:
        print(e)

print("Misson Accomplished!!!")
