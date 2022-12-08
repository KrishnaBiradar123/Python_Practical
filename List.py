import logging
logging.basicConfig(filename="List.log",level=logging.INFO,format="%(levelname)s %(name)s %(message)s %(asctime)s")
class list:
    def __int__(self,l):
        self.l=l
k=list(l)
#1.Try to reverse a list.
def revers(self):
        '''-- reversing list--'''
try:
        logging.info("|reversing operation initiated|")
        logging.info(self.l[::-1])
        ogging.info("|reversing operation has done successfully|")
    except Exception as e:
        logging.error(e)

    #2.try to access 234 out of this list
    def extract(self):
        '''-- extracting element from list--'''
        try:
            logging.info("|extraction operation initiated|")
            for i in self.l:
                if type(i)==int:
                    for j in i:
                        if j=="234":
                          logging.info(j)
                          logging.info("|extraction operation has done successfully|")
        except Exception as e:
            logging.error(e)








l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6), {"key1": "sudh",
    234:[23,45,656]}]
s=list()

