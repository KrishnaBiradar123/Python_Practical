import mysql.connector as conn
mydb=conn.connect(host="localhost",user="root",passwd="Tirupati@123")
print(mydb)
cursor=mydb.cursor()
#cursor.execute("create database tirupati")
#cursor.fetchall()
a="create table tirupati.biradar(item_name varchar(10), item_code int(10),item_company varchar(20),item_price int(4),item_type varchar(25))"
#cursor.execute(a)
#b=cursor.execute("select * from tirupati.biradar")
#print(b)
h="insert into tirupati.biradar values('coocking',256485,'forchune500',125,'vegetable oil')"
c="insert into tirupati.biradar values('wheel soap',256368,'hollywood',5,'detergent')"
cursor.execute(h)
cursor.execute(c)
mydb.commit()
q=cursor.execute("select * from tirupati.biradar")
print(cursor.fetchall())


def update():
    if(request.method=='POST'):
        item_name=request.json['item_name']
        item_code=request.json['item_code']
        item_company=request.json['item_company']
        item_price= request.json['item_price']
        item_type=request.json['item_type']
        cursor.execute("insert into sai.ram values(%s %s %s %s %s)",(item_name,item_code,item_company,item_price,item_type))
        mydb.commit()
        return jsonify(str("the above values are successfully inserted"))



def insert()