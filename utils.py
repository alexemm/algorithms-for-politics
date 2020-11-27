from json import load


def read_json(file_name):
    ret = None
    with open(file_name) as f:
        ret = load(f)
        for voter, ballot in ret.items():
            for rank, alternatives in enumerate(ballot):
                if not isinstance(ret[voter][rank], list):
                    ret[voter][rank] = [ret[voter][rank]]
                ret[voter][rank] = set(ret[voter][rank])
    return ret


def read_txt(file_name):
    with open(file_name) as f:
        ret = f.read().splitlines()
    return ret


def read_and_parse_text(file_name: str):
    text = read_txt(file_name)
    return {line_split[0]: [set(rank.split(';')) for rank in line_split[1:]] for line in text
            if (line_split := line.split(" "))}
