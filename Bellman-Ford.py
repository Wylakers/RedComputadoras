# Importamos la librería time para poder medir el tiempo de ejecución del programa
import time
import os, psutil; 
# Inicializamos esta variable antes de iniciar el programa para comparar el tiempo 
# que pasa antes y después de ejecutar el programa
start_time = time.time()


# Algoritmo de Bellman - Ford
# Algoritmo del camino o ruta más corto/pequeño
 
# Clase para representar un grafo
class Grafo:
 
    # Se definen los vértices en la variable "V" y la lista "grafo" para almacenar
    # el origen, destino y peso de cada router
    # Al llamar a esta función se debe proporcionar el número de vertices
    def __init__(self, vertices):
        self.V = vertices #Número de vértices
        self.grafo = []  #Lista de grafos
 
    # Función para añadir un enlace, es decir, un vertice con su enlace a otro vertice
    # y su respectivo peso
    def añadir(self, origen, destino, peso):
        self.grafo.append([origen, destino, peso])
         
    # Función para imprimir la respuesta
    def imprimir(self, dist):
        print("Nodo\tDistancia desde el Nodo origen")
        for i in range(self.V):
            print("{0}\t\t\t{1}".format(i, dist[i]))
        print(" ")
     

    # Función principal del algoritmo para encontrar la ruta más corta desde el punto
    # origen hacia los otros vértices a través del algoritmo Bellman-Ford. En este caso,
    # encontré en internet un paso para hallar la ruta pero con pesos negativos.
    def BellmanFord(self, fuente):
 
        # Se inicializa las distancias hasta el infito, excepto el origen
        dist = [float("Inf")] * self.V
        dist[fuente] = 0
        
        # Cualquier ruta desde el origen hacia cualquier vértice puede tener como 
        # máximo (V-1) vértices
        for _ in range(self.V - 1):
            # Actualiza el valor de la distancia y el índice principal de los vértices
            # adyacentes del vértice origen o fuente. Se consideran solo los vértices
            # que aún están en la cola
            for origen, destino, peso in self.grafo:
                if dist[origen] != float("Inf") and dist[origen] + peso < dist[destino]:
                        dist[destino] = dist[origen] + peso
 
        
        # Este paso revisa si el grafo contiene enlaces con pesos negativos, el "for" que
        # se encuentra en la parte de arriba asegura la ruta más corta si el grafo no
        # contiene pesos negativos.
        for origen, destino, peso in self.grafo:
                if dist[origen] != float("Inf") and dist[origen] + peso < dist[destino]:
                        print("El grafo contiene enlaces con pesos negativos")
                        return 
                         
        # Llama a la función para imprimir la ruta y la suma de los pesos de cada enlace
        self.imprimir(dist)


class Main: 
    # Topologías presentadas
    # Complejidad baja
    print("\nComplejidad Baja")
    g = Grafo(8)
    g.añadir(0, 1, 3)
    g.añadir(0, 2, 6)
    g.añadir(1, 2, 2)
    g.añadir(1, 4, 8)
    g.añadir(2, 3, 4)   
    g.añadir(3, 4, 1)
    g.añadir(3, 6, 9)
    g.añadir(4, 5, 5)
    g.añadir(5, 6, 2)
    g.añadir(5, 7, 7)
    g.añadir(6, 7, 3)
    # Muestra o imprime la solución
    g.BellmanFord(0)
    
    
    # Nueva topología, solo para el caso de complejidad alta
    # Complejidad Alta
    print("Complejidad Alta")
    r = Grafo(10)
    r.añadir(0, 1, 5)
    r.añadir(0, 2, 8)
    r.añadir(0, 3, 3)
    r.añadir(1, 2, 2)
    r.añadir(1, 4, 3)
    r.añadir(2, 4, 6)
    r.añadir(2, 5, 1)
    r.añadir(2, 6, 7)
    r.añadir(3, 2, 4)
    r.añadir(3, 6, 5)
    r.añadir(4, 7, 1)
    r.añadir(4, 5, 4)
    r.añadir(5, 7, 8)
    r.añadir(5, 8, 5)
    r.añadir(5, 9, 3)
    r.añadir(6, 5, 2)
    r.añadir(6, 8, 4)
    r.añadir(7, 9, 5)
    r.añadir(8, 9, 6)
    # Imprime la solución
    r.BellmanFord(0)

print("Programa ejecutado en %s segundos" % (time.time() - start_time))
print("Uso de memoria: %s" %(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
     