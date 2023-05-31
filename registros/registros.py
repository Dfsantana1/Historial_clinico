from usuario.usuario import Usuario
from ventanas.mostrar import mostrar_mensaje
import tkinter as tk
from tkinter import ttk
from historial import HistorialClinico
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
    #mostrar_mensaje("Registro Exitoso", "El paciente ha sido registrado correctamente.")

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
            print(registro.id_historial)
            registro.id_historial = len(paciente.historial_clinico) + 1
            paciente.historial_clinico.append(registro)
            print("registro exitoso")
            print(registro.id_historial)
            return   # Indicar que se agregó el historial clínico correctamente
    
    print("registro fallido") # Si no se encontró ningún paciente con el ID indicado


def mostrar_paciente_historial(id):
    ventana = tk.Toplevel()
    ventana.title("Historial del Paciente")

    frame_historial = ttk.Frame(ventana)
    frame_historial.pack(padx=10, pady=10)

    for paciente in registros_pacientes:
        if paciente.identificacion == id:
            label_paciente = ttk.Label(frame_historial, text="Paciente: " + paciente.nombre)
            label_paciente.pack()

            label_identificacion = ttk.Label(frame_historial, text="Identificación: " + paciente.identificacion)
            label_identificacion.pack()

            label_historial = ttk.Label(frame_historial, text="Historial clínico:")
            label_historial.pack(pady=5)

            for registro in paciente.historial_clinico:
                label_fecha_consulta = ttk.Label(frame_historial, text="Fecha de Consulta: " + registro.fecha_consulta)
                label_fecha_consulta.pack()

                label_sintomas = ttk.Label(frame_historial, text="Síntomas: " + registro.sintomas)
                label_sintomas.pack()

                label_quejas = ttk.Label(frame_historial, text="Quejas: " + registro.quejas)
                label_quejas.pack()

                label_enfermedades = ttk.Label(frame_historial, text="Enfermedades Actuales: " + registro.enfermedades_actuales)
                label_enfermedades.pack()

                ttk.Separator(frame_historial, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)

            break
    
    else:
        label_no_encontrado = ttk.Label(frame_historial, text="No se encontró ningún paciente con el ID indicado: " + id)
        label_no_encontrado.pack()

    ventana.mainloop()

def editar_paciente_historial(paciente1, id_historial):
    ventana = tk.Toplevel()
    ventana.title("Historial del Paciente")

    frame_historial = ttk.Frame(ventana)
    frame_historial.pack(padx=10, pady=10)

    for paciente in registros_pacientes:
        if paciente.identificacion == paciente1:
            for indice, registro in enumerate(paciente.historial_clinico):
                if id_historial == registro.id_historial:
                    #numero_documento = input("Ingrese el número de documento: ")
                    #nombre = input("Ingrese el nombre: ")
                    #edad = int(input("Ingrese la edad: "))
                    #sexo = input("Ingrese el sexo: ")
                    altura = int(input("Ingrese la altura: "))
                    peso = float(input("Ingrese el peso: "))
                    telefono = input("Ingrese el número de teléfono: ")
                    email = input("Ingrese el correo electrónico: ")
                    direccion = input("Ingrese la dirección: ")
                    sintomas = input("Ingrese los síntomas: ")
                    fecha_inicio_sintomas = input("Ingrese la fecha de inicio de los síntomas (YYYY-MM-DD): ")
                    quejas = input("Ingrese las quejas: ")
                    alergias = input("Ingrese las alergias: ")
                    medicamentos = input("Ingrese los medicamentos: ")
                    enfermedades_hereditarias = input("Ingrese las enfermedades hereditarias: ")
                    enfermedades_actuales = input("Ingrese las enfermedades actuales: ")
                    fecha_consulta = input("Ingrese la fecha de consulta (YYYY-MM-DD): ")

                    historial = HistorialClinico(
                        #numero_documento=numero_documento,
                        #nombre=nombre,
                        numero_documento=registro.numero_documento,
                        nombre=registro.nombre,
                        edad=registro.edad,
                        sexo=registro.sexo,
                        altura=altura,
                        peso=peso,
                        telefono=telefono,
                        email=email,
                        direccion=direccion,
                        sintomas=sintomas,
                        fecha_inicio_sintomas=fecha_inicio_sintomas,
                        quejas=quejas,
                        alergias=alergias,
                        medicamentos=medicamentos,
                        enfermedades_hereditarias=enfermedades_hereditarias,
                        enfermedades_actuales=enfermedades_actuales,
                        fecha_consulta=fecha_consulta
                    )
                    paciente.historial_clinico[indice] = historial
                    print("Registro actualizado")
                    break
            else:
                print("No se encontró el historial con el ID proporcionado")
            break
    else:
        print("No se encontró el paciente con la identificación proporcionada")

'''
def editar_paciente_historial(paciente1, id_historial):
    for paciente in registros_pacientes:
        if paciente.identificacion == paciente1:
            for indice, registro in enumerate(paciente.historial_clinico):
                if id_historial == registro.id_historial:
                    historial = HistorialClinico(
                        numero_documento="1",
                        nombre="Juan Pérez",
                        edad=35,
                        sexo="Hombre",
                        altura=175,
                        peso=70,
                        telefono="1234567890",
                        email="juan@example.com",
                        direccion="Calle Principal 123",
                        sintomas="Dolor de cabeza, fiebre",
                        fecha_inicio_sintomas="2023-05-15",
                        quejas="Malestar general",
                        alergias="Ninguna",
                        medicamentos="Paracetamol",
                        enfermedades_hereditarias="Diabetes",
                        enfermedades_actuales="pipi",
                        fecha_consulta="2023-05-20"
                    )
                    paciente.historial_clinico[indice] = historial
                    print("Registro actualizado")
                    break
            else:
                print("No se encontró el historial con el ID proporcionado")
            break
    else:
        print("No se encontró el paciente con la identificación proporcionada")
'''

def obtener_registros_pacientes():
    return registros_pacientes

def obtener_paciente_por_id(id_paciente):
    for paciente in registros_pacientes:
        if paciente.identificacion == id_paciente:
            return paciente
    return None

