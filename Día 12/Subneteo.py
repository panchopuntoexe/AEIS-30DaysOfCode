import math

#Función que toma el numero de hosts requerido (sin contar gateway y red)
# y retorna la mascara en formato decimal x.x.x.x

def mascara_de_hosts(numero_de_hosts):
    return CIDR_a_decimal(max(0, int(32 - math.log2(numero_de_hosts + 2))))

#Se ingresa una cadena con el formato xxx.xxx.xxx.xxx y 
# retorna el numero de hosts máximos
def hosts_de_mascara(mascara: str):
    return max(0, int(math.pow(2, 32 - decimal_a_CIDR(mascara)) - 2))


#Funciones de conversion de decimal a binario y viceversa

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

# Función que toma el formato CIDR: 24 y retorna el formato decimal x.x.x.x
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

# Función que toma el formato decimal x.x.x.x y retorna el formato CIDR
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


#Toma el formato decimal x.x.x.x y retorna la letra de la clase a la que pertenece
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
    


print(mascara_de_hosts(1))