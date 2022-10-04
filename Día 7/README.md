
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 7: Abreviación</h2>
<p align="center" >🧑‍💻👩‍💻 Programa un bloque o función que nos ayude a conocer el acrónimo de una frase dada. No importa si el acrónimo existe o no, sin embargo ten las siguientes consideraciones:
Infrastructure as a service -> IaaS
One-Time Password as a service -> OTPaaS
Liquid-crystal display -> LDC<br>
🧑‍💻👩‍💻 Explica, que consideraciones tomaste a la hora de desarrollar tu algoritmo.
</p>

### 🖥️ *Código:*

<p align="center">Para toda cadena convierto las palabras en elementos de una lista y tomo el primer elemento de cada palabra, es decir, su inicial. Si en una cadena existe la sub cadena "as a service", la reemplazo con "as a Service" y verifico que no se eliminen de la lista final. Además, si existe una cadena con el caracter "-" se lo reemplaza con un espacio. Finalemnte, de la lista final de letras, se las une y retorna una cadena. 
</p>


>Función que recibe la frase y retorna una cadena

``` py
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
```
>Diseño

![](https://github.com/panchopuntoexe/AEIS-30DaysOfCode/blob/main/D%C3%ADa%207/code2flow_ZDLjbI.png)
