from json import load


def read_json(file_name):
    ret = None
    with open(file_name) as f:
        ret = load(f)
    return ret


def read_txt(file_name):
    with open(file_name) as f:
        ret = f.read().splitlines()
    return ret


def read_and_parse_text(file_name: str):
    text = read_txt(file_name)
    return {linesplit[0]: linesplit[1:] for line in text if (linesplit := line.split(" "))}
