import tkinter as tk
from tkinter import ttk
import re
from ventanas.mostrar import mostrar_mensaje
from registros.registroMedicos import agregar_medico
from registros.registros import obtener_registros_pacientes,obtener_paciente_por_id
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

        for paciente in lista_pacientes:
            print(paciente.nombre)
            print(paciente.identificacion)

        btn_agregar_historial = ttk.Button(ventana_doctor, text="Agregar Historial Clínico", command=self.agregar_historial)
        btn_agregar_historial.pack(pady=10, padx=20, fill=tk.X)

        btn_mostrar_historial = ttk.Button(ventana_doctor, text="Mostrar Historial Clínico", command=self.mostrar_historial)
        btn_mostrar_historial.pack(pady=10, padx=20, fill=tk.X)


        btn_buscar_paciente = ttk.Button(ventana_doctor, text="Buscar Paciente", command=self.buscar_paciente)
        btn_buscar_paciente.pack(pady=10, padx=20, fill=tk.X)

        btn_ver_horario = ttk.Button(ventana_doctor, text="Ver Horario", command=self.ver_horario)
        btn_ver_horario.pack(pady=10, padx=20, fill=tk.X)

        ventana_doctor.mainloop()
        
    def ver_horario(self):
        horario_medico = self.horario
        if horario_medico is not None:
            print("Horario del médico:")
            for horario in horario_medico:
                print("Día:", horario.dia)
                print("Hora de inicio:", horario.hora_inicio)
                print("Hora de fin:", horario.hora_fin)
                print("Disponibilidad:", horario.disponible)
                print("-------------------")
        else:
            print("No se encontró un médico con la identificación especificada.")
            

    def agregar_historial(self):
        ventana_agregar_historial = tk.Toplevel()
        ventana_agregar_historial.geometry("400x500")
        ventana_agregar_historial.configure(bg="#FFFFFF")

        label_id = tk.Label(ventana_agregar_historial, text="ID:")
        label_id.pack(pady=10)
        label_nombre = tk.Label(ventana_agregar_historial, text="Nombre:")
        label_nombre.pack(pady=10)

        entry_id = ttk.Entry(ventana_agregar_historial)
        entry_id.pack(pady=10)
        entry_nombre = ttk.Entry(ventana_agregar_historial)
        entry_nombre.pack(pady=10)

        btn_agregar = ttk.Button(ventana_agregar_historial, text="Agregar", command=lambda: self.guardar_historial(entry_id.get(), entry_nombre.get()))
        btn_agregar.pack(pady=10)

        ventana_agregar_historial.mainloop()
    def mostrar_historial(self):
        # Lógica para la acción de mostrar historial clínico
        pass


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
                btn_ver_historial = ttk.Button(frame, text="Ver Historial", command=lambda: self.ver_historial_paciente(paciente_encontrado))
                btn_ver_historial.grid(row=3, column=0, pady=10)

                btn_editar_historial = ttk.Button(frame, text="Editar Historial", command=lambda: self.editar_historial_paciente(paciente_encontrado))
                btn_editar_historial.grid(row=3, column=1, pady=10)

                btn_agregar_historial = ttk.Button(frame, text="Agregar Historial", command=lambda: self.agregar_historial_paciente(paciente_encontrado))
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
