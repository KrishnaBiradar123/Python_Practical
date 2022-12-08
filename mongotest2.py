import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb1:mongodb123@cluster0.6cnfqmj.mongodb.net/?retryWrites=true&w=majority")
db = client.test

dataa =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
database=client['inventory']
collection=database['infos']
#collection.insert_many(dataa)
#d=collection.find()
#d=collection.find({'status':{'$in':['A','p']}})
#for i in d:
    #print(i)
#c=collection.find({'status':{'$gt':'A'}})
#for i in c:
    #print(i)
#b=collection.find({'qty':{'$gte':75},'item':'sketch pad'})
#for i in b:
    #print(i)
#g=collection.find({'$or':[{'qty':{'$gte':75}},{'item':'sketch pad'}] })
#for i in g:
    #print(i)
#m=collection.update_many({'item':'paper','item':'notebook','item':'mousepad'},{'$set':{'item':'fuck'}})
#keyword= collection.find({"item":"fuck"})
#for i in keyword:
    #print(i)
s=collection.find()
for i in s:
    print(i)