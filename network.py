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
            self.fill_content_distance(words, distance_to_ponderate)
            
        
        for content in self.graph.nodes:
            for other_content in content.distances.keys():
                if content.distances[other_content] <= distance_to_ponderate:
                    weight_value = int(distance_to_ponderate/content.distances[other_content])
                    if not self.graph.has_edge(content, other_content):
                        self.graph.add_edge(content, other_content, weight = weight_value)
                    else:
                        self.graph[content][other_content] += weight_value
        
                    
    def fill_content_distance(self, words : List[str], distance : int):
        
        for i in range(len(words)):
            for content in self.graph.nodes:
                if not isinstance(content.name, list):
                    if words[i] == content.name:
                        self.check_next_contents(self, content, words, i, distance)
                elif self.match(words, words[i], content.name):
                    self.check_next_contents(self, content, words, i, distance)
                        
    def check_next_contents(self, main_content : Content, words : List[str], index : int, distance: int):
        for i in range(index, distance + 1):
            for content in self.graph.nodes:
                if not isinstance(content.name, list):
                    if words[i] == content.name:
                        main_content.distances[content].append(i - index)
                elif self.match(words, words[i], content.name):
                    main_content.distances[content].append(i - index)
                    
    def match(self, words : List[str], content_first_word : str, name_content_to_match : List[str]):
        pass
                