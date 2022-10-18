
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 16:Descifrado Hill</h2>
<p align="center" >🧑‍💻👩‍💻Un bloque o función que reciba como parámetros un texto encriptado y una matriz para producir un texto claro, es decir una función que desencripte el mensaje.
[OPCIONAL] Comprueba si el método de entrega que planteaste en la solución anterior serviría para compartir mensajes de manera totalmente secreta
</p>

### 🖥️ *Código:*

<p align="center">Se tomó una cadena de caracteres y transformó según el alfabeto de Hill, en conjunto con la matriz llave, se realizó el producto punto y mod26 para obtener el resultado. Para que la persona descifre el mensaje se le debe dar el mensaje a descifrar y la llave matriz.
</p>

>Se importa la librería numpy y sys
``` py
import sys
import numpy as np
```

>Función que recibe un mensaje a cifrar, la convierte en números según A=0, B=1,...,Z=25, realiza las operaciones de producto punto y mod 26 y retorna una cadena con el mensaje cifrado y la llave.

``` py

def decifrar_hill(mensaje_cifrado: str, llave):
    inverso = get_inverso_multiplicativo(np.linalg.det(llave) % 26)
    llave_inversa = (np.linalg.inv(llave)) * inverso
    llave_inversa_mod = llave_inversa % 26
    mensaje_cifrado = np.array(
        list(
            map(
                lambda x: ord(x.upper())-65, mensaje_cifrado)))
    producto_punto = np.dot(llave_inversa_mod, mensaje_cifrado) % 26
    mensaje = producto_punto.tolist()[0]

    return "".join(str(chr(int(i)+65)) for i in mensaje)

def cifrar_hill(mensaje: str):
    llave = get_llave(len(mensaje))
    mensaje = np.array(list(map(lambda x: ord(x.upper())-65, mensaje)))
    producto_punto = np.dot(llave, mensaje) % 26
    mensaje_cifrado = producto_punto.tolist()[0]

    return "".join(str(chr(i+65)) for i in mensaje_cifrado), llave

```

>Función que crea una llave de tamaño n y verifica que sea inveritble
``` py
def get_llave(ancho):
    while (True):
        matriz_candidata = np.matrix(np.random.randint(0, 25, (ancho, ancho)))
        if (np.linalg.cond(matriz_candidata) < 1/sys.float_info.epsilon and -1 != get_inverso_multiplicativo(np.linalg.det(matriz_candidata))):
            break
    return matriz_candidata

def get_inverso_multiplicativo(determinante):
    inverso_multiplicativo = -1
    for i in range(26):
        inverso = determinante * i
        if inverso % 26 == 1:
            inverso_multiplicativo = i
            break
    return inverso_multiplicativo
```


