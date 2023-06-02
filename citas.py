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



    




