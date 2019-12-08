import networkx as nx
import pickle
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


nodelist = []
poslist=[]
coordlist = []

file = open('openord.gexf','r')
openord = file.readlines()

for each in openord:
    if 'node id' in each:
        nodelist.append(each.split('"')[1])

for each in openord:
    if 'pos' in each:
        poslist.append(each)


for each in poslist:
    coordlist.append((each.split('"')[1], each.split('"')[3] ))


rt_edges = open('higgs-retweet_network.edgelist','r').readlines()



timing = open('higgs-activity_time.txt','r').readlines()
timing_nodes = list(map(lambda x: (int(x.split()[0]),int(x.split()[1])), timing))

# print(timing_nodes[0])
coorddict ={}
for i in range(0,len(nodelist)):
    coorddict[int(nodelist[i])] =  (float(coordlist[i][0]),float(coordlist[i][1]))

fpcoords = []
spcoords = []

for time_interval in range(0,len(timing_nodes)):
    try:
#         print('sadsd')
        fpcoords.append(coorddict[timing_nodes[time_interval][0]])
        spcoords.append(coorddict[timing_nodes[time_interval][1]])
    except:
        continue

# print ([timing_nodes[1][0]])










import random
import pylab
from matplotlib.pyplot import pause
import networkx as nx
pylab.ion()



time = 0
# print(timing_nodes[time][0],fpcoords[time])
# print(timing_nodes[time][1],spcoords[time])

graph = nx.DiGraph()
graph.add_node(timing_nodes[time][0], Position=fpcoords[time])
nx.draw(graph, pos=nx.get_node_attributes(graph,'Position'))
pylab.show()

def get_fig():
    global time
    time += 1
    graph.add_node(timing_nodes[time][0], Position=fpcoords[time])
    graph.add_node(timing_nodes[time][1], Position=spcoords[time])
    graph.add_edge(timing_nodes[time][0], timing_nodes[time][1])
    nx.draw(graph, pos=nx.get_node_attributes(graph,'Position'),node_size = 100)
    nx.write_gexf(graph, "graph.gexf")


num_plots = len(timing_nodes);
print (num_plots)
pylab.show()

for i in range(num_plots):

    get_fig()
    pylab.draw()
    pylab.savefig('Plots/'+str(i)+'png')
    pause(2)