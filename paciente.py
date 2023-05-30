import tkinter as tk
from tkinter import ttk
import tkcalendar as tkcal 
import re
from ventanas.mostrar import mostrar_mensaje
from registros.registros import agregar_paciente,mostrar_paciente_historial
from historial import HistorialClinico
from usuario import Usuario
import util.generic as utl


class Paciente(Usuario):
    def __init__(self, identificacion, nombre, genero, direccion, contraseña, usuario, telefono, correo, fecha_nacimiento):
        super().__init__(identificacion, nombre, genero, direccion, contraseña, usuario, "Paciente", telefono, correo)
        self.fecha_nacimiento = fecha_nacimiento 
        self.historial_clinico =[]




    def agregar_registro_historial(self, registro):
        self.historial_clinico.agregar_registro(registro)

    def iniciar_ventana(self):
        ventana_paciente = tk.Tk()
        ventana_paciente.title("Ventana del Paciente")
        ventana_paciente.geometry("1600x900")
        ventana_paciente.configure(bg="#CBDEF6")

        mensaje_bienvenida = tk.Label(ventana_paciente, text=f"Bienvenido Paciente", font=("Arial", 16), bg="#F0F8FF", fg="#000000")
        mensaje_bienvenida.pack(pady=10)

        # Botones
        btn_mostrar_historial = ttk.Button(ventana_paciente, text="Mostrar Historial Clínico", command=mostrar_paciente_historial(self.identificacion))
        btn_mostrar_historial.pack(pady=10, padx=20, fill=tk.X)

        btn_ver_horario = ttk.Button(ventana_paciente, text="Ver Horario", command=Paciente.ver_horario)
        btn_ver_horario.pack(pady=10, padx=20, fill=tk.X)



        # Agrega aquí los elementos y la lógica para la ventana del médico

        ventana_paciente.mainloop()

        
    @staticmethod



    def ver_horario(self):
        # Lógica para la acción de ver horario
        pass


    def registro_paciente():
        ventana_registro_paciente = tk.Toplevel()
        ventana_registro_paciente.title("Registro de Paciente")
        ventana_registro_paciente.config(bg='#CBDEF6')
        ventana_registro_paciente.resizable(width=0, height=0)
        utl.centrar_ventana(ventana_registro_paciente, 600, 700)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 400))
        frame_principal = tk.Frame(ventana_registro_paciente, bg='#CBDEF6')
        frame_principal.pack(fill=tk.BOTH, expand=False)

        frame_logo = tk.Frame(frame_principal, bg='#CBDEF6')
        frame_logo.pack(side="left", padx=10, pady=10)

        label = tk.Label(frame_logo, image=logo, bg='#CBDEF6')
        label.pack(fill=tk.BOTH, expand=True)

        frame_form = tk.Frame(frame_principal, bg='#CBDEF6')
        frame_form.pack(side="right", padx=5, pady=5, fill=tk.BOTH, expand=True)

        title = tk.Label(frame_form, text="Registro de Paciente", font=('Times', 20), fg="#3176EB", bg='#CBDEF6', pady=10)
        title.pack(fill=tk.X)

        form = tk.Frame(frame_form, bg='#CBDEF6')
        form.pack(fill=tk.BOTH, expand=True)

        etiquetas = ["Identificación", "Nombre", "Género", "Dirección", "Contraseña","Confirmar Contraseña", "Usuario",
                     "Teléfono", "Correo electrónico", "Fecha de Nacimiento"]
        campos = []

        for i, etiqueta in enumerate(etiquetas):
            lbl = tk.Label(form, text=etiqueta, font=('Times', 10), fg="#0B4EC0", bg='#CBDEF6', anchor="w")
            lbl.pack(side="top", padx=5, pady=2, fill=tk.X)

            if etiqueta == "Género":
                combo_genero = ttk.Combobox(form, values=["Masculino", "Femenino"])
                combo_genero.pack(side="top", padx=5, pady=2, anchor="w")
                campos.append(combo_genero)
            elif etiqueta == "Fecha de Nacimiento":
                fecha_entry = tkcal.DateEntry(form, date_pattern="dd/mm/yyyy")
                fecha_entry.pack(side="top", padx=2, pady=2, fill=tk.X)
                campos.append(fecha_entry)
            elif etiqueta == "Contraseña" or etiqueta == "Confirmar Contraseña":
                entry = ttk.Entry(form, show='*', width=1)  # Ajustar el ancho del campo de entrada
                entry.pack(side="top", padx=2, pady=2, fill=tk.X)
                campos.append(entry)
            else:
                entry = ttk.Entry(form, width=2)  # Ajustar el ancho del campo de entrada
                entry.pack(side="top", padx=2, pady=2, fill=tk.X)
                campos.append(entry)

        def regresar():
            ventana_registro_paciente.destroy()

        def guardar_registro():
            datos = [campo.get() for campo in campos]

            if any(not dato for dato in datos):
                mostrar_mensaje("Error", "Todos los campos son requeridos.")
                return

            if datos[4] != datos[5]:
                mostrar_mensaje("Error", "La contraseña y la confirmación de contraseña no coinciden.")
                return

            if not re.match(r"^[^@]+@[^@]+\.[^@]+$", datos[8]):
                mostrar_mensaje("Error", "El correo electrónico no es válido.")
                return

            if not datos[0].isdigit():
                mostrar_mensaje("Error", "La identificación debe ser un número.")
                return

            if len(datos[4]) < 8:
                mostrar_mensaje("Error", "La contraseña debe tener al menos 8 caracteres.")
                return

            if not datos[7].isdigit():
                mostrar_mensaje("Error", "El teléfono debe contener solo números.")
                return

            paciente = Paciente(*datos[:4], datos[4], datos[6], datos[7], datos[8], datos[9])
            agregar_paciente(paciente)
            paciente.contraseña
            ventana_registro_paciente.destroy()
                
        btn_guardar = tk.Button(ventana_registro_paciente, text="Guardar", command=guardar_registro, bg='#9E9CA1', fg='#2B282E')
        btn_guardar.pack(side="top", padx=20, pady=10, fill=tk.X)

        btn_regresar = tk.Button(ventana_registro_paciente, text="Regresar", command=regresar, bg='#9E9CA1', fg='#2B282E')
        btn_regresar.pack(side="top", padx=20, pady=10, fill=tk.X)


        ventana_registro_paciente.mainloop()

