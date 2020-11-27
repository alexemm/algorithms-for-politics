from majority_digraph import MajorityDigraph
from utils import read_json, read_and_parse_text


def test_json():
    file_name = 'profiles/json/profile0.json'
    profile = read_json(file_name)
    # print(profile)
    # alternatives = determine_alternatives(profile)
    # print(alternatives)
    # edges = get_edge_tuples(alternatives)
    # print(list(edges))
    save_file = "plots/0.png"
    save_file_weighted = "plots/1.png"
    mj = MajorityDigraph(profile)
    mj.plot(False, save_file)
    mj.plot(True, save_file_weighted)


def test_txt():
    file_name = 'profiles/txt/profile1.txt'
    profile = read_and_parse_text(file_name)
    save_file = "plots/0.png"
    save_file_weighted = "plots/1.png"
    mj = MajorityDigraph(profile)
    mj.plot(False, save_file)
    mj.plot(True, save_file_weighted)


test_json()
#test_txt()
