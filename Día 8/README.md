
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20"/>&nbsp;


<h2 align="center">Día 8: Lista enlazada</h2>
<p align="center" >🧑‍💻👩‍💻 Implementa una función o bloque que nos permita crear una lista enlazada, es decir, nodos, enlaces, etc. No hagas uso de las funciones propias del lenguaje que estés implementado para el reto.<br>
Implementa los métodos:<br>
push: ingresa un elemento al final de la lista.<br>
pop: retira un elemento del final de la lista.<br>
shift: remueve un elemento del inicio de la lista<br>
unshift: inserta un elemento al inicio de la lista.<br>
</p>

### 🖥️ *Código:*

<p align="center">Dos clases asociadas de un Nodo y una lista de Nodos. El nodo tiene como dato una variable sin un tipo específico por lo que se puede trabajar con varios.
</p>


>Clases de Nodo y Lista

``` py
class Nodo:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.enlace = None

    def get_dato(self):
        return self.dato

    def get_enlace(self):
        return self.enlace

    def set_dato(self, dato):
        self.dato = dato

    def set_enlace(self, enlace):
        self.enlace = enlace

    def __str__(self) -> str:
        return self.dato.__str__()


class Lista:
    def __init__(self) -> None:
        self.inicio = None

    def esta_vacia(self):
        return self.inicio == None

    def push(self, dato):
        nodo_nuevo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = nodo_nuevo
        else:
            nodo_actual = self.inicio
            while (nodo_actual.get_enlace() != None):
                nodo_actual = nodo_actual.get_enlace()
            nodo_actual.set_enlace(nodo_nuevo)

    def pop(self):
        if not self.esta_vacia():
            nodo_actual = nodo_siguiente = self.inicio
            while (nodo_siguiente.get_enlace() != None):
                nodo_actual = nodo_siguiente
                nodo_siguiente = nodo_siguiente.get_enlace()
            if nodo_siguiente == self.inicio:
                self.inicio = None
            else:
                nodo_actual.set_enlace(None)

    def shift(self):
        if not self.esta_vacia():
            nodo_segundo = self.inicio.get_enlace()
            self.inicio = nodo_segundo

    def unshift(self, dato):
        nodo_nuevo = Nodo(dato)
        if not self.esta_vacia():
            nodo_nuevo.set_enlace(self.inicio)
            self.inicio = nodo_nuevo
        else:
            self.inicio = nodo_nuevo

    def __str__(self) -> str:
        if not self.esta_vacia():
            nodo_actual = self.inicio
            cadena_de_retorno = nodo_actual.__str__() + " -> "
            while (nodo_actual.get_enlace() != None):
                nodo_actual = nodo_actual.get_enlace()
                cadena_de_retorno += nodo_actual.__str__() + " -> "
            return cadena_de_retorno

```