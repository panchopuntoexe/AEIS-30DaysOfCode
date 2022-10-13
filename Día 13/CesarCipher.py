
#Funciones de cifrado y descifrado cesar, solo para caracteres alfabéticos.
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

#Funciones de cifrado y descifrado cesar que toman en cuenta todos
# los caracteres ascii entre 31 hasta 126.
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


print(descifrar_cesar(cifrar_cesar("Hola emilia, te voy a pasar viendo a las 2 de la tarde", 5), 5))
print(descifrar_cesar_alfanumerico(cifrar_cesar_alfanumerico("Hola emilia!, te voy a pasar viendo a las 2 de la tarde", 5), 5))