from typing import Optional, List, Dict, Set, Tuple
from itertools import product


class Edge:

    def __init__(self, source: str, destination: str, weight: Optional[int] = None):
        self.source: str = source
        self.dest: str = destination
        self.weight: Optional[str] = weight


class Edges:

    def __init__(self, edges: List[Edge]):
        # TODO: maybe list of tuples?
        self.edges: List[Edge] = edges

    def add_weight(self, source: str, dest: str):
        pass


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
    # return (list(i) for i in product(alternatives, repeat=2)
    #        if tuple(reversed(i)) >= tuple(i) and i[0] != i[1])
    return (list(i) for i in product(alternatives, repeat=2) if i[0] != i[1])


def create_majority_digraph(profile: Dict[str, List[str]]) -> Edges:
    # TODO: finish dis
    alternatives: Set[str] = determine_alternatives(profile)
    edge_list: List[str] = get_edge_tuples(alternatives)
    edges: Edges = Edges(edge_list)
    for voter, ballot in profile.items():
        print("Voter: "+voter)
        for winner, loser in generate_duels(ballot):
            print(winner + " wins against " + loser)
            edges.add_weight(winner, loser)
        print()
    return edges


def generate_duels(ballot: List[str]):
    """

    :param ballot:
    :return: The winner and the loser as a tuple
    """
    for index, winner in enumerate(ballot):
        if index < len(ballot):
            for loser in ballot[index + 1:]:
                yield winner, loser


def plot_majority_digraph(profile: List[str], weighted: bool = False, save_loc: str = ''):
    pass
