import networkx as nx
import matplotlib.pyplot as plt
import statistics as stat
import math
import time
import numpy as np

# x = nx.watts_strogatz_graph(n=100, k=20, p=0.4, seed=None,create_using = None)


# layouts = [nx.spring_layout(x), nx.circular_layout(x), nx.shell_layout(x),
#             nx.spectral_layout(x)]

# lista_wieszcholkow = list(x.nodes(data=True)) #[(0, {}), (1, {}), (2, {}), (3, {}),
# #(4, {}), (5, {}), (6, {}), (7, {}), (8, {}), (9, {})]

# lista_krawedzi = list(x.edges(data=True))    #[(0, 1, {}), (0, 9, {}), (1, 2, {}), (1, 6, {}), 
# #(2, 7, {}), (3, 7, {}), (4, 5, {}), (5, 6, {}), (7, 8, {}), (8, 9, {})]



# #print("Shortest path from 0 to 4:", nx.shortest_path(x, 0, 88))
# #print("Average shortest path length:", nx.average_shortest_path_length(x))

# cluster_coof = nx.clustering(x, nodes=[1 ,2], weight=None)  #{1: 0.24736842105263157, 2: 0.3897058823529412}
# #print(cluster_coof)

time1 = time.time()


fig, ax = plt.subplots()




avg_paths, clustering = [], []

tries = 10
probabilities = np.logspace(-3, 0, 50)
for _ in range(tries):
    p0, c0 = [],[]
    scaling =  nx.watts_strogatz_graph(n=200, k= 8, p=0)
    p0.append(nx.average_shortest_path_length(scaling))
    c0.append(nx.average_clustering(scaling))
    scal_p, scal_c = stat.mean(p0), stat.mean(c0)




for pi in probabilities: 
    paths, clusts = [], []
    for _ in range(tries):
        test = nx.watts_strogatz_graph(n=200, k= 8, p=pi)
        
        if nx.is_connected(test):
            paths.append(nx.average_shortest_path_length(test))
        else:
            print('graph is not connected bruh')
        clusts.append(nx.average_clustering(test))
    mean_path = stat.mean(paths)
    mean_clust = stat.mean(clusts)    


    clustering.append(mean_clust/scal_c)
    avg_paths.append(mean_path/scal_p)  



ax.scatter(probabilities, clustering, color="red", label="Clustering coefficient")
ax.scatter(probabilities, avg_paths, color="green", label="Average path length")
ax.set_xticks([0.0001, 0.001, 0.01, 0.1, 1])
ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())
ax.set_xscale("log")   # 👈 logarithmic x-axis
ax.set_xlabel("Rewiring probability p (log scale)")
ax.set_ylabel("Normalized value")

ax.legend()
plt.show()


time2 = time.time()

print(f'runtime : {time2 -time1} seconds')





#nx.draw(x, layouts[3], node_size=50, node_color="green")
#plt.show()
