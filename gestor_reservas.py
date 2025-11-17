"""Módulo de servicios para gestionar pasajeros, vuelos, equipajes y reservas."""

from pasaje_avion import Equipaje, Pasajero, Reserva, Vuelo


class GestorReservas:
    """Coordina las operaciones principales del sistema."""

    def __init__(self):
        self.pasajeros = {}
        self.vuelos = {}
        self.reservas = {}
        self.equipajes = {}

    # ---- Pasajeros ----
    def agregar_pasajero(self, pasajero_id, nombre, documento, nacionalidad):
        if pasajero_id in self.pasajeros:
            raise ValueError("Ya existe un pasajero con ese ID.")
        if any(p.documento == documento for p in self.pasajeros.values()):
            raise ValueError("El documento ya está asignado a otro pasajero.")
        pasajero = Pasajero(pasajero_id, nombre, documento, nacionalidad)
        self.pasajeros[pasajero_id] = pasajero
        return pasajero

    def obtener_pasajero(self, pasajero_id):
        return self.pasajeros.get(pasajero_id)

    def listar_pasajeros(self):
        return list(self.pasajeros.values())

    # ---- Vuelos ----
    def agregar_vuelo(self, codigo, origen, destino, fecha):
        if codigo in self.vuelos:
            raise ValueError("Ya existe un vuelo con ese código.")
        vuelo = Vuelo(codigo, origen, destino, fecha)
        self.vuelos[codigo] = vuelo
        return vuelo

    def obtener_vuelo(self, codigo):
        return self.vuelos.get(codigo)

    def listar_vuelos(self):
        return list(self.vuelos.values())

    # ---- Equipajes ----
    def agregar_equipaje(self, numero_serie, peso, descripcion, pasajero_id=None):
        if numero_serie in self.equipajes:
            raise ValueError("Ya existe un equipaje con ese número de serie.")
        equipaje = Equipaje(numero_serie, peso, descripcion)
        self.equipajes[numero_serie] = equipaje
        if pasajero_id is not None:
            self.asignar_equipaje_a_pasajero(numero_serie, pasajero_id)
        return equipaje

    def asignar_equipaje_a_pasajero(self, numero_serie, pasajero_id):
        equipaje = self.equipajes.get(numero_serie)
        if equipaje is None:
            raise ValueError("El equipaje no existe.")
        pasajero = self.obtener_pasajero(pasajero_id)
        if pasajero is None:
            raise ValueError("El pasajero no existe.")
        pasajero.agregar_equipaje(equipaje)
        return equipaje

    def listar_equipajes(self):
        return list(self.equipajes.values())

    # ---- Reservas para vuelo----
    def crear_reserva(self, reserva_id, codigo_vuelo, pasajero_id):
        if reserva_id in self.reservas:
            raise ValueError("Ya existe una reserva con ese ID.")
        vuelo = self.obtener_vuelo(codigo_vuelo)
        if vuelo is None:
            raise ValueError("El vuelo indicado no existe.")
        pasajero = self.obtener_pasajero(pasajero_id)
        if pasajero is None:
            raise ValueError("El pasajero indicado no existe.")
        if pasajero.tiene_reserva_para_vuelo(codigo_vuelo):
            raise ValueError("El pasajero ya tiene una reserva en ese vuelo.")

        reserva = Reserva(reserva_id, codigo_vuelo, pasajero_id)
        self.reservas[reserva_id] = reserva
        pasajero.agregar_reserva(reserva)
        if pasajero not in vuelo.lista_pasajeros:
            vuelo.agregar_pasajero(pasajero)
        if vuelo not in pasajero.historial_vuelos:
            pasajero.historial_vuelos.append(vuelo)
        return reserva

    def listar_reservas(self):
        return list(self.reservas.values())

    # - Esto nos va a servir para mostrar ----
    def resumen_general(self):
        return {
            "pasajeros": len(self.pasajeros),
            "vuelos": len(self.vuelos),
            "reservas": len(self.reservas),
            "equipajes": len(self.equipajes),
        }


