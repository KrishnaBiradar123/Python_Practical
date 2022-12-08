from flask import Flask,request,jsonify
import mysql.connector as conn
mydb=conn.connect(host='localhost',user='root',passwd="Tirupati@123")
cursor=mydb.cursor()
app=Flask(__name__)
@app.route('/get',methods=['POST','GET'] )
def test():
    name=request.args.get("name")

@app.route('/fetch', methods=['GET'])
def fetch():
    if (request.method == 'GET'):
        database=request.args.get('database'),
        connection1=request.args.get('connection')
        cursor.execute("select * from sai.ram")
        l = []
        for i in cursor.fetchall():
            l.append(i)
        return jsonify("successfully fetched ",l)

    return "this is my first python code for get {}".format(name)
if __name__=='__main__':
    app.run(port=5002)



