import sys
sys.path.append('/home/suriya/Suriya/Github/Graph-Learn/graphlearn')

from graphlearn.deepwalk import Model
from matplotlib import pyplot as plt

graph={}
graph[0]=[1,2,3]
graph[1]=[1,2]
graph[2]=[1]
graph[3]=[2]
clf=Model()
clf.fit(graph)
embeddings = clf.word2vec_model.syn0

plt.scatter(embeddings[:,0],embeddings[:,1])
plt.show()
