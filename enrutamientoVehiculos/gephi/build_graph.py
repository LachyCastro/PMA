from node import NodeNeigh, NodeSolution, Node_
import networkx as nx
from typing import List
import os
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt


def convert_query_to_node(query):
    G = nx.Graph()
    G.add_node(query)
    G.name = "Main node."
    return G


def grow_main_node(main_node: nx.Graph, types):
    main_node.add_nodes_from(types)
    first_node = main_node.nodes().keys().__iter__()
    f = first_node.__next__()
    for t in types:
        main_node.add_edge(f, t)
    return main_node


def grow_types_node(main_node: nx.Graph,  type_title, ranks):
    # for tt in type_title:
    #     if tt[0] == node.value:
    #         main_node.add_edge(graph, NodeNeigh(tt[1], tt[0]))
    # return graph
    nodes = []
    for n in main_node.nodes():
        nodes.append(n)
    for n in nodes:
        for i, t in enumerate(type_title):
            if isinstance(n, Node_):
                if n.type == t[0]:
                    temp = NodeNeigh(t[1], t[0], ranks[i])
                    print(temp.rank)
                    main_node.add_node(temp)
                    main_node.add_edge(n, temp)

    return main_node


def build_graph_type(type):
    graphs = []
    for t in type:
        temp = NodeSolution(t)
        graphs.append(temp)
    return graphs


def get_types(type_title):
    my_types = []
    for x in type_title:
        my_types.append(x[0])
    result = set(my_types)
    return result


def build_graph(query, rank: List):
    main_node = convert_query_to_node(query)
    ranking = rank
    type_title = []
    ranks = []
    for i, r in enumerate(ranking):
        type, title = get_title_and_type_from_path(r[0])
        type_title.append((type, title))
        ranks.append(r[1])
    node_types = get_types(type_title)
    graphs_types = build_graph_type(node_types)
    # print(graphs_types)
    grow_main_node(main_node, graphs_types)
    # print(main_node.nodes())

    # m_nodes = []
    # for n in main_node.nodes():
    #     m_nodes.append(n)
    # for g in m_nodes:
    #     grow_types_node(main_node, g, type_title)
    grow_types_node(main_node, type_title, ranks)
    # nx.draw(main_node, with_labels=True, font_weight='bold')
    # plt.figure(figsize=(50, 50))
    fig, ax = plt.subplots(figsize=(12, 12))
    node_size = []
    for i, node in enumerate(main_node):
        if isinstance(node, NodeNeigh):
            node_size.append(50 * node.rank)
        else:
            node_size.append(50)
    pos = nx.kamada_kawai_layout(main_node)
    label_options = {"ec": "k", "fc": "white", "alpha": 0.7}
    nx.draw_networkx_nodes(main_node, pos, node_size=node_size,
                           node_color="#3399FF", alpha=0.9)
    nx.draw_networkx_edges(main_node, pos, alpha=0.3,
                           width=1.0, edge_color="b")
    nx.draw_networkx_labels(main_node, pos, font_size=14, bbox=label_options)
    # nx.draw_networkx_edge()
    ax.set_title("Relation Quey-Document")
    ax.margins(0.1, 0.05)
    fig.tight_layout()
    plt.axis("off")
    plt.show()
    plt.savefig("foo.png")
    return main_node


def get_title_and_type_from_path(path: str):
    splitted_path = path.split("/")
    splited_path_ = splitted_path[len(splitted_path) - 1].split("\\")
    title = splited_path_[len(splited_path_) - 1]
    type = splited_path_[len(splited_path_) - 2]
    return (type, title)

# <temp>


def load_corpus(path):
    text = []
    dict_doc_path = {}
    # por ahora el metodo solo devolvera la lista de los documentos leidos
    if os.path.isdir(path):
        doc = 0
        for root, dirs, files in os.walk(path):
            for filename in files:
                with open(os.path.join(root, filename), encoding='utf8', errors='ignore') as f:
                    dict_doc_path[doc] = os.path.join(root, filename)
                    doc += 1
                    text.append(f.read())
    else:
        print("La direccion no es correcta")

    return dict_doc_path


def read_pdf(path):
    temp = open(path, 'rb')
    PDF_read = PdfReader(temp)
    text = ''
    for x in range(PDF_read.getNumPages()):
        first_page = PDF_read.getPage(x).extract_text() + " "
        text += first_page
    return text

# </temp>


# paths = load_corpus(
#     "C:/Users/acer/Downloads/Telegram Desktop/SRI/corpus")

# result = []
# for i, path in enumerate(paths.values()):
#     result.append((path, i))
#     if i == 20:
#         break

# result.sort(key=lambda x: x[1], reverse=True)

# a = build_graph("heuristic", result)
# nx.write_gexf(a, "C:/Users/acer/Downloads/vsc/g1.GEXF")
