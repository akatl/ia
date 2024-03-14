import collections

ESTADO_INICIAL = 4 
ESTADO_FINAL = 7

n_nodos = 0
id_padre = 0

# Si n_k es un nodo y n_k.estado = i para i = 1,..., 17 
# entonces los estados siguientes son i + 1 e i - 1
# si n_k.estado = 0 entonces solo i + 1
# si n_k.estado = 18 entonces solo i - 1
def test(estado):
    return estado == ESTADO_FINAL

def create_graph():
    graph = []
    graph.append([1])
    for i in range(1, 18):
        graph.append([i - 1, i + 1])
        
    graph.append([18])
    
    return graph

def init_node(id, estado, padre):
    new_node = {
        "id": id, 
        "estado": estado, 
        "padre": padre.get("id"), 
        "costo": padre.get("costo") + 1, 
        "profundidad": padre.get("profundidad") + 1, 
        "camino": padre.get("camino") + [estado],
        "test": False
    }
    
    return new_node 

def bpa(graph):
    id_nodo = 0
    id_padre = 0
    id_ppe = 0
    nodo_0 = {
        "id": 0, 
        "estado": ESTADO_INICIAL, 
        "padre": -1, 
        "costo":0, 
        "profundidad": 0, 
        "camino": [ESTADO_INICIAL], 
        "test": False
        }

    nodos = [nodo_0]
    # cola = collections.deque([ESTADO_INICIAL])
    cola = collections.deque([nodo_0])
    padres = collections.deque([-1])
    sequence  = ""
    
    while cola:
        nodo_actual = cola.popleft()
        id_ppe = padres.popleft()
        estado_nodo_actual = nodo_actual.get("estado")
        id_nodo_actual = nodo_actual.get("id")
           
        # Este ciclo se ejecuta una vez por cada vecino que tenga en la grafica
        # estado_actual, si dicho es 2 entonces se ejecuta dos veces
        # por lo tanto basta cambiar de padre solo una vez finalizado el ciclo
        for vecino in graph[estado_nodo_actual]:

            padres.append(id_nodo_actual)
            id_nodo += 1

            new_node = init_node(id_nodo, vecino, nodo_actual)
            cola.append(new_node)

            # print("P:", padres)
        # id_ppe += 1
        
        if estado_nodo_actual == ESTADO_FINAL:
            print("Camino: ", nodo_actual.get("camino"))
            break
        
        # for nodo in nodos:
            # print(f"NODO: {nodo.get('id')} Padre:{nodo.get('padre')}")



grp = create_graph()


print("BFS:")
bpa(grp)
print(grp)
