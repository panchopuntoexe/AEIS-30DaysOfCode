
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 12: Subneteo</h2>
<p align="center" >🧑‍💻👩‍💻Programa un bloque o función que reciba el número de host y nos muestre la máscara que deberá tener la subred.<br>
🧑‍💻👩‍💻Programa un bloque o función que reciba la máscara de subred y nos muerte el número máximo de host que puede tener esta máscara.<br>
🧑‍💻👩‍💻Programa un bloque o función que, a partir de la información anterior nos indique a que clase corresponde según la máscara dada o calculada.<br>
</p>

### 🖥️ *Código:*

<p align="center">Se implementaron los algortimos para convertir mascaras de red entre sus formatos de CIDR, decimal y binario. Se usó una librería propia de conversión de decimal a binario.<br>
</p>

>Se importa la librería de matemáticas

``` py
import math
```

>Función que toma el numero de hosts requerido (sin contar gateway y red)
> y retorna la mascara en formato decimal x.x.x.x

``` py
def mascara_de_hosts(numero_de_hosts):
    return CIDR_a_decimal(max(0, int(32 - math.log2(numero_de_hosts + 2))))
```

>Se ingresa una cadena con el formato xxx.xxx.xxx.xxx y 
> retorna el numero de hosts máximos
``` py
def hosts_de_mascara(mascara: str):
    return max(0, int(math.pow(2, 32 - decimal_a_CIDR(mascara)) - 2))
```

>Función que toma el formato CIDR: 24 y retorna el formato decimal x.x.x.x

``` py
def CIDR_a_decimal(mascara: int):
    mascara_decimal = [0] * 32
    for bit in range(mascara):
        mascara_decimal[bit] = 1

    lista_de_binarios = []
    byte = ""
    for indice, bit in enumerate(mascara_decimal):
        if ((indice+1) % 8 == 0):
            byte += str(bit)
            lista_de_binarios.append(byte)
            byte = ""
            continue
        byte += str(bit)

    mascara_en_decimal = [convertir_binario_a_decimal(
        int(numero)) for numero in lista_de_binarios]
    return '.'.join(map(str, mascara_en_decimal))

```

>Función que toma el formato decimal x.x.x.x y retorna el formato CIDR

``` py
def decimal_a_CIDR(mascara: str):
    mascara = mascara.split(".")
    mascara_en_binario = [convertir_decimal_a_binario(
        int(numero)) for numero in mascara]
    bits = [int(numero) for numero in ''.join(map(str, mascara_en_binario))]
    numero_de_unos = 0
    for numero in bits:
        if numero == 1:
            numero_de_unos += 1
    return numero_de_unos

```

>Toma el formato decimal x.x.x.x y retorna la letra de la clase a la que pertenece

``` py
def clase_de_mascara(mascara_decimal):
    mascara = mascara_decimal.split(".")
    mascara.reverse()
    cuenta_de_ceros = 0
    for indice in range(4):
        if mascara[indice] == "0" and cuenta_de_ceros < 3:
            cuenta_de_ceros += 1
        else:
            break
    return chr(68-max(1,cuenta_de_ceros))
```

>Funciones de conversion de decimal a binario y viceversa

``` py
def convertir_decimal_a_binario(decimal):
    resultado = []
    while decimal >= 2:
        resultado.append(decimal % 2)
        decimal = decimal//2
    resultado.append(decimal % 2)
    resultado.reverse()
    return int("".join([str(entero) for entero in resultado]))


def convertir_binario_a_decimal(binario):
    binario = int(binario)
    decimal = 0
    i = 0
    while (binario > 0):
        digito = binario % 10
        binario = int(binario//10)
        decimal = decimal+digito*(2**i)
        i = i+1
    return decimal

```