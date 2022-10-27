//codigo piloto
void main() {
  List<Persona> listaDePersonas = [];
  listaDePersonas.add(Persona("Francisco", 23, 180));
  print(listaDePersonas);
}

class Persona {
  String? nombre;
  int? edad;
  int? estatura; //cm
  bool esNacional;
  String totem = "";

  Persona(this.nombre, this.edad, this.estatura, [this.esNacional = true]) {
    crearTotem();
    contarLetrasDeNombre();
    contar4aniosDeEdad();
    contar30CMdeEstatura();
  }

  @override
  String toString() {
    String elementos = "";
    for (var i = 0; i < contar30CMdeEstatura(); i++) {
      elementos += this.totem + " ";
    }
    elementos += "\n";
    for (var i = 0; i < contarLetrasDeNombre(); i++) {
      elementos += this.totem + " ";
    }
    elementos += "\n";
    for (var i = 0; i < contar4aniosDeEdad(); i++) {
      elementos += this.totem + " ";
    }
    return elementos;
  }

  void crearTotem() {
    if (this.esNacional) {
      this.totem = "\n                                  ████████████████\n                              ██████░░░░░░████░░░░██  ████\n                          ████░░░░████░░░░░░██░░░░░░██░░░░██\n                        ██░░░░░░░░░░██░░░░░░██░░░░░░░░██░░░░██\n                        ██░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░██\n                      ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██\n                      ██▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓██\n                      ██▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓██\n                        ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████\n                            ██████████████████████████";
      return;
    }
    this.totem = "███████████████████████████\n███████▀▀▀░░░░░░░▀▀▀███████\n████▀░░░░░░░░░░░░░░░░░▀████\n███│░░░░░░░░░░░░░░░░░░░│███\n██▌│░░░░░░░░░░░░░░░░░░░│▐██\n██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n██▌░│██████▌░░░▐██████│░▐██\n███░│▐███▀▀░░▄░░▀▀███▌│░███\n██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n████▄─┘██▌░░░░░░░▐██└─▄████\n█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n███████▄░░░░░░░░░░░▄███████\n██████████▄▄▄▄▄▄▄██████████\n███████████████████████████";
  }

  int contarLetrasDeNombre() {
    return this.nombre!.length;
  }

  int contar4aniosDeEdad() {
    int contador = 0;
    for (var i = 0; i < this.edad!; i++) {
      if ((i + 1) % 4 == 0) contador++;
    }
    return contador;
  }

  int contar30CMdeEstatura() {
    int contador = 0;
    for (var i = 0; i < this.estatura!; i++) {
      if ((i + 1) % 30 == 0) contador++;
    }
    return contador;
  }

}
