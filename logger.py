import logging
import os
os.chdir(os.path.dirname(__file__))


logging.basicConfig(
    level=logging.INFO,
    filename='phonebook.log',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)
