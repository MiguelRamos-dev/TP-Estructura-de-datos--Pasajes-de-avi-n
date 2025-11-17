
from datetime import datetime   
import heapq

# --- CLASES DE SOPORTE ---

class Vuelo:
    """Clase de datos simple."""
    def __init__(self, codigo, fecha, origen, destino):
        self.codigo = codigo
        self.fecha = fecha
        self.origen = origen
        self.destino = destino

    def __lt__(self, otro):
        # LO USAMOS  para comparar objetos Vuelo si fueran usados en la cola,
        # aunque aquí solo se usa el Pasajero. Si se usan en la cola, se usaria para comparar los vuelos.
        return self.codigo < otro.codigo

class Pasajero_prioridad:
    """
    Representa a un pasajero y calcula su prioridad.
    """
    def __init__(self, nombre, clase_vuelo, millas, urgencia_medica=False):
        self.nombre = nombre
        self.clase_vuelo = clase_vuelo
        self.millas = millas
        self.urgencia_medica = urgencia_medica

    def calcular_prioridad(self):
        """
        Calcula un valor numérico de prioridad.
        El valor más bajo significa que tiene la MÁXIMA prioridad (Min-Heap).
        """
        if self.urgencia_medica:
            return 0  # Prioridad total

        clases = {'Primera': 1, 'Business': 2, 'Economica': 3}
        p_clase = clases.get(self.clase_vuelo, 100) # Base según clase

        # mientras mas millas tenga, menor es el numero y por ende, mayor es la prioridad
        p_millas = max(0, 500 - self.millas) 

        return p_clase + p_millas

    def __lt__(self, otro): #significa menor que
        """
        Define la comparación entre pasajeros basada en su prioridad.
        Permite que heapq compare directamente"""
        return self.calcular_prioridad() < otro.calcular_prioridad()
    
    #-----------------------------------------------
    
    # 2 implementacion de una cola de prioridad para los pasajeros usando heapq
    
class ColaPrioridadEmbarque:
        
#Implementación de la Cola de Prioridad usando el módulo 'heapq' (Min-Heap binario).
 #   Cada elemento en el heap es una tupla con (prioridad_numerica, pasajero).
    def __init__(self):
        # El 'heap' es simplemente una lista de Python que heapq gestiona
        # como un árbol binario casi completo (heap binario).
        self.heap = []
        self.contador = 0 # Para romper cuando hay empates de prioridad

    def agregar_pasajero(self, pasajero):
        """
        Añade un pasajero al heap. Complejidad: O(log n).
        """
        # El elemento que se inserta es una tupla: (prioridad, orden_llegada, pasajero)
        # El primer elemento (prioridad) determina la posición en el heap.
        # El segundo (contador) resuelve empates de forma estable (FIFO).
        prioridad = pasajero.calcular_prioridad()
        heapq.heappush(self.heap, (prioridad, self.contador, pasajero))
        self.contador += 1
        print(f"[{pasajero.nombre}] agregado con prioridad: {prioridad}. Tamaño de la cola: {len(self.heap)}")

    def siguiente_a_embarcar(self):
        """
        Extrae y devuelve el pasajero con la MÁXIMA prioridad (el menor valor numérico).
        Complejidad: O(log n).
        """
        if not self.heap:
            print("La cola de embarque está vacía.")
            return None

        # heapq.heappop extrae la tupla más pequeña (según el primer elemento: la prioridad)
        prioridad, _, pasajero = heapq.heappop(self.heap)
        print(f"Embarcando a: [{pasajero.nombre}] (Prioridad: {prioridad})")
        return pasajero

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return not self.heap
    
    
    #---------------------
    # --- DEMOSTRACIÓN  Y RESULTADOS---

print("==============================================")
print("PRUEBA: COLA DE PRIORIDAD (HEAP BINARIO)")
print("==============================================")

# Crear pasajeros
p1 = Pasajero_prioridad("Ana (Urgencia)", "Economica", 1000, urgencia_medica=True) # Prioridad: 0
p2 = Pasajero_prioridad("Carlos (Primera)", "Primera", 500)                        # Prioridad: 1 + 0 = 1
p3 = Pasajero_prioridad("Beatriz (Business, 100 millas)", "Business", 100)        # Prioridad: 2 + 400 = 402
p4 = Pasajero_prioridad("David (Económica, 0 millas)", "Economica", 0)            # Prioridad: 3 + 500 = 503
p5 = Pasajero_prioridad("Elena (Primera, 100 millas)", "Primera", 100)            # Prioridad: 1 + 400 = 401

cola_embarque = ColaPrioridadEmbarque()

# Añadimos en orden no prioritario
cola_embarque.agregar_pasajero(p3) # Prioridad 402
cola_embarque.agregar_pasajero(p5) # Prioridad 401
cola_embarque.agregar_pasajero(p4) # Prioridad 503
cola_embarque.agregar_pasajero(p1) # Prioridad 0 (Máxima)
cola_embarque.agregar_pasajero(p2) # Prioridad 1

print("\n--- Secuencia de Embarque (el orden en que salen del heap) ---")
print("Máxima Prioridad -> Mínimo valor numérico")

# El orden de salida debe ser: P1 (0), P2 (1), P5 (401), P3 (402), P4 (503)
while not cola_embarque.esta_vacia():
    cola_embarque.siguiente_a_embarcar()