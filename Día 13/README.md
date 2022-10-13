
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 13: Cifrado Cesar</h2>
<p align="center" >🧑‍💻👩‍💻Programa un bloque o función que reciba como parámetro una cadena de texto y un número que indique cuántas posiciones se tiene que desplazar desde la posición original.<br>
🧑‍💻👩‍💻Programa un bloque o función que reciba como parámetro una cadena cifrada y un número n, con la finalidad de que se puede la cadena Original<br>
[OPCIONAL] En este caso el cifrado para los anteriores problemas es únicamente para el alfabeto, que pasa si un usuario quiere añadir números y caracteres especiales en un orden dado, ¿Cómo solucionarías el problema?, Pon un ejemplo haga uso de números y caracteres especiales.
</p>

### 🖥️ *Código:*

<p align="center">Se tomaron los números de la tabla ascii para los rangos de letras mayúsculas y minúsculas, y se gestionó que solo se cifren estos caracteres para el cifrado cesar clásico. Para cadenas con caracteres especiales, se tomo un solo rango desde el espacio en blanco ascii 31 hasta el caracter ~ ascii 126 y se gestionó para que se intercambien los caracteres circularmente.<br>
</p>

>Funciones de cifrado y descifrado cesar, solo para caracteres alfabéticos.

``` py
def cifrar_cesar(mensaje: str, posiciones):
    mensaje_cifrado = ""
    for char in mensaje:
        if(char.isalpha()):
            ascii_char = ord(char)
            for _ in range(posiciones):
                if ascii_char == 90:
                    ascii_char = 64
                elif ascii_char == 122:
                    ascii_char = 96
                ascii_char += 1
            mensaje_cifrado += chr(ascii_char)
        else:
             mensaje_cifrado +=char
    return mensaje_cifrado.replace("!"," ")

def descifrar_cesar(mensaje_cifrado: str, posiciones):
    mensaje = ""
    for char in mensaje_cifrado:
        if(char.isalpha()):
            ascii_char = ord(char)
            for _ in range(posiciones):
                if ascii_char == 65:
                    ascii_char = 91
                elif ascii_char == 97:
                    ascii_char = 123
                ascii_char -= 1
            mensaje += chr(ascii_char)
        else:
             mensaje +=char
    return mensaje

```


>Funciones de cifrado y descifrado cesar que toman en cuenta todos
> los caracteres ascii entre 31 hasta 126.
``` py
def cifrar_cesar_alfanumerico(mensaje: str, posiciones):
    mensaje_cifrado = ""
    for char in mensaje:
            ascii_char = ord(char)
            for _ in range(posiciones):
                if ascii_char == 126:
                    ascii_char = 31
                ascii_char += 1
            mensaje_cifrado += chr(ascii_char)
    return mensaje_cifrado.replace("!"," ")

def descifrar_cesar_alfanumerico(mensaje_cifrado: str, posiciones):
    mensaje = ""
    for char in mensaje_cifrado:
            ascii_char = ord(char)
            for _ in range(posiciones):
                if ascii_char == 32:
                    ascii_char = 127
                ascii_char -= 1
            mensaje += chr(ascii_char)
    return mensaje

```