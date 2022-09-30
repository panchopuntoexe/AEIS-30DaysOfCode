
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 5: Módulo 10</h2>
<p align="center" >Programa una función o bloque de código que nos permita comprobar si un número de tarjeta es válido o no, esto aplicando el algoritmo anterior.<br>
Como te comentamos, el algoritmo es conocido como algoritmo de modulo 10, ¿Cuál sería la adaptación si se pide implementar el mismo algoritmo, pero de modulo n?
</p>

### 🖥️ *Código:*

<p align="center">Con la función map() se puede obtener los números duplicados de ciertas posiciones y convertir un una lista de strings a lista de int. Con filter se puede obtener solo cierto tipo de cantidades deseadas.
</p>

>Funciones para extraer pares o impares según una posición

``` py
def extraer_pares(numero,posicion):
    if posicion%2==0:
        return numero

def extraer_impares(numero,posicion):
    if posicion%2!=0:
        return numero
```
>Funciones para duplicar pares o impares según una posición

``` py
def duplicar_pares(numero,posicion):
    if posicion%2==0:
        return int(numero)*2

def duplicar_impares(numero,posicion):
    if posicion%2!=0:
        return int(numero)*2
```
>Aminorar decenas por 9 unidades

``` py
def aminorar_decenas(numero):
    if numero>9:
        return numero-9
    return numero
```

``` py
def tarjeta_es_valida(tarjeta):

    #Dependiendo de si hay una longitud par o impar se puede seleccionar 
    # para seguir con la regla de tomar desde el penúltimo elemento
    if len(tarjeta)%2==0:

        #Se duplican los pares y se extraen los números sobrantes
        lista = list(map(duplicar_pares,tarjeta,range(0,len(tarjeta)+1)))
        lista_sobrante = list(map(extraer_impares,tarjeta,range(0,len(tarjeta)+1)))
    else:

        #Se duplican los impares y se extraen los números sobrantes
        lista = list(map(duplicar_impares,tarjeta,range(0,len(tarjeta)+1)))
        lista_sobrante = list(map(extraer_pares,tarjeta,range(0,len(tarjeta)+1)))

    #Se eliminan los elementos None con un filtro y una función lambda
    lista_extraida,lista_sobrante_extraida = list(filter(lambda x: x!=None, lista)),list(filter(lambda x: x!=None, lista_sobrante))

    #Se aminoran las decenas y se añade los números sobrantes a la lista final calculada
    lista_final = list(map(aminorar_decenas, lista_extraida))
    lista_final.extend(list(map(int,lista_sobrante_extraida)))

    return sum(lista_final)%10==0 
```

``` py
def tarjeta_es_valida(tarjeta,n):
    if len(tarjeta)%2==0:
        lista = list(map(duplicar_pares,tarjeta,range(0,len(tarjeta)+1)))
        lista_sobrante = list(map(extraer_impares,tarjeta,range(0,len(tarjeta)+1)))
    else:
        lista = list(map(duplicar_impares,tarjeta,range(0,len(tarjeta)+1)))
        lista_sobrante = list(map(extraer_pares,tarjeta,range(0,len(tarjeta)+1)))

    lista_extraida,lista_sobrante_extraida = list(filter(lambda x: x!=None, lista)),list(filter(lambda x: x!=None, lista_sobrante))

    lista_final = list(map(aminorar_decenas, lista_extraida))
    lista_final.extend(list(map(int,lista_sobrante_extraida)))

    return sum(lista_final)%n==0 
```