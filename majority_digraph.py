from typing import Optional, List, Dict, Set, Tuple
from itertools import product
from networkx import DiGraph, spring_layout, draw_networkx, get_edge_attributes, draw_networkx_edge_labels

import matplotlib.pyplot as plt


class Edge:

    def __init__(self, source: str, destination: str, weight: Optional[int] = None):
        self.source: str = source
        self.dest: str = destination
        self.weight: Optional[int] = weight

    def add_weight(self, n: int):
        if self.weight is not None:
            self.weight += n

    def __eq__(self, other):
        return self.source == other.source and self.dest == other.dest

    def __hash__(self):
        return hash((self.source, self.dest))


class Edges:

    def __init__(self, edges: List[Tuple[str, str]]):
        self.edges: Set[Edge] = set([Edge(src, dest, 0) for src, dest in edges])

    def add_weight(self, source: str, dest: str):
        self[(source, dest)].add_weight(1)
        self[(dest, source)].add_weight(-1)

    def __getitem__(self, key: Tuple[str, str]) -> Optional[Edge]:
        if not isinstance(key, tuple):
            raise TypeError("Your key is not a tuple")
        if len(key) != 2:
            raise TypeError("Your key is not a tuple of a source and destination")
        src, dest = key
        for edge in self.edges:
            if edge.source == src and edge.dest == dest:
                return edge
        raise KeyError("Your key does not exist in this container")

    def __len__(self):
        return len(self.edges)


class MajorityDigraph:

    def __init__(self, profile: Dict[str, List[str]]):
        self.alternatives, self.edges = create_majority_digraph(profile)
        self.edges = [edge for edge in self.edges.edges if edge.weight > 0]

    def plot(self, weighted: bool = False, save_file: str = ""):
        g: DiGraph = DiGraph()
        for edge in self.edges:
            if weighted:
                g.add_edge(edge.source, edge.dest, weight=edge.weight)
            else:
                g.add_edge(edge.source, edge.dest, weight=None)
        pos = spring_layout(g)
        draw_networkx(g, pos, node_color='w')
        if weighted:
            labels = get_edge_attributes(g, 'weight')
            draw_networkx_edge_labels(g, pos, edge_labels=labels)
        plt.axis("off")
        if save_file != "":
            plt.savefig(save_file)
        plt.show()


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
    return (tuple(i) for i in product(alternatives, repeat=2) if i[0] != i[1])


def create_majority_digraph(profile: Dict[str, List[str]]) -> Tuple[Set[str], Edges]:
    # TODO: finish dis
    alternatives: Set[str] = determine_alternatives(profile)
    edge_list: List[Tuple[str, str]] = list(get_edge_tuples(alternatives))

    edges: Edges = Edges(edge_list)
    for voter, ballot in profile.items():
        #print("Voter: "+voter)
        for winner, loser in generate_duels(ballot):
            #print(winner + " wins against " + loser)
            edges.add_weight(winner, loser)
        #print()
    return alternatives, edges


def generate_duels(ballot: List[str]):
    """

    :param ballot:
    :return: The winner and the loser as a tuple
    """
    for index, winner in enumerate(ballot):
        if index < len(ballot):
            for loser in ballot[index + 1:]:
                yield winner, loser


def plot_majority_digraph(profile: Dict[str, List[str]], weighted: bool = False, save_loc: str = ''):
    mj = MajorityDigraph(profile)
    mj.plot(weighted, save_loc)
