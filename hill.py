import numpy as np

def normalizar(data):
    """Normaliza los datos de data y regresa un array normalizado"""
    # Aqui guardamos los datos normalizados
    observaciones = data 
 
    # Maximos y minimos por columna
    maximos = np.amax(data, axis=0) 
    minimos = np.amin(data, axis=0) 

    # El tamano del array
    rango = data.shape    

    for i in range(rango[0]):
        for j in range(rango[1]):
           observaciones[i][j]  = (data[i][j] - minimos[j])/(maximos[j] - minimos[j])
           
    return observaciones

def solucion_inicial():
    solucion = []
    for i in range(150):
        solucion.append(np.random.randint(0,3))
        
    return solucion
    

def funcion_objetivo(solucion, data):
    centroides = [4*[0], 4*[0], 4*[0]]
    contador = [0, 0, 0]
    distancia = 0
    
    for i in range(3):
        for j in range(150):
            if solucion[j] == i:
                centroides[i] += data[j]
                contador[i] += 1
    
    for i in range(3):
        if contador[i] != 0:
            centroides[i] = centroides[i]/contador[i]

   
    for i in range(3):
        for j in range(150):
            if solucion[j] == i:
                for k in range(4):
                    distancia += abs(centroides[i][k] - data[j][k])

    return distancia
     
# Cargamos el archivo
archivo = np.genfromtxt('src/IRIS.csv', delimiter=',')

# Quitamos el primer renglon
data = archivo[1:]

# Quitamos la ultima columna
data = np.delete(data, 4, axis=1)

# Normalizamos los datos
obs = normalizar(data)

# Hill climbing
# for k in range(30):
# Generamos la solucion inicial 
sol_inicial = solucion_inicial()

# vecinos = np.array([150*[0], 150*[0], 150*[0]])
vecinos = np.zeros((3,150))
sol_actual = sol_inicial
costo_actual = funcion_objetivo(sol_actual, obs)

for i in range(100):
    for j in range(150):
        for i in range(3):
            if i != sol_actual[j]:
                aux = sol_actual[j]
                sol_actual[j] = i
                vecinos[i][j] = funcion_objetivo(sol_actual, obs)
                sol_actual[j] = aux
            else:
                vecinos[i][j] = 1000000

    m,n = np.unravel_index(np.argmin(vecinos), vecinos.shape)
    if vecinos[m][n] <= costo_actual:
        sol_actual[n] = m
        costo_actual = vecinos[m][n]

print(costo_actual)
print(sol_actual)
