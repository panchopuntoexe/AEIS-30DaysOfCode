#Se importa la librería de expresiones regulares
import re

#Verificamos si es letra
def es_letra(letra):
    return re.match("[A-Za-z]",letra)

print(
    #Se consulta la longitud de la lista final
    len(
        list(
            #Se filtra según la verificación de es_letra
            filter(es_letra, "4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^"))))

#De la misma manera para contar los números

#Verificamos si es número
def es_numero(numero):
    return re.match("[0-9]",numero)

print(len(list(filter(es_numero, "4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^"))))