
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 1: La sucesión de Fibonacci</h2>
<p align="center" >Programa un bloque o función que retorne los n términos de la sucesión de Fibonacci.<br>
        Programa un bloque o función que retorne el n-ésimo término de la sucesión de Fibonacci.<br>
        Programa un bloque o función que retorne la suma de los n términos de la sucesión de Fibonacci.<br>
</p>

### 🖥️ *Código:*

<p align="center">Para la solución usé bucles for en vez de una función recurrente para mejorar legibilidad y rapidez, además de una variable tipo lista para gestionar los elementos de la serie.
</p>

>Lista de términos de fibonacci

``` py
def n_terminos_de_fibonacci(n):
    lista=[0,1]
    if n==0:
        return [0]
    elif n==1:
        return lista
    else:
        for x in range(0,n+1): 
            if x>1:
                lista.append(lista[x-1]+lista[x-2])
        return lista
``` 
>Término n de fibonacci, siendo f(0)=0 y f(1)=1

``` py
def n_termino_de_fibonacci(n):
    lista=[0,1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for x in range(0,n+1): 
            if x>1:
                lista.append(lista[x-1]+lista[x-2])
        return lista[x]
``` 
>Suma de todos los términos fibonacci hasta el término n
``` py
def suma_de_n_terminos_de_fibonacci(n):
    lista=[0,1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        suma=1
        for x in range(0,n+1): 
            if x>1:
                lista.append(lista[x-1]+lista[x-2])
                suma+=lista[x]
        return suma
 ``` 
