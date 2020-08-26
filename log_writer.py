import datetime
import logging
import os
import inspect


# change timezone To Berlin
os.environ['TZ'] = 'CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00'


def write_exception_error_log(msg=""):
    frm = inspect.stack()[1]

    date = datetime.date.today().strftime('%Y_%m_%d')
    FORMAT = '%(asctime)s (%(levelname)s) \n %(message)s'
    # FORMAT = '%(asctime)s %(message)s'
    logging.basicConfig(filename='logs/error/%s.log' %date, level=logging.ERROR, format=FORMAT, datefmt='%H:%M:%S')
    # logging.basicConfig(filename='logs/%s.log' %date, level=logging.DEBUG, format=FORMAT, datefmt='%H:%M:%S => ')
    # logging.basicConfig(filename='logs/%s.log' %date, level=logging.DEBUG, format=FORMAT, datefmt='%d.%m.%Y %H:%M:%S ')
    adjust_msg = "\tpath => %s \n\tline => %s \n\tmsg => %s\n" %(frm[1], frm[2], msg)
    logging.error(adjust_msg)

def write_exception_debug_log(msg=""):
    frm = inspect.stack()[1]
    date = datetime.date.today().strftime('%Y_%m_%d')
    FORMAT = '%(asctime)s %(levelname)s => %(message)s'
    logging.basicConfig(filename='logs/debug/%s.log' %date, level=logging.DEBUG, format=FORMAT, datefmt='%H:%M:%S')
    adjust_msg = "\tpath => %s \n\tline => %s \n\tmsg => %s\n" %(frm[1], frm[2], msg)
    logging.debug(adjust_msg)

def write_exception_warning_log(msg=""):
    frm = inspect.stack()[1]
    date = datetime.date.today().strftime('%Y_%m_%d')
    FORMAT = '%(asctime)s (%(levelname)s) \n %(message)s'
    logging.basicConfig(filename='logs/warning/%s.log' %date, level=logging.WARNING, format=FORMAT, datefmt='%H:%M:%S')
    adjust_msg = "\tpath => %s \n\tline => %s \n\tmsg => %s\n" %(frm[1], frm[2], msg)
    logging.warning(adjust_msg)