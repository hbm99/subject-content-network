from utils import pdfs_info_dict
from content import Content
from network import Graph 


if __name__ == '__main__':
    
    pdfs_text_info = pdfs_info_dict("pdfs/")
    
    plu_content = Content('plu')
    epsilon_content = Content('epsilon', 'maquina')
    contents = [epsilon_content, plu_content]
    
    graph = Graph(pdfs_text_info, contents)
    
    
    
    
    
    