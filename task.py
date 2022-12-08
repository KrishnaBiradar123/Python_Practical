import logging
logging.basicConfig(filename="task.log",level=logging.DEBUG,format= '%(asctime)s %(levelname)s : %(message)s' )
#logging.info("this is just information")
#logging.error("here an error occured")
#logging.warning("this is warning not use headphones")
#logging.debug("i have to debug this code")
#logging.critical("it's a critical situation")

def divide():
    try:
        a=int(input("enter initial number-"))
        b=int(input("enter final number-"))

        if b==0:raise ZeroDivisionError("#entered value should not be zero")
        logging.info("the entered values are %s and %s",a,b)
        logging.info(a / b)
        logging.info("operation successed")
    except Exception as e:
        logging.error(e)
divide()

