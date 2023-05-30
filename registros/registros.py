from usuario.usuario import Usuario
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


def agregar_historial(id, registro):
    for paciente in registros_pacientes:
        if paciente.identificacion == id:
            paciente.historial_clinico.append(registro)
            print("registro exitoso")
            return   # Indicar que se agregó el historial clínico correctamente
    
    print("registro fallido") # Si no se encontró ningún paciente con el ID indicado


def mostrar_paciente_historial(id):
    for paciente in registros_pacientes:
        if paciente.identificacion == id:
            print("Paciente:", paciente.nombre)
            print(paciente.identificacion)
            print("Historial clínico:")
            for registro in paciente.historial_clinico:
                print("Fecha de Consulta:", registro.fecha_consulta)
                print("Síntomas:", registro.sintomas)
                print("Quejas:", registro.quejas)
                print("Enfermedades Actuales:", registro.enfermedades_actuales)
                print("---------------")
            print("---------------")
            return  # Salir de la función después de encontrar el paciente con el ID deseado
    
    # Si no se encuentra ningún paciente con el ID indicado
    print("No se encontró ningún paciente con el ID indicado:", id)


def obtener_registros_pacientes():
    return registros_pacientes

def obtener_paciente_por_id(id_paciente):
    for paciente in registros_pacientes:
        if paciente.identificacion == id_paciente:
            return paciente
    return None

