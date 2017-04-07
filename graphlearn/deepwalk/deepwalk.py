import numpy as np
import random
from gensim.models import Word2Vec


class Model:
	def __init__(self,input_format='adj_list',walk_len=40,num_walks=10,directed=False,restart=False,save_model=False):
		self.walk_len=walk_len
		self.num_walks=num_walks
		self.input_format=input_format
		self.directed=directed
		self.restarts=restart
		self.ndim=2
		self.save_model=save_model

	def _build_random_walk(self,key,graph):
		walk=[]
		start=key
		walk.append(start)
		while(len(walk)!=self.walk_len):
			node=walk[-1]
			node_selected=random.choice(graph[node])
			walk.append(node_selected)
		return walk
	
	def _build_adj_list_data_matrix(self,graph):
		data_matrix=[]
		for _ in xrange(self.num_walks):
			for key in graph:
				walk = self._build_random_walk(key,graph)
				data_matrix.append(walk)
		self.data_matrix_size=(len(data_matrix),len(data_matrix[0]))
		return data_matrix

	def _build_word2vec_model(self,data_matrix):
		word2vec_model=Word2Vec(data_matrix,size=self.ndim,min_count=1)
		if self.save_model:
			pass #write code to save data
		return word2vec_model
	def fit(self,graph):
		if self.input_format=='adj_list':
			data_matrix=self._build_adj_list_data_matrix(graph)
		elif self.input_format=='edge_list':
			data_matrix=build_edge_list_data_matrix_(graph)
		elif self.input_format=='adj_mat':
			data_matrix=build_adj_mat_data_matrix_(graph)
		else:
			print "Invalid Argument"
			pass

		self.word2vec_model=self._build_word2vec_model(data_matrix)
"""
graph={}
graph[0]=[1,2,3]
graph[1]=[1,2]
graph[2]=[1]
graph[3]=[2]
from graphlearn.deepwalk import Model
clf=Model()
clf.fit(graph)
"""
