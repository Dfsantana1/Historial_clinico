import tkinter as tk
from tkinter import ttk
import tkcalendar as tkcal 
import re
from ventanas.mostrar import mostrar_mensaje
from registros.registros import agregar_paciente,mostrar_paciente_historial
from registros.registroMedicos import obtener_medicos
from historial import HistorialClinico
from usuario.usuario import Usuario
import util.generic as utl
from datetime import datetime

class Cita:
    def __init__(self, identificacion, dia , hora , paciente, medico, tipo_cita, descripcion):
        self.identificacion = identificacion
        self.dia  = dia
        self.hora = hora
        self.paciente = paciente
        self.medico = medico
        self.tipo_cita = tipo_cita
        self.descripcion = descripcion


    citas_programadas = []  # Lista para almacenar las citas programadas

    
    def agendar_cita(identificacion, dia, hora , paciente, medico, tipo_cita, descripcion):
        # Validar que la fecha y hora sean válidas
        try:
            fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        except ValueError:
            print("La fecha y hora ingresadas no son válidas.")
            return

        # Crear una instancia de la clase Cita con los datos proporcionados
        cita = Cita(identificacion, fecha_hora, paciente, medico, tipo_cita, descripcion)

        # Agregar la cita a la lista de citas programadas
        Cita.citas_programadas.append(cita)

        print("Cita agendada exitosamente.")

# Ejemplo de uso
        Cita.agendar_cita("123456789", "2023-06-01 10:00", "Juan Perez", "Dr. Martinez", "Consulta", "Consulta general")

