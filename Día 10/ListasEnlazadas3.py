
#ObjetoGit que reemplaza al nudo en la lista, esta clase tiene dos referencias:
#  a un nodo historial o a una rama
class ObjetoGit:
    def __init__(self, comentario, datos, rama) -> None:
        self.comentario = comentario
        self.datos = datos
        self.enlace_historial = None
        self.enlace_rama = None
        self.rama = rama

    def get_datos(self):
        return self.comentario, self.datos

    def get_enlace_historial(self):
        return self.enlace_historial

    def get_enlace_rama(self):
        return self.enlace_rama

    def get_rama(self):
        return self.rama

    def set_rama(self, rama):
        self.rama = rama

    def set_datos(self, comentario, datos):
        self.comentario = comentario
        self.datos = datos

    def set_enlace_historial(self, enlace_historial):
        self.enlace_historial = enlace_historial

    def set_enlace_rama(self, enlace_rama):
        self.enlace_rama = enlace_rama

    def __str__(self) -> str:
        return "Comentario: \"" + self.comentario + "\"\nDatos:\"" + self.datos + "\""

#Clase que reemplaza a la clase lista enlazada, esta clase usa dos cabezas:
# una relativa que indica la rama en la que se encuentra y otra absoluta que indica el primer commit
class SistemaGit:
    def __init__(self) -> None:
        self.inicio_absoluto = None
        self.inicio_relativo = None

    def esta_vacia(self):
        return self.inicio_absoluto == None

    # Commit en la rama actual
    def git_commit(self, comentario, dato):
        nodo_nuevo = ObjetoGit(comentario, dato, "")
        if self.esta_vacia():
            nodo_nuevo.set_rama("main")
            self.inicio_absoluto = nodo_nuevo
            self.inicio_relativo = self.inicio_absoluto
        else:
            nodo_nuevo.set_rama(self.get_rama_actual())
            nodo_actual = self.inicio_relativo
            while (nodo_actual.get_enlace_historial() != None):
                nodo_actual = nodo_actual.get_enlace_historial()
            nodo_actual.set_enlace_historial(nodo_nuevo)

        print("["+self.get_rama_actual()+"] se actualizó el nodo \'"+nodo_nuevo.comentario
                +"\'\n1 nodo cambiado, 1 inserción(+)\n")

    # Crear una nueva rama
    def git_branch(self, nombre_de_rama):
        if not self.esta_vacia():
            # Se busca el nodo más actual en el historial, es decir, el nodo actual
            nodo_actual = self.inicio_relativo
            while (nodo_actual.get_enlace_historial() != None):
                nodo_actual = nodo_actual.get_enlace_historial()
            # Clono el objeto
            comentario_clon, datos_clon = nodo_actual.get_datos()
            nodo_actual.set_enlace_rama(
                ObjetoGit(comentario_clon, datos_clon, nombre_de_rama))
            # Se cambia la rama cambiando la cabeza relativa al nuevo nodo de la nueva rama
            self.inicio_relativo = nodo_actual.get_enlace_rama()

        # print(self.get_rama_actual())

    # información del objeto del nodo actual
    def git_status(self):
        if not self.esta_vacia():
            nodo_actual = self.inicio_relativo
            while (nodo_actual.get_enlace_historial() != None):
                nodo_actual = nodo_actual.get_enlace_historial()
            return "\t\tRama: \"" + self.get_rama_actual() + "\"\n" + nodo_actual.__str__()

    # buscar rama en el sistema git
    def git_checkout(self, nombre_a_buscar):
        rama = self.buscar_rama(nombre_a_buscar, self.inicio_absoluto)
        if rama != None:
            self.inicio_relativo = rama
        print("Se ha cambiado a la rama: \'"+self.get_rama_actual()+"\'\n")

    def buscar_rama(self, nombre_a_buscar, nodo: ObjetoGit):
        if nodo.get_rama() == nombre_a_buscar:
            return nodo
        elif nodo.get_rama() == None and nodo.get_enlace_historial() == None:
            return None
        elif nodo.get_enlace_historial() != None:
            nodo_actual = nodo
            while (nodo_actual.get_enlace_historial() != None):
                if nodo_actual.get_enlace_rama() != None:
                    rama = self.buscar_rama(
                        nombre_a_buscar, nodo_actual.get_enlace_rama())
                    if rama != None:
                        return rama
                nodo_actual = nodo_actual.get_enlace_historial()

            #añadiendo una iteración final para el último nodo
            if nodo_actual.get_enlace_rama() != None:
                rama = self.buscar_rama(
                    nombre_a_buscar, nodo_actual.get_enlace_rama())
                if rama != None:
                    return rama

    #Eliminar el último commit de la rama en la que nos encontramos
    def git_revert(self):
        if not self.esta_vacia():
            nodo_actual = nodo_siguiente = self.inicio_relativo
            while (nodo_siguiente.get_enlace_historial() != None):
                nodo_actual = nodo_siguiente
                nodo_siguiente = nodo_siguiente.get_enlace_historial()
            if nodo_siguiente == self.inicio_relativo:
                self.inicio_relativo = None
            else:
                nodo_actual.set_enlace_historial(None)
            print("["+self.get_rama_actual()+"] se eliminó el cambio \'"+nodo_siguiente.comentario
                +"\'\n1 nodo cambiado, 1 eliminación(-)\n")

    def git_show_head(self):
        print("commit: \'"+self.inicio_relativo.comentario+"\'\nrama: "+self.get_rama_actual()
                +":datos:\n"+self.inicio_relativo.datos)

    def get_rama_actual(self):
        return self.inicio_relativo.get_rama()

    def __str__(self) -> str:
        if not self.esta_vacia():
            nodo_actual = self.inicio_relativo
            cadena_de_retorno = "\t\tRama: \"" + self.get_rama_actual() + "\"\n"
            cadena_de_retorno += nodo_actual.__str__() + "\n\t| \n\tV\n"
            while (nodo_actual.get_enlace_historial() != None):
                nodo_actual = nodo_actual.get_enlace_historial()
                cadena_de_retorno += nodo_actual.__str__() + "\n\t|\n\tV\n"
            return cadena_de_retorno


#Llamadas de prueba
sistema_git = SistemaGit()
sistema_git.git_commit("Primer commit", "a + b")
sistema_git.git_commit("Segundo commit", "a + b -c")

sistema_git.git_branch("Primera iteración")
sistema_git.git_commit("fix:Segundo commit", "a + b - c")
sistema_git.git_commit("Primer commit", "a + b")

sistema_git.git_branch("Develop")
sistema_git.git_commit("fix:Segundo commit", "a / b * c")

sistema_git.git_checkout("Primera iteración")
sistema_git.git_commit("Segundo commit", "a + b * c")

sistema_git.git_checkout("main")

sistema_git.git_commit("Tercer commit", "qwerty")

sistema_git.git_branch("Segunda iteración")
sistema_git.git_commit("Cero Commit", "abc")
sistema_git.git_commit("Primer commit", "acccc")
sistema_git.git_commit("Segundo commit", "cbca")


sistema_git.git_checkout("Segunda iteración")

sistema_git.git_revert()

sistema_git.git_show_head()

#print(sistema_git.__str__())
