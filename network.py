import networkx as nx
from typing import Dict, Tuple, List
from content import Content

class Graph:
    def __init__(self, pdfs_info : Dict[int, Tuple[List[str], List[str]]], contents : List[Content], distance_to_ponderate : int = 300) -> None:
        self.graph = nx.Graph()
        self.graph.add_nodes_from(contents)
        self.ponderate(pdfs_info)
    
    def ponderate(self, pdfs_info : Dict[int, Tuple[List[str], List[str]]], distance_to_ponderate : int = 300):
        
        
        for document in pdfs_info.values():
            words = document[0]
            self.fill_content_distance(words, distance_to_ponderate)
            
        
        for content in self.graph.nodes:
            for other_content in content.distances.keys():
                for distance in content.distances[other_content]:
                    if distance <= distance_to_ponderate:
                        weight_value = int(distance_to_ponderate/(distance + 1))
                        if not self.graph.has_edge(content, other_content):
                            self.graph.add_edge(content, other_content, weight = weight_value)
                        else:
                            testing_var = self.graph[content][other_content]['weight']
                            testing_var += weight_value
        
                    
    def fill_content_distance(self, words : List[str], distance : int):
        
        for i in range(len(words)):
            for content in self.graph.nodes:
                if len(content.name) == 1:
                    if words[i] in content.name:
                        self.check_next_contents(content, words, i + 1, distance)
                elif self.match(words, i, content.name):
                    self.check_next_contents(content, words, i + 1, distance)
                        
    def check_next_contents(self, main_content : Content, words : List[str], index : int, distance: int):
        for i in range(index, distance + 1):
            for content in self.graph.nodes:
                if content == main_content:
                    continue
                if len(content.name) == 1:
                    if words[i] in content.name:
                        main_content.insert_to_distances(content, i - index)
                elif self.match(words, i, content.name):
                    main_content.insert_to_distances(content, i - index)
                    
    def match(self, words : List[str], content_first_word_index : int, name_content_to_match : Tuple[str]):
        index = content_first_word_index
        words_content = words[index : index + len(name_content_to_match)]
        for i in range(len(words_content)):
            if words_content[i] != name_content_to_match[i]:
                return False
        return True