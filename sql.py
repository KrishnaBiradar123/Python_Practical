import mysql.connector as conn
mydb=conn.connect(host="localhost",user="root",passwd="Tirupati@123")
print(mydb)
cursor=mydb.cursor()

s="create table krishna.krishnadeatails(student_name varchar(30),student_id int(10),student_fees int(6),pate_no int(10))"
#cursor.execute(s)

#q1=cursor.execute(s)
#q2=cursor.execute("select * from krishna.krishnadeatails")
#print(q2)
k="""insert into  krishna.krishnadeatails values ("krishna",8025,2500,886155698)"""

cursor.execute(k)
mydb.commit()
#cursor.execute("select * from krishna.krishnadeatails")
print(cursor.fetchall())
for i in cursor.fetchall():
    print(i)
print(type(cursor.fetchall()))


"item_name":"kgf","item_code":542,"item_company":"mass","item_price":224,"item_type":"commercial"





