import multiprocessing
import numpy as np


__espacio_vacio__=0
__lado_matriz__=5
__quina__="QUINA"
__completo__="COMPLETO"
__esquinas__="ESQUINAS"

def tarjeta_bingo():
    B = np.random.randint(1, 15,  __lado_matriz__)
    I = np.random.randint(16, 30, __lado_matriz__)
    N = np.random.randint(31, 45, __lado_matriz__)
    G = np.random.randint(46, 60, __lado_matriz__)
    O = np.random.randint(61, 75, __lado_matriz__)

    tarjeta=[list(B),list(I),list(N),list(G),list(O)]
    
    tarjeta[int(__lado_matriz__/2)][int(__lado_matriz__/2)]=__espacio_vacio__
    tarjeta=np.stack(tarjeta,-1)

    return (tarjeta)

def verificar_diagonal(tarjeta):
    bandera=True
    for indice,_ in enumerate(tarjeta):
        if tarjeta[indice][indice]!=0:
            return False

    #Verificamos la segunda diagonal si la primera no se validó
    if not bandera:
        for indice,_ in enumerate(tarjeta):
            if tarjeta[indice][__lado_matriz__-indice-1]!=0:
                return False
    return bandera

def verificar_linea(tarjeta):
    for numero in tarjeta:
        if list(numero) == list(np.zeros(__lado_matriz__)):
            return True
    return False

def verificar_esquinas(tarjeta):
    return tarjeta[0][0]==0 and tarjeta[__lado_matriz__-1][__lado_matriz__-1]==0 and tarjeta[__lado_matriz__-1][0]==0 and tarjeta[0][__lado_matriz__-1]==0

def verificar_completo(tarjeta):
    for fila in tarjeta:
        for elemento in fila:
            if elemento!=0:
                return False
    return True

def anunciar():
    B = np.random.randint(1, 75,  75)
    return list(B)

def verificar_numero(tarjeta,numero_a_verificar):
    bandera=False
    for fila in range(len(tarjeta)):
        for columna in range(len(tarjeta)):
            if tarjeta[fila][columna]==numero_a_verificar:
                tarjeta[fila][columna]=__espacio_vacio__
                bandera=True
    return bandera,tarjeta

def jugar_bingo(nombre_de_jugador,numeros_a_verificar,tipo_de_juego):
    tarjeta=tarjeta_bingo()
    
    if tipo_de_juego==__completo__:
        for numero in numeros_a_verificar:
            bandera,tarjeta=verificar_numero(tarjeta,numero)
            if bandera:
                if verificar_completo(tarjeta):
                    print(nombre_de_jugador+" ha Ganado con el número en la posición "+str(posicion))
                    return True

    elif tipo_de_juego==__esquinas__:
        for posicion,numero in enumerate(numeros_a_verificar):
            bandera,tarjeta=verificar_numero(tarjeta,numero)
            if bandera:
                if verificar_esquinas(tarjeta):
                    print(nombre_de_jugador+" ha Ganado con el número en la posición "+str(posicion))
                    return True


    elif tipo_de_juego==__quina__:
        for numero in numeros_a_verificar:
            bandera,tarjeta=verificar_numero(tarjeta,numero)
            if bandera:
                if verificar_linea(tarjeta) or verificar_diagonal(tarjeta):
                    print(nombre_de_jugador+" ha Ganado con el número en la posición "+str(posicion))
                    return True
    return False

def comenzar_juego(participantes):
    procesos=[]
    # Creates two processes
    for participante in participantes:
        p = multiprocessing.Process(target=jugar_bingo,args=participante)
        p.start()
        procesos.append(p)
 
    for p in procesos:
        p.join()

if __name__ == "__main__":
    numeros=anunciar()
    modo_de_juego=__esquinas__

    participantes = [("Pancho",numeros,modo_de_juego),
            ("Andrés",numeros,modo_de_juego),("Caro",numeros,modo_de_juego),
            ("Paul",numeros,modo_de_juego),("Kare",numeros,modo_de_juego)]

    comenzar_juego(participantes)
