import requests
from time import sleep

from db import write_entry
from vars import auth, ip_addr


def vshift_inc(x):
    return(f'{vshift_inc.__name__} - {x}')


def vshift_dec(x):
    return(f'{vshift_inc.__name__} - {x}')


def zoom_inc(x):
    return(f'{zoom_inc.__name__} - {x}')


def zoom_dec(x):
    return(f'{zoom_dec.__name__} - {x}')


def backwall():
    z = zoom_dec(75)
    s = vshift_dec(100)
    write_entry(backwall.__name__)
    print(f'{z}\n{s}')
    sleep(2)


def screen():
    s = vshift_inc(100)
    z = zoom_inc(75)
    write_entry(screen.__name__)
    print(f'{z}\n{s}')
    sleep(2)
