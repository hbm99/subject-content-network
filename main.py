from utils import pdfs_info_dict
from content import Content
from network import Graph
import networkx


if __name__ == '__main__':
    
    pdfs_text_info = pdfs_info_dict("pdfs/")
    
    contents = [
        
        #region Angela's notes contents
        
        #region Interpolación
        
        Content('formula', 'lagrange', node_description='Fórmula de Lagrange'),
        Content('formula', 'interpolacion', 'newton', node_description='Fórmula de interpolación de Newton'),
        Content('hermite', node_description='Forma de Hermite del polinomio de interpolación'),
        Content('interpolacion', 'tramos', node_description='Interpolación por tramos'),
        
        #endregion
        
        #region Aplicaciones de la interpolación
        
        Content('diferenciacion', 'numerica', node_description='Diferenciación numérica'),
        Content('integracion', 'aproximada', node_description='Integración aproximada'),
        Content('newton', 'cotes', node_description='Fórmulas de Newton Cotes'),
        Content('extrapolacion', 'richardson', node_description='Extrapolación de Richardson'),
        Content('romberg', node_description='Algoritmo de Romberg'),
        
        #endregion
        
        #region Ecuaciones diferenciales ordinarias
        
        Content('integracion', 'serie', 'Taylor', node_description='Integración por serie de Taylor'),
        Content('metodo', 'euler', node_description='Método de Euler'),
        Content('runge-kutta', node_description='Métodos de Runge-Kutta'),
        
        #endregion
        
        #region Aproximación de funciones por mínimos cuadrados
        
        Content('ajuste', 'curva', 'lineal', node_description='Ajuste de curvas lineal'),
        Content('aproximacion', 'lineal', 'multiple', node_description='Aproximación lineal múltiple'),
        
        #endregion
        
        #endregion
        
        #region "Resumen de las clases de Numérica"'s contents
        
        
        
        #endregion
        
    ]
    
    graph = Graph(pdfs_text_info, contents)
    
    
    
    # networkx.write_graphml(graph, "example.graphml")
    networkx.write_gexf(graph.graph, "example.gexf")
    
    
    
    
    
    