from usuario.usuario import Usuario
from ventanas.mostrar import mostrar_mensaje
import tkinter as tk
from tkinter import ttk
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

def obtener_registros_pacientes():
    return registros_pacientes

def obtener_paciente_por_id(id_paciente):
    for paciente in registros_pacientes:
        if paciente.identificacion == id_paciente:
            return paciente
    return None

