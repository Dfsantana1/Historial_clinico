from ventanas.mostrar import mostrar_mensaje

registros_historiales = []

def agregar_historial(historial):
    registros_historiales.append(historial)
    mostrar_mensaje("Historial Clínico Agregado", "El historial clínico se ha guardado correctamente.")

def obtener_historiales():
    return registros_historiales

def limpiar_registros():
    registros_historiales.clear()
