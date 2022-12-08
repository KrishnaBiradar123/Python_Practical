import os
os.remove("kgf")


class person:


    def __init__(self,name1,surname,emailid,year_of_brth):
        self.name= name1
        self.surname = surname
        self.emailid = emailid
        self.year_of_brth = year_of_brth

    def age (self,current_year):
        return current_year - self.year_of_brth
a=person("fjfguju","mcvhny","fgkuvjbujb",544)
b=person("fjfguju","mcvhny","fgkub",54)
c=person("vvvv","vvvv","vvvv",545)
print(sys.getsizeof(c))
print(a.name,a.year_of_birth,a.emailid,a.surname)
print(b.name,b.year_of_birth,b.surname,b.emailid)

krish_var = person("krishna","biradar","kittybiradar123@gmail.com","2000")
print(krish_var.age(2022))
print(krish_var.name)
print(krish_var.surname)
print(krish_var.emailid)
print(krish_var.year_of_birth)

tirupati = person("tirupati","biradar","tirupati@gmail.com","2004")
print(len(tirupati))
print(tirupati.name)
print(tirupati.surname)
print(tirupati.emailid)
print(tirupati.year_of_birth)
print(type(tirupati))
try:
    pprint(type(krish_var))
except Exception as e:
    print(e)
print(tirupati.age(2022))

print(person())