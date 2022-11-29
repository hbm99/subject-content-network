from utils import pdfs_info_dict
from content import Content
from network import Graph
import networkx


if __name__ == '__main__':
    
    pdfs_text_info = pdfs_info_dict("pdfs/")
    
    plu_content = Content('plu')
    epsilon_content = Content('epsilon')
    maquina_content = Content('maquina')
    contents = [epsilon_content, plu_content, maquina_content, Content('conferencia'), Content('profesor')]
    
    graph = Graph(pdfs_text_info, contents)
    
    
    
    # networkx.write_graphml(graph, "example.graphml")
    networkx.write_gexf(graph.graph, "example.gexf")
    
    
    
    
    
    