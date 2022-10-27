
<h1 align="center">#30DaysOfCode</h1>

<p align="center"><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100"></p>

### 👷‍♂️ *Realizado por:* Francisco García M.  <a href="https://www.instagram.com/edeenigma/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" title="Instagram" alt="Instagram" width="20" height="20"/></a>&nbsp;

### 🎲 *Codificado en:* Dart <img src="https://github.com/devicons/devicon/blob/master/icons/dart/dart-original.svg" title="Dart" alt="Dart" width="20" height="20"/>&nbsp;


<h2 align="center">Día 18:Lista de Objetos</h2>
<p align="center" >El programa debe mostrar lo siguiente para todos los usuarios
X elementos por la cantidad de letras del nombre
X elementos por cada 4 años cumplidos por la persona
X elementos por cada 30 cm que posea la persona
Donde X puede ser Coladita Morada o Dulces de Halloween, dependiendo que seleccionó como atributo. 
</p>

### 🖥️ *Código:*

<p align="center">
</p>

>codigo piloto
``` dart
void main() {
  List<Persona> listaDePersonas = [];
  listaDePersonas.add(Persona("Francisco", 23, 180));
  print(listaDePersonas);
}
```
>clase persona
``` dart
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

```

>Funciones de cuenta
``` dart
  int contar30CMdeEstatura() {
    int contador = 0;
    for (var i = 0; i < this.estatura!; i++) {
      if ((i + 1) % 30 == 0) contador++;
    }
    return contador;
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

```


