import json


def load_raw_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
