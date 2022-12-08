from flask import Flask,request,jsonify
import mysql.connector as conn
mydb=conn.connect(host='localhost',user='root',passwd='Tirupati@123')
cursor=mydb.cursor()
#cursor.execute("create database sai")
#cursor.fetchall()
a=("create table sai.ram(item_name varchar(10),item_code int(10),item_company varchar(20),item_price int(4),item_type varchar(25))")
#cursor.execute(a)

app=Flask(__name__)
@app.route('/insert',methods=['POST','GET'])
def insert():
    if(request.method=='POST'):
        item_name=request.json['item_name']
        item_code=request.json['item_code']
        item_company=request.json['item_company']
        item_price= request.json['item_price']
        item_type=request.json['item_type']
        cursor.execute("insert into sai.ram values(%s,%s, %s, %s,%s)",(item_name,item_code,item_company,item_price,item_type))
        mydb.commit()
        return jsonify(str("the above values are successfully inserted"))
@app.route('/update',methods=['POST','GET'])
def update():
    if(request.method=='POST'):
        item_name=request.json['item_name']
        cursor.execute("update sai.ram set item_code=12345678,item_price=55,item_company='krishna_ltd' where item_name= %s",(item_name,))
        mydb.commit()
        return jsonify(str("the above values are successfully updated"))

@app.route('/delete',methods=['POST','GET'])
def delete():
    if(request.method=='POST'):
        user=request.json['mysql']
        cursor.execute("delete from sai.ram where item_code=%s",(user,))
        mydb.commit()
        return jsonify(str("successfully deleted"))
@app.route('/fetch',methods=['POST','GET'])
def fetch():
    if(request.method=='POST'):
        cursor.execute("select * from sai.ram")
        l=[]
        for i in cursor.fetchall():
            l.append(i)
        return jsonify("successfully fetched",l)






if __name__=='__main__':
    app.run()
