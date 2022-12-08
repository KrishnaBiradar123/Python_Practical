from flask import Flask,request,jsonify
import pymongo

client = pymongo.MongoClient("mongodb+srv://mongodb123:mongodb111@cluster1.zaqg5iw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database=client['mongodb2']
collection=database['test1']
app=Flask(__name__)
data={
            "ite_name": "krishna",
            "item_code":14566,
            "item_company": "biradar",
            "item_price": 542
        }
@app.route('/insert',methods=['POST','GET'])
def insert():
    if(request.method=='POST'):
        data={
            "ite_name": "krishna",
            "item_code":14566,
            "item_company": "biradar",
            "item_price": 542
        }
        collection.insert_one(data)
        return "inserted successfully"



@app.route('/update',methods=['POST','GET'])
def update():
    if(request.method=='POST'):
        ite_name=request.json['ite_name'],
        item_code=request.json['item_code'],
        item_company=request.json['item_company'],
        item_price=request.json['item_price']
        collection.update_many({'ite_name':'krishna','item_code':14566,'item_company':'biradar','item_price':542},{'$set':{'ite_name':'etetet','item_code':8884,'item_company':'fhfhfd','item_price':548}})
    return (str("successfully updated"))

@app.route('/delete',methods=['POST','GET'])
def delete():
    if(request.method=='POST'):
        collection.delete_one({'item_price':542})
        return jsonify(str("successfully deleted"))

@app.route('/find',methods=['POST','GET'])
def find():
    if(request.method=='POST'):
        collection.find()
        for i in collection.find():
            return jsonify(str("successfully fetched"),str(i))







if __name__=='__main__':
    app.run(port=5001)

