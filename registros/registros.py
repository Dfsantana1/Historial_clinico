from usuario import Usuario
from ventanas.mostrar import mostrar_mensaje
registros_pacientes = []

def agregar_paciente(paciente):
    for p in registros_pacientes:
        if p.identificacion == paciente.identificacion:
            mostrar_mensaje("Error", "El ID ya está en uso.")
            return
        if p.contraseña == paciente.contraseña :
            mostrar_mensaje("Error", "La contraseña ya está en uso.")
            return
    
    registros_pacientes.append(paciente)
    mostrar_mensaje("Registro Exitoso", "El paciente ha sido registrado correctamente.")

def obtener_pacientes():
    return registros_pacientes

def limpiar_registros():
    registros_pacientes.clear()

def validar_credenciales(usuario, contraseña):
    
    for paciente in registros_pacientes:
        if isinstance(paciente, Usuario) and paciente.usuario == usuario and paciente.contraseña == contraseña:
            return paciente
    return None


def obtener_registros_pacientes():
    return registros_pacientes
