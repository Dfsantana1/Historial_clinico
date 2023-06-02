import tkinter as tk
from tkinter import ttk
import tkcalendar as tkcal 
from tkcalendar import Calendar
import re
from ventanas.mostrar import mostrar_mensaje
from registros.registros import agregar_paciente,mostrar_paciente_historial
from registros.registroMedicos import obtener_medicos,validar_disponibilidad_horario
from historial import HistorialClinico
from usuario.usuario import Usuario
import util.generic as utl
from datetime import datetime
from registros.registroCitas import guardar_cita, mostrar_citas
from citas import Cita


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
        btn_ver_horario = ttk.Button(ventana_paciente, text="Ver Medicos ", command=self.ver_medicos)
        btn_ver_horario.pack(pady=10, padx=20, fill=tk.X)
        btn_mostrar_historial = ttk.Button(ventana_paciente, text="Ver Mi Historial", command=lambda: mostrar_paciente_historial(self.identificacion))
        btn_mostrar_historial.pack(pady=10, padx=20, fill=tk.X)




        # Agrega aquí los elementos y la lógica para la ventana del médico

        ventana_paciente.mainloop()



    



    def agendar_cita(self, medico):
        ventana_agendar = tk.Toplevel()
        ventana_agendar.title("Agendamiento de citas")
        ventana_agendar.geometry("600x300")  # Ajusta el tamaño de la ventana según tus necesidades


        label_dia = ttk.Label(ventana_agendar, text="Día:")
        label_dia.pack()

        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        selected_dia = ttk.Combobox(ventana_agendar, values=dias_semana)
        selected_dia.pack()

        label_hora = ttk.Label(ventana_agendar, text="Hora (Formato HH:MM):")
        label_hora.pack()

        entry_hora = ttk.Entry(ventana_agendar)
        entry_hora.pack()

        label_tipo_cita = ttk.Label(ventana_agendar,  text="Tipo cita:")
        label_tipo_cita.pack()

        entry_tipo_cita = ttk.Entry(ventana_agendar)
        entry_tipo_cita.pack()

        label_descripcion = ttk.Label(ventana_agendar,  text=" Descripcion :")
        label_descripcion.pack()

        entry_descripcion = ttk.Entry(ventana_agendar)
        entry_descripcion.pack() 

        btn_agendar = ttk.Button(ventana_agendar, text="Agendar", command=lambda: self.guardar_cita( selected_dia.get(), entry_hora.get(),medico,  entry_tipo_cita.get(), entry_descripcion.get()))
        btn_agendar.pack()

        ventana_agendar.mainloop()

    def guardar_cita(self, dia, hora, medico, tipo_cita, descripcion):
        # Lógica para validar los datos ingresados y guardar la cita en el sistema de agendamiento
        if validar_disponibilidad_horario(medico.identificacion, dia, hora):
            nueva_cita = Cita(self.identificacion, dia, hora, self.nombre, medico, tipo_cita, descripcion)
            guardar_cita(nueva_cita)
            mostrar_citas()
        else:
            print("Horario no disponible")
    

    def ver_medicos(self):
        ventana = tk.Toplevel()  # Crear una nueva ventana (pestaña)

        medicos = obtener_medicos()

        for medico in medicos:
            nombre = medico.nombre
            especialidad = medico.especialidad

            # Crear un frame para agrupar el nombre, la especialidad y los botones
            frame_medico = ttk.Frame(ventana)
            frame_medico.pack(pady=10)

            # Etiqueta para mostrar el nombre y la especialidad en la misma línea
            label_nombre_especialidad = ttk.Label(frame_medico, text=f"{nombre} - {especialidad}")
            label_nombre_especialidad.pack(side=tk.LEFT, padx=5)

            # Botón "Ver Horario"
            btn_ver_horario = ttk.Button(frame_medico, text="Ver Horario", command=medico.ver_horario)
            btn_ver_horario.pack(side=tk.LEFT, padx=5)

            # Botón "Agendar Cita"
            btn_agendar_cita = ttk.Button(frame_medico, text="Agendar Cita", command=lambda medico=medico: self.agendar_cita(medico))
            btn_agendar_cita.pack(side=tk.LEFT, padx=5)

        ventana.mainloop()

    def ventana_agendar_cita(self, medico):
        ventana_agendar = tk.Toplevel()  # Crear una nueva ventana para agendar la cita

        # Lógica para crear los elementos necesarios para agendar la cita, como etiquetas, campos de entrada, botones, etc.

        # Lógica para guardar la cita en el sistema de agendamiento (puedes utilizar la función "guardar_cita" mencionada anteriormente)

        ventana_agendar.mainloop()



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

