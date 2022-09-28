import math
import random

#Se usarán listas para las coordenadas
# [(x,y),(...),(...),(...),...]

def distancia_entre_dos_puntos(x1,y1,x2,y2):
    return math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))

def ordenar_por_distancia(coordenadas):
    
    #Se randomiza para obtener un punto inicial aleatorio
    random.shuffle(coordenadas)

    #Se asigna como punto inicial a la variable orden_de_trabajos
    orden_de_trabajos=[coordenadas[0]]

    #Eliminamos el punto inicial de las coordenadas dadas
    coordenadas.pop(0)

    #Se itera por la variable orden_de_trabajos que ira aumentando cada vez que se encuentre una posición
    for i in orden_de_trabajos:
        
        #La variable auxiliar para comparar la menor distancia se inicializa con infinito para asegurarnos que cualquier otro valor sea menor
        distancia_menor=math.inf
        
        #Se verifica que las coordenadas dadas no sean vacias ya que se irá reduciendo esta variable
        if coordenadas!=[]:

            #Se itera en las coordenadas
            for j in coordenadas:

                #Calculo de distancia y comparación con la distancia menor anterior
                distancia=distancia_entre_dos_puntos(i[0],i[1],j[0],j[1])
                if distancia_menor>distancia:

                    #Si la nueva distancia es menor, se asignan nuevos valores al punto mas cercano y a la nueva distancia menor
                    punto_mas_cercano=j
                    distancia_menor=distancia
            
            #Se elimina el punto más cercano de las coordenadas dadas
            coordenadas.pop(coordenadas.index(punto_mas_cercano))

            #Se añade el punto más cercano al orden de trabajos
            orden_de_trabajos.append(punto_mas_cercano)
    return orden_de_trabajos

