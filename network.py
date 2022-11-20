import networkx as nx
from typing import Dict, Tuple, List
from content import Content

class Graph:
    def __init__(self, pdfs_info : Dict[int, Tuple[List[str], List[str]]], contents : List[Content]) -> None:
        self.graph = nx.Graph()
        self.graph.add_nodes_from(contents)
        self.ponderate(pdfs_info)
    
    def ponderate(self, pdfs_info : Dict[int, Tuple[List[str], List[str]]], distance_to_ponderate : int = 50):
        
        
        for document in pdfs_info.values():
            words = document[0]
            for i in range(len(words)):
                for content in self.graph.nodes:
                    if content.name is not list:
                        if words[i] == content.name:
                            pass # iterate distance_to_ponderate next, check other contents related, ponderate
                    elif words[i] == content.name[0]:
                        pass # iterate the rest of the content to check if it matchs, if it does, do the previous comment