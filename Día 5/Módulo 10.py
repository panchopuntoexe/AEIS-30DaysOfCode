#Funciones para duplicar pares o impares según una posición
def duplicar_pares(numero,posicion):
    if posicion%2==0:
        return int(numero)*2

def duplicar_impares(numero,posicion):
    if posicion%2!=0:
        return int(numero)*2

#Funciones para extraer pares o impares según una posición
def extraer_pares(numero,posicion):
    if posicion%2==0:
        return numero

def extraer_impares(numero,posicion):
    if posicion%2!=0:
        return numero

#Aminorar decenas por 9 unidades
def aminorar_decenas(numero):
    if numero>9:
        return numero-9
    return numero



def tarjeta_es_valida(tarjeta):

    #Dependiendo de si hay una longitud par o impar se puede seleccionar 
    # para seguir con la regla de tomar desde el penúltimo elemento
    if len(tarjeta)%2==0:

        #Se duplican los pares y se extraen los números sobrantes
        lista = list(map(duplicar_pares,tarjeta,range(0,len(tarjeta)+1)))
        lista_sobrante = list(map(extraer_impares,tarjeta,range(0,len(tarjeta)+1)))
    else:

        #Se duplican los impares y se extraen los números sobrantes
        lista = list(map(duplicar_impares,tarjeta,range(0,len(tarjeta)+1)))
        lista_sobrante = list(map(extraer_pares,tarjeta,range(0,len(tarjeta)+1)))

    #Se eliminan los elementos None con un filtro y una función lambda
    lista_extraida,lista_sobrante_extraida = list(filter(lambda x: x!=None, lista)),list(filter(lambda x: x!=None, lista_sobrante))

    #Se aminoran las decenas y se añade los números sobrantes a la lista final calculada
    lista_final = list(map(aminorar_decenas, lista_extraida))
    lista_final.extend(list(map(int,lista_sobrante_extraida)))

    return sum(lista_final)%10==0 

#Al pedir modulo n solo se usa una variable al final de la función
def tarjeta_es_valida(tarjeta,n):
    if len(tarjeta)%2==0:
        lista = list(map(duplicar_pares,tarjeta,range(0,len(tarjeta)+1)))
        lista_sobrante = list(map(extraer_impares,tarjeta,range(0,len(tarjeta)+1)))
    else:
        lista = list(map(duplicar_impares,tarjeta,range(0,len(tarjeta)+1)))
        lista_sobrante = list(map(extraer_pares,tarjeta,range(0,len(tarjeta)+1)))

    lista_extraida,lista_sobrante_extraida = list(filter(lambda x: x!=None, lista)),list(filter(lambda x: x!=None, lista_sobrante))

    lista_final = list(map(aminorar_decenas, lista_extraida))
    lista_final.extend(list(map(int,lista_sobrante_extraida)))

    return sum(lista_final)%n==0 