from typing import Optional, List, Dict, Set

from itertools import product


class Edge:

    def __init__(self, source: str, destination: str, weight: Optional[int] = None):
        self.source: str = source
        self.dest: str = destination
        self.weight: Optional[str] = weight


class Edges:

    def __init__(self, edges: List[Edge]):
        self.edges: List[Edge] = edges


def determine_alternatives(profile: Dict[str, List[str]]) -> Set[str]:
    """

    :param profile:
    :return:
    """
    ret_set = set()
    for _, ballot in profile.items():
        for alternative in ballot:
            ret_set.add(alternative)
    return ret_set


def get_edge_tuples(alternatives: Set[str]):
    """
    Source
    https://stackoverflow.com/questions/48186012/how-to-remove-mirrors-reflections-values-of-itertools-product-function
    :param alternatives:
    :return:
    """
    return (list(i) for i in product(alternatives, repeat=2)
            if tuple(reversed(i)) >= tuple(i) and i[0] != i[1])


def plot_majority_digraph(profile: List[str], weighted: bool = False, save_loc: str = ''):
    pass
