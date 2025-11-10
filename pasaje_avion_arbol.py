'''Implementar un árbol binario para organizar vuelos según fecha o número de vuelo.'''
'''Modelar el historial de vuelos de un pasajero como un árbol general (cada nodo es un vuelo, ramas
son conexiones o escalas).'''
'''Implementar recorridos (preorden, inorden, postorden) y búsquedas en ambos árboles.'''


# ---- arbol binario para organizar vuelos ----
from datetime import datetime

class NodoVueloBinario:
    """Nodo para el árbol binario de vuelos"""
    def __init__(self, vuelo):
        self.vuelo = vuelo
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioVuelos:
    """Árbol binario de búsqueda (ABB) para organizar vuelos por código o fecha"""

    def __init__(self, criterio="codigo"):
        self.raiz = None
        self.criterio = criterio  # puede ser 'codigo' o 'fecha'

    def _comparar(self, v1, v2):
        """Compara vuelos según el criterio definido"""
        if self.criterio == "codigo":
            return v1.codigo < v2.codigo
        elif self.criterio == "fecha":
            return datetime.strptime(v1.fecha, "%Y-%m-%d") < datetime.strptime(v2.fecha, "%Y-%m-%d")

    def insertar(self, vuelo):
        """Inserta un vuelo en el árbol"""
        nuevo = NodoVueloBinario(vuelo)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar_recursivo(self.raiz, nuevo)

    def _insertar_recursivo(self, actual, nuevo):
        if self._comparar(nuevo.vuelo, actual.vuelo):
            if actual.izquierdo is None:
                actual.izquierdo = nuevo
            else:
                self._insertar_recursivo(actual.izquierdo, nuevo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo
            else:
                self._insertar_recursivo(actual.derecho, nuevo)

    def buscar(self, codigo):
        """Busca un vuelo por código"""
        return self._buscar_recursivo(self.raiz, codigo)

    def _buscar_recursivo(self, nodo, codigo):
        if nodo is None:
            return None
        if nodo.vuelo.codigo == codigo:
            return nodo.vuelo
        elif codigo < nodo.vuelo.codigo:
            return self._buscar_recursivo(nodo.izquierdo, codigo)
        else:
            return self._buscar_recursivo(nodo.derecho, codigo)

    # --- Recorridos ---
    def preorden(self):
        self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo:
            print(nodo.vuelo.codigo, end=" -> ")
            self._preorden(nodo.izquierdo)
            self._preorden(nodo.derecho)

    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierdo)
            print(nodo.vuelo.codigo, end=" -> ")
            self._inorden(nodo.derecho)

    def postorden(self):
        self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.izquierdo)
            self._postorden(nodo.derecho)
            print(nodo.vuelo.codigo, end=" -> ")


# -- Árbol general para el historial de vuelos de un pasajero --

class NodoVueloGeneral:
    """Cada nodo representa un vuelo y sus conexiones/escalas como hijos."""
    def __init__(self, vuelo):
        self.vuelo = vuelo
        self.hijos = []

    def agregar_conexion(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def preorden(self):
        print(self.vuelo.codigo, end=" -> ")
        for hijo in self.hijos:
            hijo.preorden()

    def postorden(self):
        for hijo in self.hijos:
            hijo.postorden()
        print(self.vuelo.codigo, end=" -> ")

    def buscar(self, codigo):
        if self.vuelo.codigo == codigo:
            return self.vuelo
        for hijo in self.hijos:
            resultado = hijo.buscar(codigo)
            if resultado:
                return resultado
        return None


