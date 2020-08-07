import pymongo

client = pymongo.MongoClient("mongodb://15.165.220.75:27017")

db = client.naver
collection = db.article
