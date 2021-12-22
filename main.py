import csv
from datetime import date
import random


class Challenge:

    def __init__(self):

        self.__categoria = 1
        self.__nombre = "Jugador"
        self.__puntaje = 0
        self.__preguntas = []

    def nuevo_jugador(self, nombre):

        print("Nombre de jugador guardado")
        self.__nombre = nombre
        print("Bienvenidx ", self.__nombre)

        print(
            "Jugarás 5 rondas, podras ganar QuizCoin💵 en cada pregunta si la contestas correctamente, en cada ronda incrementará la complejidad\nLos QuizCoin🤑 se asignaran de la siguiente manera:")

        print(
            "  Ronda 1 => 150 QuizCoin\n    Ronda 2 => 250 QuizCoin\n    Ronda 3 => 350 QuizCoin\n    Ronda 4 => 450 QuizCoin\n    Ronda 5 => 1050 QuizCoin🤯🤯")
        self.leerArchivo()
        self.inicio_ronda()

    def leerArchivo(self):

        with open('questions.csv', encoding="utf8") as csvfile:
            for row in csv.DictReader(csvfile, delimiter=','):
                self.__preguntas.append(row)

    def puntosRonda(self):

        if self.__categoria == 1:
            val = 150
        elif self.__categoria == 2:
            val = 250
        elif self.__categoria == 3:
            val = 350
        elif self.__categoria == 4:
            val = 450
        elif self.__categoria == 5:
            val = 1050

        texto = "Por " + str(val) + " QuizCoin💵"
        return texto

    def inicio_preguntas(self):

        loadRandom = int(random.uniform(0, 5))
        setDificultad = 5 * (self.__categoria - 1)

        pregunta = self.__preguntas[loadRandom + setDificultad]['pregunta']
        opcion1 = self.__preguntas[loadRandom + setDificultad]['opcion1']
        opcion2 = self.__preguntas[loadRandom + setDificultad]['opcion2']
        opcion3 = self.__preguntas[loadRandom + setDificultad]['opcion3']
        opcion4 = self.__preguntas[loadRandom + setDificultad]['opcion4']
        mensaje = self.__preguntas[loadRandom + setDificultad]['mensaje']
        respuesta = self.__preguntas[loadRandom + setDificultad]['correcta']
        return pregunta, opcion1, opcion2, opcion3, opcion4, respuesta, mensaje

    def pasarNivel(self):

        if self.__categoria < 5:
            self.__categoria += 1
            self.inicio_ronda()
        else:
            self.terminarJuego()

    def leerRanking(self):

        ranking = []
        with open('ranking.csv', encoding="utf8") as csvfile:
            for row in csv.DictReader(csvfile, delimiter=','):
                row['puntaje'] = int(row['puntaje'])
                ranking.append(row)

        return ranking

    def guardarHistorico(self):

        ranking = self.leerRanking()
        jugadorAct = {"nombre": self.__nombre, "puntaje": int(
            self.__puntaje), "categoria": self.__categoria, "fecha": str(date.today())}
        ranking.append(jugadorAct)
        ranking.sort(key=lambda p: p['puntaje'], reverse=True)

        with open('ranking.csv', 'w', newline='') as csvfile:
            cabezera = ["nombre", "puntaje", "categoria", "fecha"]
            writer = csv.DictWriter(csvfile, fieldnames=cabezera)

            writer.writeheader()
            for i in ranking:
                writer.writerow(i)

    def sumarPuntos(self):

        if self.__categoria == 1:
            self.__puntaje += 150
        elif self.__categoria == 2:
            self.__puntaje += 250
        elif self.__categoria == 3:
            self.__puntaje += 350
        elif self.__categoria == 4:
            self.__puntaje += 450
        elif self.__categoria == 5:
            self.__puntaje += 1050
        print("QuizCoin💵 acumulados: ", self.__puntaje, "\n")
        self.pasarNivel()

    def validarResultados(self, respuesta, opcion, mensaje):

        if respuesta == opcion:
            print("🎉🎊🎉✨-Respuesta Correcta-🎉🎊🎉✨")
            print(mensaje)
            self.sumarPuntos()

        else:
            print("💣💣💣-Respuesta incorrecta-💣💣💣\n\nJuego finalizado")
            print("La respuesta correcta es: ", mensaje)
            print("Tienes acumulados: ", self.__puntaje, " QuizCoin💵\n")
            self.terminarJuego()

    def terminarJuego(self):

        self.guardarHistorico()
        print("Top Ranking")
        ranking = self.leerRanking()
        for i in ranking:
            print(".............................")
            for y in i:
                print(y, " -->", i[y])

    def iniciar_juego(self):
        
        print("Bienvenido/a a: Quiz Challenge 🤠\n")

        print("Encontrarás preguntas de conocimiento general, desde música, deportes, cine y por qué no, el espacio exterior!🪐🤯")

        print("¿Estás listo/a para empezar?, buena suerte🤗!\n")

        nombreJugador = input("Por favor ingresa tu nombre: ")

        self.nuevo_jugador(nombreJugador)

    def inicio_ronda(self):

        if self.__categoria <= 5:
            pregunta, opcion1, opcion2, opcion3, opcion4, respuesta, mensaje = self.inicio_preguntas()
            print(
                "\n\nSi desea salir de inmediato del juego presione la tecla X y 'enter'\n")
            print("Ronda ", self.__categoria, "   -   ", self.puntosRonda())
            print("   * ", pregunta)
            print("   1. ", opcion1)
            print("   2. ", opcion2)
            print("   3. ", opcion3)
            print("   4. ", opcion4)

            controlador = True
            while controlador:

                opcionJugador = input(
                    "Ingresa la respuesta que creas correcta: ")

                if opcionJugador == "1" or opcionJugador == "2" or opcionJugador == "3" or opcionJugador == "4":
                    self.validarResultados(respuesta, opcionJugador, mensaje)
                    controlador = False

                elif opcionJugador == "X" or "x":
                    print("El juego ha finalizado")
                    print("QuizCoin💵 acumulados:  ", self.__puntaje, "\n")
                    self.terminarJuego()
                    controlador = False

                else:
                    print("Ingresa una opción valida por favor\n\n")


if __name__ == "__main__":
    juego1 = Challenge()
    juego1.iniciar_juego()
