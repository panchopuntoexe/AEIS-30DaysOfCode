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


def partir_lista(lista: Lista):
    lista_de_pares = Lista()
    lista_de_impares = Lista()
    if not lista.esta_vacia():
        nodo_actual = lista.inicio
        while nodo_actual.get_enlace() != None:
            if (nodo_actual.get_dato() % 2 == 0):
                lista_de_pares.push(nodo_actual.get_dato())
            else:
                lista_de_impares.push(nodo_actual.get_dato())
            nodo_actual = nodo_actual.get_enlace()
        if (nodo_actual.get_dato() % 2 == 0):
                lista_de_pares.push(nodo_actual.get_dato())
        else:
            lista_de_impares.push(nodo_actual.get_dato())
    return lista_de_pares, lista_de_impares


lista = Lista()
# 1 -> 54 -> 20 -> 13 -> 43 ->18 -> 11-> 53
for elemento in [1, 54, 20, 13, 43, 18, 11, 53]:
    lista.push(elemento)
print(lista.__str__())


lista_de_pares, lista_de_impares = partir_lista(lista)
print(lista_de_pares.__str__())
print(lista_de_impares.__str__())