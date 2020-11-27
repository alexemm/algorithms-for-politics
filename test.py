from majority_digraph import MajorityDigraph
from utils import read_file


def test():
    file_name = 'profiles/profiles.json'
    profile = read_file(file_name)
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


test()
