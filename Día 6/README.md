
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 6: Bingo</h2>
<p align="center" >🧑‍💻👩‍💻 Programa un bloque o función que nos ayude a generar las tablas de bingo, recuerda que puede haber n participantes.<br>
🧑‍💻👩‍💻 Programa un bloque o función que simule ser la persona que canta los números. Para esto tu bloque o función tiene que mostrar el orden de salida de los 75 números. Recuerda, esto es al azar.<br>
🧑‍💻👩‍💻 Simulemos que los n participantes juegan al mismo tiempo. Programa un bloque o función que nos muestre cual participante de los n ganó en el BINGO. Para esto tu bloque o función tiene que recibir los datos necesarios, más un parámetro que nos indique si se juega cartón completo, quina (Diagonal, línea) o 4 esquinas.
</p>

### 🖥️ *Código:*

<p align="center">Se usó multiprocesamiento para simular el juego, la librería randómica en numpy para crear la matriz y la lista de números anunciantes. Funciones para verificar si hay un matriz ganadora, verificar si el número anunciado está en la matriz y verificar si un jugador tiene una matriz ganadora.
</p>

>Se importa la librería de multiprocesamiento y numpy. 
>Además se declaran variables globales del espacio vacío, el tamaño de la matriz y los modos de juego

``` py
import multiprocessing
import numpy as np

__espacio_vacio__=0
__lado_matriz__=5
__quina__="QUINA"
__completo__="COMPLETO"
__esquinas__="ESQUINAS"

```
>La tarjeta se crea con un array randómnico de numpy. Se unen los arrays con stack para crear la matriz.

``` py
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
```
>Las siguientes funciones son para verificar según el modo de juego, la matriz ganadora.
>Se usa 0 para declarar que un espacio está "tachado"

``` py
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
```

>Para anunciar una lista de números randómicos también se usa numpy

``` py
def anunciar():
    B = np.random.randint(1, 75,  75)
    return list(B)
```

>Función para verificar que si dentro de la tarjeta está el número anunciado, entonces se lo tacha

``` py
def verificar_numero(tarjeta,numero_a_verificar):
    bandera=False
    for fila in range(len(tarjeta)):
        for columna in range(len(tarjeta)):
            if tarjeta[fila][columna]==numero_a_verificar:
                tarjeta[fila][columna]=__espacio_vacio__
                bandera=True
    return bandera,tarjeta
```

>Función de un jugador, para verificar el modo de juego y bucles para iterar sobre los números anunciados

``` py
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

```

>Función que usa multiprocesamiento según el n número de participantes

``` py
def comenzar_juego(participantes):
    procesos=[]
    # Creates two processes
    for participante in participantes:
        p = multiprocessing.Process(target=jugar_bingo,args=participante)
        p.start()
        procesos.append(p)
 
    for p in procesos:
        p.join()
```

>Declaramos los numeros anunciados, el modo de jugo y un array con los participantes.

``` py
if __name__ == "__main__":
    numeros=anunciar()
    modo_de_juego=__esquinas__

    participantes = [("Pancho",numeros,modo_de_juego),
            ("Andrés",numeros,modo_de_juego),("Caro",numeros,modo_de_juego),
            ("Paul",numeros,modo_de_juego),("Kare",numeros,modo_de_juego)]

    comenzar_juego(participantes)

```