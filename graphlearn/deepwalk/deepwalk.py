import keras
import numpy as np

class Model:
	def __init__(self,input_format='adj_list',walk_len=40,num_walks=10,directed=False,restart=False):
		self.walk_len=walk_len
		self.num_walks=num_walks
		self.input_format=input_format
		self.directed=directed
		self.restarts=restart

	

	def build_adj_list_data_matrix_(graph):
		self.data_matrix=[]
		for key,value in graph:	
	def fit(self,graph):
		if self.input_format='adj_list':
			self.data_matrix=build_adj_list_data_matrix_(graph)
		elif self.input_format='edge_list':
			self.data_matrix=build_edge_list_data_matrix_(graph)
		if self.input_format='adj_mat':
			self.data_matrix=build_adj_mat_data_matrix_(graph)

