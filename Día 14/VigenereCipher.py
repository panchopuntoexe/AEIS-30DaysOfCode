import random as rd

#Función que calcula el cambio de posición de una letra mayúscula o minúscula
# el resultado es gracias a la tabla ascii de caracteres
def posicion(letra):
    if letra.isupper():
        return ord(letra) - 65
    else:
        return ord(letra) - 97

#Función que genera una clave randómica entre el alfabeto de mayúsulas o minúsculas
# retorna el mensaje cifrado y la clave.
def cifrar_vigenere_clave_random(mensaje: str):
    mensaje_cifrado = ""
    clave = ""
    for indice, char in enumerate(mensaje):
        #Se selecciona una letra mayúscula o minúscula de manera randómica
        clave += chr(rd.choice([rd.randint(65, 90), rd.randint(97, 122)]))
        if (char.isalpha()):
            ascii_char = ord(char)
            for _ in range(posicion(clave[indice])):
                if ascii_char == 90:
                    ascii_char = 64
                elif ascii_char == 122:
                    ascii_char = 96
                ascii_char += 1
            mensaje_cifrado += chr(ascii_char)
        else:
            mensaje_cifrado += char
    return mensaje_cifrado, clave

#Función de cifrado vigenere clásico
def cifrar_vigenere(mensaje: str, clave: str):
    mensaje_cifrado = ""
    #Verificación de que la clave sea igual de tamaño al mensaje
    i = 0
    while len(mensaje_cifrado) > len(clave):
        clave += clave[i]
        i += 1
    #Iteramos sobre el mensaje
    for indice, char in enumerate(mensaje):
        #Verifición de que el caracter sea alfabético, si es así lo ciframos
        if (char.isalpha()):
            ascii_char = ord(char)
            #Se itera según la posición delta que se indica desde la letra Aa
            for _ in range(posicion(clave[indice])):
                if ascii_char == 90:
                    ascii_char = 64
                elif ascii_char == 122:
                    ascii_char = 96
                ascii_char += 1
            mensaje_cifrado += chr(ascii_char)
        else:
            mensaje_cifrado += char
    return mensaje_cifrado

# Función que recibe como parámetro un mesaje cifrado y una clave de cualquier tamaño
def descifrar_vigenere(mensaje_cifrado: str, clave: str):
    mensaje = ""
    i = 0
    while len(mensaje_cifrado) > len(clave):
        clave += clave[i]
        i += 1
    for indice, char in enumerate(mensaje_cifrado):
        if (char.isalpha()):
            ascii_char = ord(char)
            for _ in range(posicion(clave[indice])):
                if ascii_char == 65:
                    ascii_char = 91
                elif ascii_char == 97:
                    ascii_char = 123
                ascii_char -= 1
            mensaje += chr(ascii_char)
        else:
            mensaje += char
    return mensaje


print(cifrar_vigenere_clave_random("AEIS GOD"))
print(cifrar_vigenere("AEIS GOD","GVFH YGI"))
print(descifrar_vigenere("GZNZ EUL", 'GVFH YGI'))
