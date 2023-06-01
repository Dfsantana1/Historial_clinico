citas = []

def agregar_cita(cita):
    citas.append(cita)

def ver_mis_citas(id):
    mis_citas=[]
    for cita in citas:
        if cita.identificacion==id:
            mis_citas.append(cita)
    return mis_citas
