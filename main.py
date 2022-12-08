#INHERITANCE
class car:

    def __init__(self,bodycolour,engine,tyre):
        self.b=bodycolour
        self.e=engine
        self.t=tyre

    def model(self):
        print("this is the car model--")
c=car("red","b6","appollo")
print(c)
print(c.t,c.e,c.b)
class tata(car):
    pass
t=tata("white","b6","jktyre")
print(t)
print(t.t,t.b,t.e)
#Multi level__INHERITANCE
class bank:
    def credit(self):
        print("$2000 has been credited.")
    def debit(self):
        print("$1000 has been debited.")
    def awareness(self):
        print("be aware of fake messages, if any kind of messages regarding banking, put them to spam.")
class canara_bank(bank):
    def loan(self):
        print("education loan has been sanctioned successfully.")
    def pay_slip(self):
         print("your payslip for the month of AUG has been generated.")
class INFOSYS(canara_bank):
    def salary(self):
         print("salary for the month of AUG has been credited.")
#I=INFOSYS()
#I.loan()
#I.debit()
#I.credit()
#I.salary()
#I.pay_slip()
#I.awareness()
#Multiple INHERITANCE
class bank:
    def credit(self):
        print("$2000 has been credited.")
    def debit(self):
        print("$1000 has been debited.")
    def awareness(self):
        print("be aware of fake messages, if any kind of messages regarding banking, put them to spam.")
class canara_bank():
    def credit(self):
        print("-------------.")
    def pay_slip(self):
         print("your payslip for the month of AUG has been generated.")
class icici(bank,canara_bank):
    def salary(self):
         print("salary for the month of AUG has been credited.")
#k=icici()
#k.loan()
#k.debit()
#k.credit()
#k.salary()
#k.pay_slip()
#k.awareness()
#redifining method in child class
class school:
    def lower_primary(self):
        print("this is lower primary school")
    def primary(self):
        print("this is primary school")
    def higher_primary(self):
        print("this is higher primary school")

class collage:
    def ug(self):
        print("this is under graduate collage ")
    def pg(self):
         print("this is post graduate collage")
class institution(school,collage):
    def ug(self):
         print("this is the boys ug collage")

#i=institution()
#i.ug()

#ABSTRACTION:hidding data from user which is not directly accessed by him/her.
class staff:
    __teacher= "dr.n.b.prakash"
    def teaching_staff(self):
        print(self.__teacher)
#s=staff()
#s.teaching_staff()
#print(s._staff__teacher)


#ENCAPSULATION : not allowing user to modify the data directly but it could be modified by method/class function.
class ineuron:
    __course= "fullstack data science"
    def may_7th(self,):
        print(self.__course)
    def change(self,data):
        self.__course=data
        print(data)
#i=ineuron()
#i.change("big data engineering")

class ineuron1:
    course= "fullstack data science"
    def may_7th(self,):
        print(self.course)
    def change(self,data):
        self.__course=data
        print(data)
#i=ineuron1()
#i.course="data analytics"
#i.may_7th()

#POLYMORPHISM
class father:
    def son(self):
        print("he is my father")
class mother:
    def son(self):
        print("she is my motther")
def friend(i):
    i.son()
k=father()
m=mother()
friend(k)
friend(m)

