from typing import List, Dict

class Content:
    def __init__(self, *name) -> None:
        self.name = name
        self.distances : Dict[Content, List[int]] = {}
        
    def insert_to_distances(self, key_content, value):
        try:
            self.distances[key_content].append(value)
        except KeyError:
            self.distances[key_content] = [value]

