""" 
Hilo Conductor: "Gestión Integral de Pasajes de Avión"
Modalidad y Entregas
Trabajo grupal (2 o 3 integrantes)
    El trabajo se desarrolla en 4 entregas parciales (una cada tres semanas)
    Cada entrega debe incluir: desarrollo teórico, implementación en Python, documentación y material
    adicional (presentación, video, infografía, etc.)
    Defensa oral individual y grupal al finalizar
Objetivo General
    Integrar y aplicar los conceptos de estructuras de datos y análisis de algoritmos en el contexto de la
    gestión, análisis y simulación de pasajes de avión, desarrollando tanto la fundamentación teórica como la
implementación práctica.
    Entrega 1: Modelado y Encapsulamiento (Unidades 1 y 2)
Teoría
    Explicar el concepto de encapsulamiento y su importancia en la programación orientada a objetos.
    Justificar la elección de atributos y métodos para modelar pasajeros, vuelos y reservas.
    Analizar ventajas y desventajas de distintas representaciones de listas y pilas para gestionar reservas
    y equipaje.
Práctica
    Definir la clase Pasajero con atributos: nombre, documento, nacionalidad, historial de vuelos,
    equipaje, etc.
    Definir la clase Vuelo con atributos: código, origen, destino, fecha, lista de pasajeros, etc.
    Implementar interfaces para agregar/eliminar reservas y equipaje.
    Implementar una estructura recursiva para calcular el total de equipaje de un pasajero
    considerando conexiones y escalas.
    Adicional obligatorio
    Presentación (diapositivas o video corto) explicando el diseño de las clases y la lógica de
    encapsulamiento.
"""
class Equipaje:
    #creamos un metodo constructor para los atributos del equipaje.
    def __init__(self, peso, dimensiones, descripcion):
        self.peso = peso
        self.dimensiones = dimensiones
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.descripcion} - {self.peso}kg ({self.dimensiones})"


class Pasajero: 
    #creamos un metodo constructor para los atributos del pasajero.
    def __init__(self, nombre, documento, nacionalidad, historial_de_vuelos, equipaje):
        self.nombre = nombre
        self.documento = documento
        self.nacionalidad = nacionalidad
        self.historial_de_vuelos = []
        self.equipaje = equipaje

    def agregar_historial(self, Vuelo):
        self.historial_de_vuelos.append(Vuelo.codigo)

    def __str__(self):
        return f"Pasajero {self.nombre} con documento {self.documento} y nacionalidad {self.nacionalidad} con el historial de vuelos: {self.historial_de_vuelos} y el equipaje: {self.equipaje}"
        

class Vuelo:
    #creamos un metodo constructor para los atributos del vuelo.
    def __init__(self, codigo, origen, destino, fecha, lista_de_pasajeros, lista_de_equipaje):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.lista_de_pasajeros = lista_de_pasajeros
        self.lista_de_equipaje = lista_de_equipaje

    def __str__(self):
        return f"Vuelo {self.codigo} desde {self.origen} a {self.destino} el {self.fecha} con los siguientes pasajeros: {self.lista_de_pasajeros} y los siguientes equipajes: {self.lista_de_equipaje}"
    
    #creamos un metodo para agregar un pasajero al vuelo.
    def agregar_pasajero(self, pasajero):
        self.lista_de_pasajeros.append(pasajero)
        
    #creamos un metodo para eliminar un pasajero del vuelo.
    def eliminar_pasajero(self, pasajero):
        self.lista_de_pasajeros.remove(pasajero)
        
    #creamos un metodo para agregar equipaje al vuelo.
    def agregar_equipaje(self, equipaje):
        self.lista_de_equipaje.append(equipaje)
        
    #creamos un metodo para eliminar equipaje del vuelo.
    def eliminar_equipaje(self, equipaje):
        self.lista_de_equipaje.remove(equipaje)


vuelo111 = Vuelo("111", "Buenos Aires", "Madrid", "2025-01-01", [], [])

pasajero1 = Pasajero("Juan Perez", "123456789", "Argentina", [], [])
equipaje1 = Equipaje(10, "100x100x100", "Equipaje de mano")

vuelo111.agregar_pasajero(pasajero1)
vuelo111.agregar_equipaje(equipaje1)

print(vuelo111.lista_de_pasajeros)
print(vuelo111.lista_de_equipaje)
print(vuelo111.lista_de_pasajeros)
# Mostrar la representación del vuelo usando __str__

print(vuelo111)
print(pasajero1)
print(equipaje1)

pasajero1.agregar_historial(vuelo111)

