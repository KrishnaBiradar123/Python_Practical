import logging
logging.basicConfig(filename="logging.log",level=logging.INFO)
logging.info("this is my first logging class.")
logging.warning("there is some restriction not to use this URL")
logging.error("//412 error occured")
l=[1,2,3,4,5,6,7,8]
for i in l:
    if i==5:
        logging.info(l)
        logging.warning("if i=2, then it harms to your system")
        logging.error('if i=2,//438 error occured')
logging.shutdown()
l=[1,2,3,4,5,6,7,8,8,9]
l1=[]
for i in l:
    l1.append(i)
print(l1)
logging.error("this is an error")
logging.shutdown()

import logging
logging.basicConfig(filename="timestamp.log",level=logging.DEBUG,format='%(asctime)s %(messege)s %(levelname)s')
logging.info("this is the format to import time in log file, at what time error occured, how it occured for all this this things")

