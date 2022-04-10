import requests
import logging
from time import sleep

from db import write_entry
from vars import auth, ip_addr


def power_on():
    url = f'{ip_addr}/cgi-bin/power_ctl.cgi?key=pow_on&lang=e'
#    requests.get(url, auth=auth)
    print('power on')

def power_off():
    url = f'{ip_addr}/cgi-bin/power_ctl.cgi?key=pow_off&lang=e'
#    requests.get(url, auth=auth)
    print('power off')


def shutter_open():
    url = f'{ip_addr}/cgi-bin/power_ctl.cgi?key=shutter_off&lang=e'
#    requests.get(url, auth=auth)
    print('shutter open')


def shutter_close():
    url = f'{ip_addr}/cgi-bin/power_ctl.cgi?key=shutter_on&lang=e'
#    requests.get(url, auth=auth)
    print('shutter close')


def vshift_inc(x):
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_vshift_inc1&lang=e'
#    for i in range(x):
#       requests.get(url, auth=auth)
#       sleep(.05)
    print('up')


def vshift_dec(x):
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_vshift_dec1&lang=e'
#    for i in range(x):
#       requests.get(url, auth=auth)
#        sleep(.05)
    print('down')

def zoom_inc(x):
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_zoom_inc1&lang=e'
#    for i in range(x):
#        requests.get(url, auth=auth)
#        sleep(.05)
    print('left')

def zoom_dec(x):
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_zoom_dec1&lang=e'
#    for u in range(x):
#        requests.get(url, auth=auth)
#        sleep(.05)
    print('right')

def backwall():
    print('backwall')
#    zoom_dec(75)
#    vshift_dec(100)
    write_entry(backwall.__name__)


def screen():
    print('screen')
#    vshift_inc(100)
#    zoom_inc(75)
    write_entry(screen.__name__)
