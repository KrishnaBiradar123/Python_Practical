import mysql.connector as conn
mydb=conn.connect(host='localhost',user='root',passwd='Tirupati@123')
print(mydb)
cursor=mydb.cursor()
#cursor.execute('create database Dataset')
#cursor.execute("create table Dataset.attribute_data4 (Dress_ID varchar(100),Style varchar(30),Price varchar(30),Rating int(20),Size varchar(25),Season varchar(30),NeckLine varchar(30),SleeveLength varchar(30),waiseline varchar(30),Material varchar(30),FabricType varchar(30),Decoration int(25),Pattern_Type varchar(30),Recommendation int(5))")
a="create table Dataset.Dress_data (Dress_ID int(20),29_8_2013 int(20),31_8_2013 int(20),09_02_2013 int(20),09_04_2013 int(20),09_06_2013 int(20),09_08_2013 int(20),09_10_2013 int(20),09_12_2013 int(20),14_9_2013 int(20),16_9_2013 int(20),18_9_2013 int(20),20_9_2013 int(20),22_9_2013 int(20),24_9_2013 int(20),26_9_2013 int(20),28_9_2013 int(20),30_9_2013 int(20),10_02_2013 int(20),10_04_2013 int(20),10_06_2013 int(20),10_08_2010 int(20),10_10_2013 int(20),10_12_2013 int(20))"
#cursor.execute(a)
k="insert into "

#cursor.execute("drop table Dataset.Attribute_data")
cursor.execute("LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Attribute_2.csv' INTO TABLE Dataset.Attribute_data4 ")
#cursor.execute("SHOW VARIABLES LIKE'secure-file-priv'")
