from typing import List
import networkx as nx
from node import NodeNeigh
from node import NodeQuery
from ir_logic.load import load_corpus as lc


def convert_query_to_node(query):
    G = nx.Graph()
    node = NodeQuery(query)
    G.add_node(node)
    return G


def build_graph(query, rank: List[(str, float)]):
    main_node = convert_query_to_node(query)
    ranking = rank

    for i, r in enumerate(ranking):
        type, title = get_title_and_type_from_path(r[0])
        rank_value = ranking[i][1]
        main_node.add_node(NodeNeigh(title, type, rank_value))
    return main_node


def get_title_and_type_from_path(path: str):
    splitted_path = path.split("/")
    return (splitted_path[len(splitted_path) - 1], splitted_path[len(splitted_path) - 2])


paths = lc("C:/Users/acer/Downloads/Telegram Desktop/SRI/corpus/alt.atheism")
print("+++")
