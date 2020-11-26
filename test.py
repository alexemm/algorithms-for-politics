from majority_digraph import get_edge_tuples, determine_alternatives, create_majority_digraph
from utils import read_file


def test():
    file_name = 'profiles.json'
    profile = read_file(file_name)
    print(profile)
    alternatives = determine_alternatives(profile)
    print(alternatives)
    edges = get_edge_tuples(alternatives)
    print(list(edges))
    create_majority_digraph(profile)


test()
