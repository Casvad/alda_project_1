import json

memory_files = {}


def open_json_file(filename):
    if filename in memory_files:
        return memory_files[filename]

    with open(filename, "r") as file:
        return json.load(file)


def open_csv_file(filename, separator=","):
    if filename in memory_files:
        return memory_files[filename]
    with open(filename, "r") as file:
        return [x.split(separator) for x in file.read().split("\n")]
