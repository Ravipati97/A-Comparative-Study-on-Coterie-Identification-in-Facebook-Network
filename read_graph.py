import networkx as nx
import os

def lst_graph_files(data_path):
    files = []
    rootdir = data_path
    for root, dirnames, filenames in os.walk(rootdir):
        for f in filenames:
            files.append(os.path.join(rootdir, f))
    return files

def read_graph(file_lst):
    ego_lst = {}
    graph = nx.Graph()
    for f in file_lst:
        if f.endswith('edges'):
            tmp_graph = nx.read_edgelist(f)
            ego_node = f.strip().split('/')[-1].split('.')[0]
            tmp_graph.add_node(ego_node)
            nodes = tmp_graph.nodes()
            for node in nodes:
                tmp_graph.add_edge(ego_node, node)
            ego_lst[ego_node] = tmp_graph
            graph.add_edges_from(tmp_graph.edges())
    return graph

def generate_graph(fpath):
    G = nx.Graph()
    egos = ['0', '107', '348', '414', '686', '698', '1684', '1912', '3437', '3980']
    node2Circle = {}
    circle2Node = {}

    for ego in egos:
        e = int(ego)
        nodeLst = []
        node2Circle[e] = e

        edgeFile = fpath + ego + '.edges'
        f = open(edgeFile, 'r')
        for line in f:
            m = line.split()
            fn = int(m[0])
            tn = int(m[1])
            G.add_edge(fn, tn)
        f.close()

        nodeFile = fpath + ego + '.feat'
        f = open(nodeFile, 'r')
        for line in f:
            nodeLst.append(int(line.split()[0]))
        for n in nodeLst:
            node2Circle[n] = e
            if e == n: pass
            G.add_edge(e, n)
        f.close()
    return G, node2Circle