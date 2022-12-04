from typing import List, Dict

class Content:
    def __init__(self, *name, node_description = '') -> None:
        self.name = name
        self.distances : Dict[Content, List[int]] = {}
        self.node_description = node_description
        
    def insert_to_distances(self, key_content, value):
        try:
            self.distances[key_content].append(value)
        except KeyError:
            self.distances[key_content] = [value]
    
    def __str__(self) -> str:
        return self.node_description

