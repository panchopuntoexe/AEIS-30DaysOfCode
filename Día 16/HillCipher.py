import sys
import numpy as np

# Función que recibe un mensaje a cifrar, la convierte en números según A=0, B=1,...,Z=25,
# realiza las operaciones de producto punto y mod 26
# y retorna una cadena con el mensaje cifrado y la llave.


def cifrar_hill(mensaje: str):
    llave = get_llave(len(mensaje))
    mensaje = np.array(list(map(lambda x: ord(x.upper())-65, mensaje)))
    producto_punto = np.dot(llave, mensaje) % 26
    mensaje_cifrado = producto_punto.tolist()[0]

    return "".join(str(chr(i+65)) for i in mensaje_cifrado), llave


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

# Función que crea una llave de tamaño n y verifica que sea inveritble


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


mensaje_cifrado, llave = cifrar_hill("OLA")

print(decifrar_hill(mensaje_cifrado, llave))
