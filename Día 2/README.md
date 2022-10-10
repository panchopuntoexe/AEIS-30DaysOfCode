
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 2: Cadena Especial</h2>
<p align="center" >🧑‍💻 Programa un bloque o función que retorne la cantidad de letras que existe en la cadena.<br>
👩‍💻 Programa un bloque o función que retorne la cantidad de dígitos que existe en la cadena.<br>
</p>

### 🖥️ *Código:*

<p align="center">Se usó la función filter para colar los elementos de la cadena que cumplían con el método es_letra y es_numero.
</p>

>Se importa la librería de expresiones regulares

``` py
import re
```
>Verificamos si es letra

``` py
def es_letra(letra):
    return re.match("[A-Za-z]",letra)
```

``` py
print(
    #Se consulta la longitud de la lista final
    len(
        list(
            #Se filtra según la verificación de es_letra
            filter(es_letra, "4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^"))))
```

>De la misma manera para contar los números

``` py
def es_numero(numero):
    return re.match("[0-9]",numero)

print(len(list(filter(es_numero, "4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^"))))
```
