def calcular_total_equipaje_pasajero(self, pasajero, visitados=None, pasajeros_procesados=None):
        
        #A Conjunto para rastrear vuelos visitados
        if visitados is None: 
            visitados = set()   
            
        #B Conjunto para rastrear pasajeros ya contados
        if pasajeros_procesados is None:
            pasajeros_procesados = set()
            
        #B Si este vuelo ya fue procesado (código en visitados), no sumar nada
        if self.codigo in visitados: 
            return 0
        else:
            #C Marcar este vuelo como visitado para no procesarlo dos veces
            visitados.add(self.codigo) 
            
        #D Acumular el peso del pasajero *en este vuelo* si está en la lista
        peso_total = 0  
        if pasajero in self.lista_pasajeros and pasajero.documento not in pasajeros_procesados:
            peso_total += sum(e.peso for e in pasajero.equipajes)
            pasajeros_procesados.add(pasajero.documento)
            
        #E Recursivamente sumar el peso de escalas y conexiones
        for escala in self.escalas:
            peso_total += escala.calcular_total_equipaje_pasajero(pasajero, visitados, pasajeros_procesados)
        for conexion in self.conexiones:
            peso_total += conexion.calcular_total_equipaje_pasajero(pasajero, visitados, pasajeros_procesados)
            
        #F Devolver el peso total acumulado
        return peso_total