import collections

ESTADO_INICIAL = 2 
ESTADO_FINAL = 4
SEP = "-" # Separador
GRAPH = {
        "1": [2,5], "2":[1, 3], "3":[2, 4], "4":[3, 8],
        "5":[1,9], "6":[7, 10], "7":[6, 8], "8":[4, 7],
        "9":[5,13], "10":[6, 11], "11":[10, 12], "12":[11],
        "13":[9, 14], "14":[13, 15], "15":[14, 16], "16":[15]
        }

def test(estado):
    return estado == ESTADO_FINAL

def init_node(id, estado, padre):
    new_node = {
        "id": id, 
        "estado": estado, 
        "padre": padre.get("id"), 
        "costo": padre.get("costo") + 1, 
        "profundidad": padre.get("profundidad") + 1, 
        "camino": padre.get("camino") + [estado],
        "test": test(estado) 
    }
    
    return new_node 
    
def print_node(nodo):
    for key, value in nodo.items():
        print(f"{key.title()}: {value}")
        
    print(30*SEP)


def bpa(graph):
    # Contador del numero de nodos creados
    id_nodo = 0 

    # Creamos el nodo cero 
    nodo_0 = {
        "id": 0, 
        "estado": ESTADO_INICIAL, 
        "padre": -1, 
        "costo":0, 
        "profundidad": 0, 
        "camino": [ESTADO_INICIAL], 
        "test": test(ESTADO_INICIAL)
        }

    cola = collections.deque([nodo_0])
    padres = collections.deque([-1])
    
    while cola:
        nodo_actual = cola.popleft()
        estado_nodo_actual = nodo_actual.get("estado")

        id_nodo_actual = nodo_actual.get("id")
        id_padre_actual = padres.popleft()

        print_node(nodo_actual)

        if nodo_actual.get("test"):
            camino_encontrado = nodo_actual.get("camino")
            return camino_encontrado
   
        for vecino in graph[str(estado_nodo_actual)]:

            padres.append(id_nodo_actual)
            id_nodo += 1

            new_node = init_node(id_nodo, vecino, nodo_actual)
            cola.append(new_node)

        

print("BPA:")
camino = bpa(GRAPH)

if camino:
    print(30*"<")
    print("CAMINO ENCONTRADO: ", camino)
    print(30*">")
else:
    print(30*"<")
    print("CAMINO NO ENCONTRADO")
    print(30*">")
