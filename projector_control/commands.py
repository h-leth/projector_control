import requests
from time import sleep

from db import write_entry
from vars import auth, ip_addr


def vshift_inc(x):
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_vshift_inc1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def vshift_dec(x):
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_vshift_dec1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def zoom_inc(x):
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_zoom_inc1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def zoom_dec(x):
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_zoom_dec1&lang=e'
    for u in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def backwall():
    zoom_dec(75)
    vshift_dec(100)
    write_entry(backwall.__name__)


def screen():
    vshift_inc(100)
    zoom_inc(75)
    write_entry(screen.__name__)
