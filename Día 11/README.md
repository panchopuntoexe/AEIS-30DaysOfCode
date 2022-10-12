
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 11: Notación Polaca Inversa</h2>
<p align="center" >🧑‍💻👩‍💻Programa un bloque o función que reciba una expresión como: [(3*4)+(5*7)] y lo transforme a NPI.
</p>

### 🖥️ *Código:*

<p align="center">Se implementó el algoritmo de Shunting yard para convertir una operación matemática con los operandos +, *, / y -. Este algoritmo pude recibir cadenas con paréntesis y espacios en blanco.<br>
</p>

>Se importa la librería de regex

``` py
import re
```

>Función que recibe dos operandos de: +, /, * o - y retorna: 
> 1 si el operador1 tiene mayor precedencia que operador2
> 0 si el operador1 tiene igual precedencia a operador2
> -1 si el operador1 tiene menor precedencia que operador2

``` py
def precedencia(operador1, operador2):
    if operador1 == operador2:
        return 0
    else:
        operadores = [operador1, operador2]
        for operador in operadores:
            if operador == "*" or operador == "/":
                operador = ("*", "/")
            else:
                operador = ("+", "-")
        precedencia_de_operadores = [("*", "/"), ("+", "-")]
        return precedencia_de_operadores.index(operadores[1]) - precedencia_de_operadores.index(operadores[0])

```

>Función que retorna una cadena RPN
``` py
def invertirRPN(cadena: str):
    # Se tokeniza en una lista a la cadena eliminando espacios
    tokens = re.split("", cadena.replace(" ", ""))[1:-1]

    resultado = []
    operadores = []

    for token in tokens:
        # Si el token es un número lo enviamos a la lista del resultado
        if re.search("[0-9]", token) != None:
            resultado.append(token)
        # Si es un paréntesis de apertura se lo envía a la pila de operadores
        elif re.search("[(]", token) != None:
            operadores.append(token)

        # Si es un paréntesis de cierre:
        # se envían todos los operadores en la pila hacia la lista de resultado
        # hasta encontrar un paréntesis de apertura eliminándolo de la pila
        elif re.search("[)]", token) != None:
            while operadores[-1] != "(":
                resultado.append(operadores.pop())
            operadores.pop()

        #Si es un operador se verifica que sea de mayor precedencia a la cabeza de la pila de operadores y
        # que el operador en la cabeza de la pila sea parte de * / + -. Entonces se elimina la cabeza de la 
        # pila de operadores y se la envía a la lista de resultados. Finalmente, se añade el token a la 
        # pila de operadores
        else:
            if operadores != []:
                while re.search("[*/\+\-)]", operadores[-1]) != None and precedencia(operadores[-1], token) >= 0:
                    resultado.append(operadores.pop())
            operadores.append(token)

    for token in operadores:
        resultado.append(operadores.pop())
    return resultado
```