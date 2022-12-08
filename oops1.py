import sys


class details:
    def user_id(self,user_id):
        print("please enter user_id--",user_id)
        return user_id
    def password(self,password):
        print("please enter password-",password)
        return password

    def dob(self):
        dob=input("please enter date of birth--")
        return dob
krishna= details()
tirupati=details()
venkatesh=details()
krishna.user_id(123654)
try:
    print(len(krishna))
except Exception as k:
    print(k)

print(krishna.user_id("kittybiradar123@gmail.com"))
print(krishna.password(123456789))
krishna.password(987456321)
print(krishna.dob())
print(sys.getsizeof(venkatesh))




