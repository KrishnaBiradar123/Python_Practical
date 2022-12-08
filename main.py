import logging
logging.basicConfig(filename="timespam.log",level=logging.DEBUG,format="%(asctime)s %(message)s %(levelname)s")
def divide(a,b,c):
    logging.info("user entered data is %s,%s and %s ",a,b,c)
    return a+b+c
print(divide(2,4,7))

def face(a,b):
    logging.info("user has entered this data %s and %s",a,b)
    try:
        logging.info("we are into the function")
        k=a/b
        logging.info("we have completed the operation")
        logging.info("result of the code is %s",k)
        return k
    except Exception as e:
     logging.exception(e)
print(face(14,0))
