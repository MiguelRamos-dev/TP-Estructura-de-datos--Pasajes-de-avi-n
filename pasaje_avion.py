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
    y equipaje."""

#PRACTICA
    
"""Definir la clase Pasajero con atributos: nombre, documento, nacionalidad, historial de vuelos,
equipaje, etc."""

"""Definir la clase Vuelo con atributos: código, origen, destino, fecha, lista de pasajeros, etc."""

"Implementar interfaces para agregar/eliminar reservas y equipaje."""

"""Implementar una estructura recursiva para calcular el total de equipaje de un pasajero
considerando conexiones y escalas."""

class Equipaje:
    """Representa un bulto de equipaje asociado a un pasajero."""

    def __init__(self, numero_serie, peso, descripcion):
        self.numero_serie = numero_serie
        self.peso = peso
        self.descripcion = descripcion

    def __str__(self):
        return (
            f"Equipaje(serie={self.numero_serie}, descripcion={self.descripcion}, "
            f"peso={self.peso}kg)"
        )


class Reserva:
    """Asocia un pasajero con un vuelo."""

    def __init__(self, reserva_id, codigo_vuelo, pasajero_id):
        self.reserva_id = reserva_id
        self.codigo_vuelo = codigo_vuelo
        self.pasajero_id = pasajero_id

    def __str__(self):
        return (
            f"Reserva(id={self.reserva_id}, codigo_vuelo={self.codigo_vuelo}, "
            f"pasajero_id={self.pasajero_id})"
        )


class Pasajero:
    """Modelo de pasajero con historial y equipajes."""

    def __init__(self, pasajero_id, nombre, documento, nacionalidad):
        self.pasajero_id = pasajero_id
        self.nombre = nombre
        self.documento = documento
        self.nacionalidad = nacionalidad
        self.equipajes = []
        self.historial_vuelos = []
        self.reservas = []

    def mostrar_info_pasajero(self):
        print(f"ID: {self.pasajero_id}")
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Equipajes:")
        if not self.equipajes:
            print("  - Sin equipajes registrados.")
        else:
            for equipaje in self.equipajes:
                print(f"  - {equipaje}")
        print(f"Peso total de equipajes: {self.peso_total_equipajes()}kg")
        print("Reservas:")
        if not self.reservas:
            print("  - Sin reservas.")
        else:
            for reserva in self.reservas:
                print(f"  - {reserva}")
        if self.historial_vuelos:
            print("Historial de vuelos:")
            for vuelo in self.historial_vuelos:
                print(f"  - {vuelo.codigo}")

    def agregar_equipaje(self, equipaje):
        if any(e.numero_serie == equipaje.numero_serie for e in self.equipajes):
            print("El equipaje ya está registrado para este pasajero.")
        else:
            self.equipajes.append(equipaje)

    def eliminar_equipaje(self, equipaje):
        self.equipajes.remove(equipaje)

    def agregar_reserva(self, reserva):
        if any(r.reserva_id == reserva.reserva_id for r in self.reservas):
            print("La reserva ya está registrada.")
            return
        if reserva.pasajero_id != self.pasajero_id:
            print("El ID del pasajero no coincide con la reserva.")
            return
        self.reservas.append(reserva)

    def eliminar_reserva(self, reserva):
        self.reservas.remove(reserva)

    def peso_total_equipajes(self):
        return sum(equipaje.peso for equipaje in self.equipajes)

    def tiene_reserva_para_vuelo(self, codigo_vuelo):
        return any(reserva.codigo_vuelo == codigo_vuelo for reserva in self.reservas)


class Vuelo:
    
    def __init__(self, codigo, origen, destino, fecha):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.lista_pasajeros = []
        self.escalas = []
        self.conexiones = []
        
    def mostrar_info_vuelo(self):
        print(f"Código: {self.codigo}")
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        print(f"Fecha: {self.fecha}")
        
        print("Lista de pasajeros:")
        print("total pasajeros:", len(self.lista_pasajeros))
        if len(self.lista_pasajeros) == 0:
            print("No hay pasajeros en este vuelo.")
        else:
            for pasajero in self.lista_pasajeros:
             print(pasajero.nombre)
            
        print("Escalas:")
        print("total escalas:", len(self.escalas))  
        if len(self.escalas) == 0:
            print("No hay escalas en este vuelo.")
        else:
            for escala in self.escalas:
             print(escala)
            
        print("Conexiones:")
        print("total conexiones:", len(self.conexiones))
        if len(self.conexiones) == 0:
            print("No hay conexiones en este vuelo.")
        else:
            for conexion in self.conexiones:
                print(conexion)
        
    def agregar_pasajero(self, pasajero):
        if pasajero in self.lista_pasajeros:
            print("El pasajero ya está en la lista.")
        else:
            self.lista_pasajeros.append(pasajero)
    
    def eliminar_pasajero(self, pasajero):  
        self.lista_pasajeros.remove(pasajero)
    
    def agregar_escala(self, vuelo):
        if vuelo in self.escalas:
            print("La escala ya está registrada.")
        else:
            self.escalas.append(vuelo)
    
    def eliminar_escala(self, vuelo):
        self.escalas.remove(vuelo)
        
    def agregar_conexion(self, vuelo):
        if vuelo in self.conexiones:
            print("La conexión ya está registrada.")
        else:
            self.conexiones.append(vuelo)  
    
    def eliminar_conexion(self, vuelo):
        self.conexiones.remove(vuelo)
    
    
    def calcular_total_equipaje_pasajero(self, pasajero, visitados=None):
        
        if visitados is None: 
            visitados = set()
        
        if self.codigo in visitados:
            return 0
        else:
            visitados.add(self.codigo)

        peso_total = 0
        if pasajero in self.lista_pasajeros:
            peso_total += sum(e.peso for e in pasajero.equipajes)

        for escala in self.escalas:
            peso_total += escala.calcular_total_equipaje_pasajero(pasajero, visitados)
        for conexion in self.conexiones:
            peso_total += conexion.calcular_total_equipaje_pasajero(pasajero, visitados)

        return peso_total

