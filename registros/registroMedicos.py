from ventanas.mostrar import mostrar_mensaje
from usuario.usuario import Usuario

registros_medicos = []

def agregar_medico(medico):
    for m in registros_medicos:
        if m.identificacion == medico.identificacion:
            mostrar_mensaje("Error", "El ID ya está en uso.")
            return
        if m.contraseña == medico.contraseña:
            mostrar_mensaje("Error", "La contraseña ya está en uso.")
            return

    registros_medicos.append(medico)
    mostrar_mensaje("Registro Exitoso", "El médico ha sido registrado correctamente.")

def obtener_medicos():
    return registros_medicos

def limpiar_registros():
    registros_medicos.clear()

def validar_credencialesM(usuario, contraseña):
    
    for medico in registros_medicos:
        if isinstance(medico, Usuario) and medico.usuario == usuario and medico.contraseña == contraseña:
            return medico
    return None

def consultar_horario_medico(identificacion):
    for medico in registros_medicos:
        if medico.identificacion == identificacion:
            return medico.horario
    return None


