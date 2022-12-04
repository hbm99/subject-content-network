from utils import pdfs_info_dict
from content import Content
from network import Graph
import networkx


if __name__ == '__main__':
    
    pdfs_text_info = pdfs_info_dict("pdfs/")
    
    contents = [
        
        #region Angela's notes contents
        
        #region Interpolación
        
        Content('lagrange', node_description='Fórmula de Lagrange'),
        Content('interpolacion', 'newton', node_description='Fórmula de interpolación de Newton'),
        Content('hermite', node_description='Forma de Hermite del polinomio de interpolación'),
        Content('interpolacion', 'tramos', node_description='Interpolación por tramos'),
        
        #endregion
        
        #region Aplicaciones de la interpolación
        
        Content('diferenciacion', 'numerica', node_description='Diferenciación numérica'),
        Content('integracion', 'aproximada', node_description='Integración aproximada'),
        Content('newton', 'cotes', node_description='Fórmulas de Newton Cotes'),
        Content('richardson', node_description='Extrapolación de Richardson'),
        Content('romberg', node_description='Algoritmo de Romberg'),
        
        #endregion
        
        #region Ecuaciones diferenciales ordinarias
        
        Content('integracion', 'serie', 'Taylor', node_description='Integración por serie de Taylor'),
        Content('euler', node_description='Método de Euler'),
        Content('runge-kutta', node_description='Métodos de Runge-Kutta'),
        
        #endregion
        
        #region Aproximación de funciones por mínimos cuadrados
        
        Content('ajuste', 'curva', 'lineal', node_description='Ajuste de curvas lineal'),
        Content('aproximacion', 'lineal', 'multiple', node_description='Aproximación lineal múltiple'),
        
        #endregion
        
        #endregion
        
        #region "Resumen de las clases de Numérica"'s contents
        
        Content('error', 'absoluto', node_description='Error absoluto'),
        Content('error', 'relativo', node_description='Error relativo'),
        Content('error', 'redondeo', node_description='Error de redondeo'),
        Content('error', 'truncamiento', node_description='Error de truncamiento'),
        Content('overflow', node_description='Error por overflow'),
        Content('underflow', node_description='Error por underflow'),
        Content('eliminacion', 'gauss', node_description='Eliminación de Gauss'),
        Content('sustitucion', 'inversa', node_description='Sustitución inversa'),
        Content('factorizacion', 'lu', node_description='Factorización LU'),
        Content('cholesky', node_description='Método de Cholesky'),
        Content('biseccion', node_description='Método de bisección'),
        Content('falsa', 'posicion', node_description="Método de la falsa posición"),
        Content('aproximacion', 'sucesiva', node_description="Método de las aproximaciones sucesivas o punto fijo"),
        Content('newton', 'raphson', node_description='Método de Newton-Raphson'),
        Content('metodo', 'steffensen', node_description='Método de Steffensen'),
        Content('metodo', 'lagrange', node_description='Método de Lagrange'),
        Content('metodo', 'newton', node_description='Método de Newton'),
        Content('baricentrica', 'lagrange', node_description='Interpolación baricéntrica de Lagrange'),
        Content('interpolacion', 'hermite', node_description='Interpolación de Hermite'),
        Content('cuadrado', 'minimo', node_description='Método de los cuadrados mínimos'),
        Content('polinomio', 'legendre', node_description='Polinomios de Legendre'),
        Content('polinomio', 'taylor', node_description='Polinomios de Taylor'),
        Content('lipschitz', node_description='Condición de Lipschitz')
        
        #endregion
        
    ]
    
    graph = Graph(pdfs_text_info, contents, 1000)
    
    networkx.write_gexf(graph.graph, "numerical_analysis.gexf")
    
    
    
    
    
    