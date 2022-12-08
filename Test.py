import pymongo

client = pymongo.MongoClient("mongodb+srv://mongodb1:mongodb123@cluster0.6cnfqmj.mongodb.net/?retryWrites=true&w=majority")
db = client.test



data={
    "name":"krishna",
    "mail_id":"kittybiradar123@gmail.com",
    "subject":["data science","data analytics","big data"]
}
database=["myinfo"]
collection=client['krishna']
collection.insert_one[data]

collection.client['tirupati']
collection.insert_one[data]