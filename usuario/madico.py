import tkinter as tk
from tkinter import ttk
import re
from historial import HistorialClinico
from ventanas.mostrar import mostrar_mensaje
from registros.registroMedicos import agregar_medico
from registros.registroCitas import mostrar_citas
from registros.registros import obtener_registros_pacientes,obtener_paciente_por_id,mostrar_paciente_historial, editar_paciente_historial,agregar_historial
from usuario.usuario import Usuario
import util.generic as utl
from horario import Horario

class Medico(Usuario):
    def __init__(self, identificacion, nombre, genero, direccion, contraseña, usuario, telefono, correo, especialidad):
        super().__init__(identificacion, nombre, genero, direccion, contraseña, usuario, "Medico", telefono, correo)
        self.especialidad = especialidad
        self.horario = []

        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        horas_disponibles = list(range(7, 13)) + list(range(14, 18))
# Rango de horas de 7 a 12 y de 14 a 17
        for dia in dias_semana:
            for hora in horas_disponibles:
                hora_inicio = f"{hora:02d}:00"  # Formato HH:MM
                hora_fin = f"{hora + 1:02d}:00"
                self.horario.append(Horario(dia, hora_inicio, hora_fin))

    def iniciar_ventana(self):
        ventana_doctor = tk.Tk()
        ventana_doctor.title("Ventana del Médico")
        ventana_doctor.geometry("1600x900")
        ventana_doctor.configure(bg="#CBDEF6")

        lista_pacientes = obtener_registros_pacientes()
        mensaje_bienvenida = tk.Label(ventana_doctor, text=f"Bienvenido Médico {self.nombre}", font=("Arial", 16), bg="#F0F8FF", fg="#000000")
        mensaje_bienvenida.pack(pady=10)

        


        btn_buscar_paciente = ttk.Button(ventana_doctor, text="Buscar Paciente", command=self.buscar_paciente)
        btn_buscar_paciente.pack(pady=10, padx=20, fill=tk.X)

        btn_ver_horario = ttk.Button(ventana_doctor, text="Ver Horario", command=self.ver_horario)
        btn_ver_horario.pack(pady=10, padx=20, fill=tk.X)

        btn_ver_horario = ttk.Button(ventana_doctor, text="Ver Citas", command=mostrar_citas)
        btn_ver_horario.pack(pady=10, padx=20, fill=tk.X)

        ventana_doctor.mainloop()
        
    
    def ver_horario(self):
        ventana = tk.Toplevel()
        ventana.title("Horari del Médico")
        ventana.geometry("600x300")  # Ajusta el tamaño de la ventana según tus necesidades

        horario_medico = self.horario

        if horario_medico is not None:
            frame_horario = ttk.Frame(ventana)
            frame_horario.pack(padx=10, pady=10)

            canvas = tk.Canvas(frame_horario, width=550)  # Ajusta el valor de width según tus necesidades
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar = ttk.Scrollbar(frame_horario, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            frame_horario_interior = ttk.Frame(canvas)
            canvas.create_window((0, 0), window=frame_horario_interior, anchor="nw")

            for horario in horario_medico:
                frame_dia = ttk.Frame(frame_horario_interior)
                frame_dia.pack(pady=5)

                label_dia = ttk.Label(frame_dia, text=f"Día: {horario.dia}")
                label_dia.pack(side=tk.LEFT)

                label_inicio = ttk.Label(frame_dia, text=f"Hora de inicio: {horario.hora_inicio}")
                label_inicio.pack(side=tk.LEFT, padx=10)

                label_fin = ttk.Label(frame_dia, text=f"Hora de fin: {horario.hora_fin}")
                label_fin.pack(side=tk.LEFT, padx=10)

                label_disponibilidad = ttk.Label(frame_dia, text=f"Disponibilidad: {'Disponible' if horario.disponible else 'No disponible'}")
                label_disponibilidad.pack(side=tk.LEFT, padx=10)

            canvas.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))

        else:
            mensaje_no_encontrado = ttk.Label(ventana, text="No se encontró un médico con la identificación especificada.")
            mensaje_no_encontrado.pack(pady=10)

        ventana.mainloop()


   
    def buscar_paciente(self):
        def buscar():
            id_paciente = entry_id.get()
            paciente_encontrado = obtener_paciente_por_id(id_paciente)
            if paciente_encontrado is not None:
                resultado = f"Paciente encontrado:\n"
                resultado += f"Nombre: {paciente_encontrado.nombre}\n"
                resultado += f"Género: {paciente_encontrado.genero}\n"
                resultado += f"Dirección: {paciente_encontrado.direccion}\n"
                resultado += f"Teléfono: {paciente_encontrado.telefono}\n"
                resultado += f"Correo: {paciente_encontrado.correo}\n"
                resultado += f"Fecha de nacimiento: {paciente_encontrado.fecha_nacimiento}\n"
                lbl_resultado.config(text=resultado)

                # Agregar botones
                btn_ver_historial = ttk.Button(frame, text="Ver Historial", command=lambda :mostrar_paciente_historial(paciente_encontrado.identificacion))
                btn_ver_historial.grid(row=3, column=0, pady=10)

                btn_editar_historial = ttk.Button(frame, text="Editar Historial", command=lambda :editar_paciente_historial(paciente_encontrado.identificacion,1))
                btn_editar_historial.grid(row=3, column=1, pady=10)

                btn_agregar_historial = ttk.Button(frame, text="Agregar Historial", command=lambda :self.agregar_historial1(paciente_encontrado))
                btn_agregar_historial.grid(row=3, column=2, pady=10)

            else:
                lbl_resultado.config(text="No se encontró ningún paciente con el ID proporcionado.")

        ventana_buscar_paciente = tk.Toplevel()
        ventana_buscar_paciente.title("Buscar Paciente")

        frame = ttk.Frame(ventana_buscar_paciente, padding=20)
        frame.pack()

        lbl_id = ttk.Label(frame, text="ID del Paciente:")
        lbl_id.grid(row=0, column=0, sticky="w")

        entry_id = ttk.Entry(frame)
        entry_id.grid(row=0, column=1)

        btn_buscar = ttk.Button(frame, text="Buscar", command=buscar)
        btn_buscar.grid(row=1, column=0, columnspan=2, pady=10)

        lbl_resultado = ttk.Label(frame, text="")
        lbl_resultado.grid(row=2, column=0, columnspan=2, pady=10)


    def agregar_historial1(self, usuario):
        ventana_registro_historial = tk.Toplevel()
        ventana_registro_historial.title("Registro de Historial Clínico")
        ventana_registro_historial.config(bg='#CBDEF6')
        ventana_registro_historial.resizable(width=0, height=0)
        utl.centrar_ventana(ventana_registro_historial, 600, 700)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 400))
        frame_principal = tk.Frame(ventana_registro_historial, bg='#CBDEF6')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        frame_logo = tk.Frame(frame_principal, bg='#CBDEF6')
        frame_logo.pack(side="left", padx=10, pady=10)

        label = tk.Label(frame_logo, image=logo, bg='#CBDEF6')
        label.pack(fill=tk.BOTH, expand=True)

        frame_form = tk.Frame(frame_principal, bg='#CBDEF6')
        frame_form.pack(side="right", padx=5, pady=5, fill=tk.BOTH, expand=True)

        title = tk.Label(frame_form, text="Registro de Historial Clínico", font=('Times', 20), fg="#3176EB", bg='#CBDEF6', pady=10)
        title.pack(fill=tk.X)

        canvas = tk.Canvas(frame_form, bg='#CBDEF6')
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame_form, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        form_frame = tk.Frame(canvas, bg='#CBDEF6')
        canvas.create_window((0, 0), window=form_frame, anchor="nw")

        etiquetas = ["Número de Documento", "Nombre", "Edad", "Sexo", "Altura", "Peso", "Teléfono", "Correo Electrónico",
                    "Dirección", "Síntomas", "Fecha de Inicio de Síntomas", "Quejas", "Alergias", "Medicamentos",
                    "Enfermedades Hereditarias", "Enfermedades Actuales", "Fecha de Consulta"]

        campos = []
        for i, etiqueta in enumerate(etiquetas):
            lbl = tk.Label(form_frame, text=etiqueta, font=('Times', 8), fg="#0B4EC0", bg='#CBDEF6', anchor="w")
            lbl.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = ttk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            campos.append(entry)

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        def regresar():
            ventana_registro_historial.destroy()

        def guardar_registro():
            datos = [campo.get() for campo in campos]

            # Realizar validaciones
            if any(not dato for dato in datos):
                mostrar_mensaje("Error", "Todos los campos son requeridos.")
                return

            # Resto de las validaciones...

            # Crear instancia de HistorialClinico
            H = HistorialClinico(*datos)

            agregar_historial(usuario.identificacion,H)

                        
            ventana_registro_historial.destroy()


            # Resto del código para guardar el registro
            # ...



        btn_guardar = tk.Button(ventana_registro_historial, text="Guardar", command=lambda: guardar_registro(), bg='#9E9CA1', fg='#2B282E')
        btn_guardar.pack(side="top", padx=20, pady=10, fill=tk.X)

        btn_regresar = tk.Button(ventana_registro_historial, text="Regresar", command=regresar, bg='#9E9CA1', fg='#2B282E')
        btn_regresar.pack(side="top", padx=20, pady=10, fill=tk.X)

        ventana_registro_historial.mainloop()


        
    def registro_medico():
        ventana_registro_medico = tk.Toplevel()
        ventana_registro_medico.title("Registro de Médico")
        ventana_registro_medico.config(bg='#CBDEF6')
        ventana_registro_medico.resizable(width=0, height=0)
        utl.centrar_ventana(ventana_registro_medico, 600, 700)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 400))
        frame_principal = tk.Frame(ventana_registro_medico, bg='#CBDEF6')
        frame_principal.pack(fill=tk.BOTH, expand=False)

        frame_logo = tk.Frame(frame_principal, bg='#CBDEF6')
        frame_logo.pack(side="left", padx=10, pady=10)

        label = tk.Label(frame_logo, image=logo, bg='#CBDEF6')
        label.pack(fill=tk.BOTH, expand=True)

        frame_form = tk.Frame(frame_principal, bg='#CBDEF6')
        frame_form.pack(side="right", padx=5, pady=5, fill=tk.BOTH, expand=True)

        title = tk.Label(frame_form, text="Registro de medico", font=('Times', 20), fg="#3176EB", bg='#CBDEF6', pady=10)
        title.pack(fill=tk.X)

        form = tk.Frame(frame_form, bg='#CBDEF6')
        form.pack(fill=tk.BOTH, expand=True)

        etiquetas = ["Identificación", "Nombre", "Género", "Dirección", "Contraseña", "Confirmar Contraseña", "Usuario",
                     "Teléfono", "Correo electrónico", "Especialidad"]
        campos = []

        for i, etiqueta in enumerate(etiquetas):
            lbl = tk.Label(form, text=etiqueta, font=('Times', 8), fg="#0B4EC0", bg='#CBDEF6', anchor="w")
            lbl.pack(side="top", padx=5, pady=5, fill=tk.X)

            if etiqueta == "Género":
                combo_genero = ttk.Combobox(form, values=["Masculino", "Femenino"])
                combo_genero.pack(side="top", padx=5, pady=2, anchor="w")
                campos.append(combo_genero)
            elif etiqueta == "Contraseña" or etiqueta == "Confirmar Contraseña":
                entry = ttk.Entry(form, show='*', width=1)  # Ajustar el ancho del campo de entrada
                entry.pack(side="top", padx=2, pady=2, fill=tk.X)
                campos.append(entry)
            else:
                entry = ttk.Entry(form, width=2)  # Ajustar el ancho del campo de entrada
                entry.pack(side="top", padx=2, pady=2, fill=tk.X)
                campos.append(entry)

        def regresar():
            ventana_registro_medico.destroy()


        def guardar_registro():
            datos = [campo.get() for campo in campos]

            # Realizar validaciones
            if any(not dato for dato in datos):
                mostrar_mensaje("Error", "Todos los campos son requeridos.")
                return

            if datos[4] != datos[5]:
                mostrar_mensaje("Error", "La contraseña y la confirmación de contraseña no coinciden.")
                return

            if not re.match(r"[^@]+@[^@]+\.[^@]+", datos[8]):
                mostrar_mensaje("Error", "El correo electrónico no es válido.")
                return

            # Validación de identificación como número
            if not datos[0].isdigit():
                mostrar_mensaje("Error", "La identificación debe ser un número.")
                return

            # Validación de longitud mínima de contraseña
            if len(datos[4]) < 8:
                mostrar_mensaje("Error", "La contraseña debe tener al menos 8 caracteres.")
                return

            # Validación de teléfono como número
            if not datos[7].isdigit():
                mostrar_mensaje("Error", "El teléfono debe contener solo números.")
                return

            # Resto del código para guardar el registro
            medico = Medico(*datos[:4], datos[4], datos[6], datos[7], datos[8], datos[9])
            agregar_medico(medico)
            ventana_registro_medico.destroy()

        btn_guardar = tk.Button(ventana_registro_medico, text="Guardar", command=guardar_registro, bg='#9E9CA1', fg='#2B282E')
        btn_guardar.pack(side="top", padx=20, pady=10, fill=tk.X)

        btn_regresar = tk.Button(ventana_registro_medico, text="Regresar", command=regresar, bg='#9E9CA1', fg='#2B282E')
        btn_regresar.pack(side="top", padx=20, pady=10, fill=tk.X)

        ventana_registro_medico.mainloop()
