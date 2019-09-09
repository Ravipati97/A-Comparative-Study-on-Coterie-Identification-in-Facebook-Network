import networkx
import preprocessing as preproc

def slpa(graph, base_partition):
    partition = {}
    tmp_partition = base_partition
    node_lst = graph.nodes()
    for node in node_lst:
        neighbor = graph.neighbors(node)

