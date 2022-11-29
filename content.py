from typing import List, Dict

class Content:
    def __init__(self, *name) -> None:
        self.name = name
        self.distances : Dict[Content, List[int]] = {} 


               