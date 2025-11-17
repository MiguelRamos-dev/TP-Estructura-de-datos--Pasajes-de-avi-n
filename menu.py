"""Menú interactivo simple para gestionar reservas de pasajes de avión."""

from gestor_reservas import GestorReservas


def _solicitar(mensaje):
    return input(mensaje).strip()


def _mostrar_pasajeros(gestor):
    pasajeros = gestor.listar_pasajeros()
    if not pasajeros:
        print("No hay pasajeros cargados.")
        return
    for pasajero in pasajeros:
        print(
            f"- ID: {pasajero.pasajero_id} | Nombre: {pasajero.nombre} | "
            f"Documento: {pasajero.documento} | Equipajes: {len(pasajero.equipajes)}"
        )


def _mostrar_vuelos(gestor):
    vuelos = gestor.listar_vuelos()
    if not vuelos:
        print("No hay vuelos cargados.")
        return
    for vuelo in vuelos:
        print(
            f"- Código: {vuelo.codigo} | Origen: {vuelo.origen} | Destino: {vuelo.destino} | "
            f"Fecha: {vuelo.fecha} | Pasajeros: {len(vuelo.lista_pasajeros)}"
        )


def _mostrar_reservas(gestor):
    reservas = gestor.listar_reservas()
    if not reservas:
        print("No hay reservas cargadas.")
        return
    for reserva in reservas:
        print(
            f"- Reserva {reserva.reserva_id}: pasajero {reserva.pasajero_id} "
            f"en vuelo {reserva.codigo_vuelo}"
        )


def ejecutar_menu():
    gestor = GestorReservas()
    opciones = {
        "1": "Agregar pasajero",
        "2": "Agregar vuelo",
        "3": "Agregar equipaje",
        "4": "Asignar equipaje a pasajero",
        "5": "Crear reserva",
        "6": "Listar pasajeros",
        "7": "Listar vuelos",
        "8": "Listar reservas",
        "9": "Mostrar resumen general",
        "0": "Salir",
    }

    while True:
        print("\n--- Menú de gestión de reservas ---")
        for clave, texto in opciones.items():
            print(f"{clave}. {texto}")
        eleccion = _solicitar("Seleccione una opción: ")

        try:
            if eleccion == "1":
                pasajero_id = _solicitar("ID único del pasajero: ")
                nombre = _solicitar("Nombre: ")
                documento = _solicitar("Documento: ")
                nacionalidad = _solicitar("Nacionalidad: ")
                gestor.agregar_pasajero(pasajero_id, nombre, documento, nacionalidad)
                print("Pasajero agregado correctamente.")

            elif eleccion == "2":
                codigo = _solicitar("Código de vuelo: ")
                origen = _solicitar("Origen: ")
                destino = _solicitar("Destino: ")
                fecha = _solicitar("Fecha (YYYY-MM-DD): ")
                gestor.agregar_vuelo(codigo, origen, destino, fecha)
                print("Vuelo agregado correctamente.")

            elif eleccion == "3":
                numero = _solicitar("Número de serie del equipaje: ")
                peso_bruto = _solicitar("Peso en kg: ")
                peso = float(peso_bruto.replace(",", "."))
                descripcion = _solicitar("Descripción: ")
                pasajero_id = _solicitar(
                    "ID del pasajero (Enter para omitir la asignación): "
                )
                pasajero_id = pasajero_id or None
                gestor.agregar_equipaje(numero, peso, descripcion, pasajero_id)
                print("Equipaje registrado correctamente.")

            elif eleccion == "4":
                numero = _solicitar("Número de serie del equipaje: ")
                pasajero_id = _solicitar("ID del pasajero: ")
                gestor.asignar_equipaje_a_pasajero(numero, pasajero_id)
                print("Equipaje asignado correctamente.")

            elif eleccion == "5":
                reserva_id = _solicitar("ID único de la reserva: ")
                codigo_vuelo = _solicitar("Código de vuelo: ")
                pasajero_id = _solicitar("ID del pasajero: ")
                gestor.crear_reserva(reserva_id, codigo_vuelo, pasajero_id)
                print("Reserva creada correctamente.")

            elif eleccion == "6":
                _mostrar_pasajeros(gestor)

            elif eleccion == "7":
                _mostrar_vuelos(gestor)

            elif eleccion == "8":
                _mostrar_reservas(gestor)

            elif eleccion == "9":
                resumen = gestor.resumen_general()
                print(
                    f"Pasajeros: {resumen['pasajeros']} | "
                    f"Vuelos: {resumen['vuelos']} | "
                    f"Reservas: {resumen['reservas']} | "
                    f"Equipajes: {resumen['equipajes']}"
                )

            elif eleccion == "0":
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Ha ocurrido un error inesperado: {error}")


if __name__ == "__main__":
    ejecutar_menu()


