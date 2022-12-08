class person:
    def __init__(self,name,surname,yob):
        self.__name1=name
        self._surname1=surname
        self.yob1=yob
variable=person("krishna","biradar",2000)
print(variable.yob1)
print(variable._surname1)
try:
    print(variable.__name1)
except Exception as e:
    print(e)
print(variable._person__name1)
