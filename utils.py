from json import load


def read_file(file_name):
    ret = None
    with open(file_name) as f:
        ret = load(f)
    return ret
