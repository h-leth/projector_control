from time import sleep
import requests

from db import write_entry
from vars import auth, ip_addr


def check_connection():
    """Check the connection to projector"""
    url = f'{ip_addr}/'
    try:
        requests.get(url, auth=auth, timeout=2)
    except requests.exceptions.ConnectTimeout:
        return False
    return True


def power_on():
    """Power on"""
    url = f'{ip_addr}/cgi-bin/power_on.cgi'
    requests.post(url, auth=auth)


def power_off():
    """Power off"""
    url = f'{ip_addr}/cgi-bin/power_off.cgi'
    requests.post(url, auth=auth)


def shutter_open():
    """Open shutter"""
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=shutter_off&lang=e&osd=on'
    requests.get(url, auth=auth)


def shutter_close():
    """Close shutter"""
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=shutter_on&lang=e&osd=one'
    requests.get(url, auth=auth)


def vshift_inc(x):
    """"Increments vertical shift"""
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_vshift_inc1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def vshift_dec(x):
    """Decrements vertical shift"""
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_vshift_dec1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def zoom_inc(x):
    """Increments zoom"""
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_zoom_inc1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def zoom_dec(x):
    """"Decrements zoom"""
    url = f'{ip_addr}/cgi-bin/proj_ctl.cgi?key=lens_zoom_dec1&lang=e'
    for i in range(x):
        requests.get(url, auth=auth)
        sleep(.05)


def backwall():
    """Preset to move image from screen to backwall"""
    zoom_dec(75)
    vshift_dec(100)
    write_entry(backwall.__name__)


def screen():
    """Preset to move image from backwall to screen"""
    vshift_inc(100)
    zoom_inc(75)
    write_entry(screen.__name__)
