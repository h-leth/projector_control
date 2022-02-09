import requests
from requests.auth import HTTPDigestAuth
from time import sleep

from vars import auth


def vshift_inc(x):
    url = 'http://10.0.20.6/cgi-bin/proj_ctl.cgi?key=lens_vshift_inc1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def vshift_dec(x):
    url = 'http://10.0.20.6/cgi-bin/proj_ctl.cgi?key=lens_vshift_dec1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def zoom_inc(x):
    url = 'http://10.0.20.6/cgi-bin/proj_ctl.cgi?key=lens_zoom_inc1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def zoom_dec(x):
    url = 'http://10.0.20.6/cgi-bin/proj_ctl.cgi?key=lens_zoom_dec1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def backwall():
    zoom_dec(75)
    vshift_dec(100)


def screen():
    vshift_inc(100)
    zoom_inc(75)
