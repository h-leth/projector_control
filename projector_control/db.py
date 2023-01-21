import json
from requests.auth import HTTPDigestAuth

DB = 'db.json'


def write_entry(x):
    """Write entry to json file"""
    with open(DB, 'w+', encoding='utf-8') as file:
        json.dump(x, file, indent=4)


def read_entry():
    """Read entry for json file"""
    try:
        with open(DB, 'r', encoding='utf-8') as file:
            entry = json.load(file)
        return entry
    except FileNotFoundError:
        pass


def sleep_time():
    """Checks if a sleeptime is set"""
    if database.get('settings').get('sleeptime').get('custom') is not None:
        wait = database.get('settings').get('sleeptime').get('custom')
    else:
        wait = database.get('settings').get('sleeptime').get('default')
    return wait

database = read_entry()

ip_addr = database.get('login').get('adresse')

user = database.get('login').get('user')
password = database.get('login').get('password')
auth = HTTPDigestAuth(user, password)
