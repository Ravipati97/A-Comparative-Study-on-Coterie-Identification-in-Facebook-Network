import networkx
import community
import preprocessing as preproc

if __name__ == '__main__':
    data_path = '../dataset/facebook/'
    graph, _ = preproc.generate_graph(data_path)

    # louvain fast unfolding method
    partition = community.best_partition(graph)

    #  modularity
    mod2 = community.modularity(partition, graph)
    print ("modularity of community.best_partition: ", mod2)
