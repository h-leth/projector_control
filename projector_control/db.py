import json

db = 'db.json'


def write_entry(x):
    with open(db, 'w+') as file:
        json.dump(x, file, indent=4)


def read_entry():
    try:
        with open(db, 'r') as file:
            entry = json.load(file)
        return entry
    except FileNotFoundError:
        pass
