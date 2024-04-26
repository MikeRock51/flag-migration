#!/usr/bin/env python3

from os import getenv
from dotenv import load_dotenv
import pymongo

load_dotenv()

DB = getenv('DB_PROD')


client = pymongo.MongoClient(DB)
db = client[getenv('DATABASE')]
collection = db["players"]
cursor = collection.find()

transfer1 = cursor[2]['transfers']['transfer'][0]
collection.update_one({"transfers.transfer": transfer1}, {'$set': {'transfers.transfer.$.type': transfer1['type'].replace('&euro; ', '')}})
print('Updated Successfully')
    
        # if '&euro;' in transfer['type']:
        #     print(player)
        #     print(transfer['type'].replace('&euro; ', ''))

# for doc in cursor:
#     try:
#         if doc['transfers'] is not None:
#             player = doc['common_name']
#             transfers = doc['transfers']['transfer']
#             for transfer in transfers:
#                 if '&euro;' in transfer['type']:
#                     print(player)
#                     print(transfer['type'].replace('&euro; ', ''))
#     except Exception:
#         print(Exception)
