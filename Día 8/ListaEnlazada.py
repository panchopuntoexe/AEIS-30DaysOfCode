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
