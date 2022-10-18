
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 15: Cifrado Hill</h2>
<p align="center" >🧑‍💻👩‍💻Programa un bloque o función que reciba como parámetro una cadena de texto y genere un criptograma haciendo uso de cifrado de Hill
[OPCIONAL] Que deberíamos dar a una persona para que logre descifrar el mensaje original
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
        if (np.linalg.cond(matriz_candidata) < 1/sys.float_info.epsilon):
            break
    return matriz_candidata
```


