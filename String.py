import logging
logging.basicConfig(filename="String.log",level=logging.DEBUG,format="%(asctime)s:%(levelname)s:%(message)s")
class string_task:

    s= "this is My First Python programming class and i am learNING python string and its function"
    # 1.Try to extract data from index one to index 300 with jump of 3?
    def jump(self,a,b,c):
        '''---slicing operation with jump'''
        a=int(input("enter 'a' value-"))
        b=int(input("enter 'b' value-"))
        c=int(input("enter 'c' value-"))
        try:
            logging.info("|slicing operation has initiated|")
            logging.info("entered 'a','b' & 'c' value--%s : %s: %s",a,b,c)
            logging.info(self.s[a:b:c])
            logging.info("|slicing operation has done successfully|")
        except Exception as e:
            logging.error(e)

    #2.Try to reverse a string without using reverse function?
    def reverse(self):
        '''---reversing operation without using reserve function'''
        try:
            logging.info("|reversing operation initiated|")
            logging.info(self.s[::-1])
            logging.info("|reversing operation has done successfully|")
        except Exception as e:
            logging.error(e)
    #3.Try to split a string after conversion of entire string in uppercase?
    def split_upper(self):
        '''---first try to split and then convert it to uppercase---'''
        try:
            logging.info("|splitting & uppercase operation has initiated|")
            logging.info(self.s.split())
            logging.info(self.s.upper())
            logging.info("|splitting & uppercase operation has done successfully|")
        except Exception as e:
            logging.error(e)
    #4.Try to convert the whole string into lowercase.
    def lowercase(self):
        '''---convert it to lowercase---'''
        try:
            logging.info("|lowercase operation has initiated|")
            logging.info(self.s.lower())
            logging.info("|lowercase operation has done successfully|")
        except Exception as e:
            logging.error(e)
    #5.Try to capitalize the whole string.
    def capitalize(self):
        '''--capitalization--'''
        try:
            logging.info("|capitalize operation has initiated|")
            logging.info(self.s.capitalize())
            logging.info("|capitalize operation has done successfully|")
        except Exception as e:
            logging.error(e)
    #7.Try to give an example of expand tab.
    k = "this is My Fi\trst Python progra\tmming cl\tass and i am lear\tNING python st\tring and its f\tunction"
    def expand_tab(self):
        '''-- Example for Expand tab operation--'''
        try:
            logging.info("|expand tab operation has initiated|")
            logging.info(self.k.expandtabs())
            logging.info("|expand tab operation has done successfully|")
        except Exception as e:
            logging.error(e)
    #8.Give example of strip, lstrip and rstrip.
    m="  function  "
    def strip(self):
        '''-- Example for strip, lstrip, rstrip--'''
        try:
            logging.info("|strip, lstrip & rstrip operation has initiated|")
            logging.info("%s:%s:%s",self.m.strip(),self.m.lstrip(),self.m.rstrip())
            logging.info("|strip, lstrip & rstrip operation has done successfully|")
        except Exception as e:
            logging.error(e)
    #9.Replace a string character by another character taking your own example.
    def replace(self):
        '''-- replace operation--'''
        try:
            logging.info("|replace operation has initiated|")
            logging.info(self.m.replace("function","krishna"))
            logging.info("|replace operation has done successfully|")
        except Exception as e:
            logging.error(e)

    #11.Try give definition of string center with example.
    def center(self):
        '''-- center operation--'''
        try:
            logging.info("|center operation has initiated|")
            logging.info(self.m.center(30,"@"))
            logging.info("|center operation has done successfully|")
        except Exception as e:
            logging.error(e)















obj=string_task()
obj.jump("a",'b','c')
obj.reverse()
obj.split_upper()
obj.lowercase()
obj.capitalize()
obj.expand_tab()
obj.strip()
obj.replace()
print(obj.m)
obj.center()