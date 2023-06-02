citas = []

def ver_mis_citas(id):
    mis_citas=[]
    for cita in citas:
        if cita.identificacion==id:
            mis_citas.append(cita)
    return mis_citas


def guardar_cita(cita):
    citas.append(cita)
    print("Registro Exitoso", "La cita ha sido agendada correctamente.")

def mostrar_citas():
    if len(citas) == 0:
        print("No hay citas guardadas.")
        return
    
    print("Citas guardadas:")
    for cita in citas:
        print(f"Identificación: {cita.identificacion}")
        print(f"Dia: {cita.dia}")
        print(f"Hora: {cita.hora}")
        print(f"Medico: {cita.medico.nombre}")
        print(f"Tipo cita: {cita.tipo_cita}")
        print(f"Descripcion: {cita.descripcion}")

        # Aquí puedes mostrar otros atributos de la cita según tu implementación
        print("---")


def validar_disponibilidad_horario(medico, dia, hora):
        for cita in citas:
            if cita.medico == medico and cita.dia == dia and cita.hora == hora:
                return False
        return True