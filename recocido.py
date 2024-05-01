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
for itt in range(30):
    sol_inicial = solucion_inicial()
    mejor_sol = np.zeros(150)
    sol_actual = np.zeros(150)

    mov1 = 0
    mejor_costo = 0.0
    costo_actual = 0.0
    costo_vecino = 0.0

# Parametros
    tempI = 10
    tempF = 0.001
    alfa = 0.95
    temp = 0.0

    maxIt = 150
# it = 0

# Inicializacion
    sol_actual = sol_inicial
    mejor_sol = sol_inicial

    costo_actual = funcion_objetivo(sol_actual, obs)
    mejor_costo = costo_actual

# Recocido simulado
    temp = tempI
    while(temp > tempF):
        for it in range(maxIt):
            a = np.random.randint(0,150)
            mov1 = sol_actual[a]
            b = np.random.random()
            if b < 0.5:
                sol_actual[a] = (sol_actual[a] + 1)%3
            else:
                sol_actual[a] = (sol_actual[a] - 1)%3
            costo_vecino = funcion_objetivo(sol_actual, obs)
            v = costo_vecino - costo_actual
            b = np.random.random()
            if(b < np.exp((-1)*(v)/(temp))):
                costo_actual = costo_vecino
            else:
                sol_actual[a] = mov1

            if mejor_costo > costo_vecino:
                mejor_costo = costo_vecino
                mejor_sol = sol_actual
        temp = temp*alfa
        
    # print(mejor_sol)
    print(mejor_costo)
