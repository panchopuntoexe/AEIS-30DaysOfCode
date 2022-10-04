frase = "One-Time Password as a service"

#Función que recibe la frase y retorna una cadena
def obtener_abreviacion(frase):
    #Se reemplaza cualquier guión con un espacio vacío
    frase=frase.replace("-"," ")

    #Si existe "as a service" en la frase se la reemplaza con "as a Service"
    if "as a service" in frase:
        frase=frase.replace("as a service","as a Service")

        #Se separa en una lista la frase con split y se selecciona la primera letra
        # con una función lambda en map
        lista_de_iniciales = list(map(lambda x:x[0],frase.split(" ")))

        for letra in lista_de_iniciales:

            #Si existe una letra minúscula que no sea "a", se la reemplaza con ""
            if letra.islower() and not letra=="a":
                lista_de_iniciales = list(map(lambda x: x.replace(letra, ""), lista_de_iniciales))
    else:
        lista_de_iniciales = list(map(lambda x:x[0],frase.split(" ")))
        for letra in lista_de_iniciales:

            #Si existe una letra minúscula se la reemplaza con ""
            if letra.islower():
                lista_de_iniciales = list(map(lambda x: x.replace(letra, ""), lista_de_iniciales))

    #Se une la lista de letras en una cadena
    return ''.join(lista_de_iniciales)

print (obtener_abreviacion(frase))

