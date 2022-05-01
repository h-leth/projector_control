import json

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
