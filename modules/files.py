import json


def json_load(file_path: str):
    with open(file_path, 'r') as file:
        content = json.load(file)
    return content
