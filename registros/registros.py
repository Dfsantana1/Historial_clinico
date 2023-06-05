from usuario.usuario import Usuario
from ventanas.mostrar import mostrar_mensaje
import tkinter as tk
from tkinter import ttk
from historial import HistorialClinico
import util.generic as utl
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
            registro.id_historial = len(paciente.historial_clinico) + 1
            paciente.historial_clinico.append(registro)
            mostrar_mensaje("Registro Exitoso","Registro Agregado Correctamente")
            return   # Indicar que se agregó el historial clínico correctamente
    
    mostrar_mensaje("Error","registro fallido") # Si no se encontró ningún paciente con el ID indicado


def mostrar_paciente_historial(id):

    def regresar():
        ventana.destroy()

    ventana = tk.Toplevel()
    ventana.title("Historial del Paciente")

    frame_principal = ttk.Frame(ventana)
    frame_principal.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Crear el lienzo de desplazamiento
    lienzo = tk.Canvas(frame_principal)
    lienzo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear el scrollbar vertical
    scrollbar = ttk.Scrollbar(frame_principal, orient=tk.VERTICAL, command=lienzo.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configurar el lienzo para desplazamiento
    lienzo.configure(yscrollcommand=scrollbar.set)

    # Crear un nuevo marco dentro del lienzo
    frame_historial = ttk.Frame(lienzo)
    lienzo.create_window((0, 0), window=frame_historial, anchor=tk.NW)

    for paciente in registros_pacientes:
        if paciente.identificacion == id:
            label_paciente = ttk.Label(frame_historial, text="Paciente: " + paciente.nombre)
            label_paciente.pack()

            label_identificacion = ttk.Label(frame_historial, text="Identificación: " + paciente.identificacion)
            label_identificacion.pack()

            label_historial = ttk.Label(frame_historial, text="Historial clínico:")
            label_historial.pack(pady=5)

            btn_regresar = tk.Button(ventana, text="Regresar", command=regresar, bg='#9E9CA1', fg='#2B282E')
            btn_regresar.pack(side="top", padx=20, pady=10, fill=tk.X)

            for registro in paciente.historial_clinico:
                label_fecha_consulta = ttk.Label(frame_historial, text="Fecha de Consulta: " + registro.fecha_consulta)
                label_fecha_consulta.pack()

                label_sintomas = ttk.Label(frame_historial, text="Síntomas: " + registro.sintomas)
                label_sintomas.pack()

                label_quejas = ttk.Label(frame_historial, text="Quejas: " + registro.quejas)
                label_quejas.pack()

                label_enfermedades_actuales = ttk.Label(frame_historial, text="Enfermedades Actuales: " + registro.enfermedades_actuales)
                label_enfermedades_actuales.pack()

                label_altura = ttk.Label(frame_historial, text="Altura: " + str(registro.altura))
                label_altura.pack()

                label_peso = ttk.Label(frame_historial, text="Peso: " + str(registro.peso))
                label_peso.pack()

                label_telefono = ttk.Label(frame_historial, text="Teléfono: " + registro.telefono)
                label_telefono.pack()

                label_email = ttk.Label(frame_historial, text="Email: " + registro.email)
                label_email.pack()

                label_direccion = ttk.Label(frame_historial, text="Dirección: " + registro.direccion)
                label_direccion.pack()

                label_alergias = ttk.Label(frame_historial, text="Alergias: " + registro.alergias)
                label_alergias.pack()

                label_medicamentos = ttk.Label(frame_historial, text="Medicamentos: " + registro.medicamentos)
                label_medicamentos.pack()

                label_enfermedades_hereditarias = ttk.Label(frame_historial, text="Enfermedades Hereditarias: " + registro.enfermedades_hereditarias)
                label_enfermedades_hereditarias.pack()

                ttk.Separator(frame_historial, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)

            break

    else:
        label_no_encontrado = ttk.Label(frame_historial, text="No se encontró ningún paciente con el ID indicado: " + id)
        label_no_encontrado.pack()

    # Configurar el desplazamiento del lienzo
    frame_historial.update_idletasks()
    lienzo.configure(scrollregion=lienzo.bbox("all"))

    ventana.mainloop()

def editar_paciente_historial(paciente1, id_historial):
    ventana = tk.Toplevel()
    ventana.title("Historial del Paciente")
    ventana.config(bg='#CBDEF6')
    ventana.resizable(width=0, height=0)
    utl.centrar_ventana(ventana, 600, 700)

    logo = utl.leer_imagen("./imagenes/logo.png", (200, 400))
    frame_principal = tk.Frame(ventana, bg='#CBDEF6')
    frame_principal.pack(fill=tk.BOTH, expand=True)

    frame_logo = tk.Frame(frame_principal, bg='#CBDEF6')
    frame_logo.pack(side="left", padx=10, pady=10)

    label = tk.Label(frame_logo, image=logo, bg='#CBDEF6')
    label.pack(fill=tk.BOTH, expand=True)

    frame_form = tk.Frame(frame_principal, bg='#CBDEF6')
    frame_form.pack(side="right", padx=5, pady=5, fill=tk.BOTH, expand=True)

    title = tk.Label(frame_form, text="Historial del Paciente", font=('Times', 20), fg="#3176EB", bg='#CBDEF6', pady=10)
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

    # Obtener información existente del registro
    for paciente in registros_pacientes:
        if paciente.identificacion == paciente1:
            for registro in paciente.historial_clinico:
                if id_historial == registro.id_historial:
                    # Rellenar los campos de entrada con la información existente
                    campos[0].insert(tk.END, paciente1)
                    campos[1].insert(tk.END, paciente.nombre)
                    campos[2].insert(tk.END, registro.edad)
                    campos[3].insert(tk.END, registro.sexo)
                    campos[4].insert(tk.END, registro.altura)
                    campos[5].insert(tk.END, registro.peso)
                    campos[6].insert(tk.END, registro.telefono)
                    campos[7].insert(tk.END, registro.email)
                    campos[8].insert(tk.END, registro.direccion)
                    campos[9].insert(tk.END, registro.sintomas)
                    campos[10].insert(tk.END, registro.fecha_inicio_sintomas)
                    campos[11].insert(tk.END, registro.quejas)
                    campos[12].insert(tk.END, registro.alergias)
                    campos[13].insert(tk.END, registro.medicamentos)
                    campos[14].insert(tk.END, registro.enfermedades_hereditarias)
                    campos[15].insert(tk.END, registro.enfermedades_actuales)
                    campos[16].insert(tk.END, registro.fecha_consulta)
                    break
                
    for campo in campos[:4]:
        campo.configure(state='readonly')

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    def regresar():
        ventana.destroy()

    def guardar_registro():
        datos = [campo.get() for campo in campos]

        # Realizar validaciones
        if any(not dato for dato in datos):
            mostrar_mensaje("Error", "Todos los campos son requeridos.")
            return

        # Resto de las validaciones...

        # Crear instancia de HistorialClinico
        historial = HistorialClinico(*datos)

        for paciente in registros_pacientes:
            if paciente.identificacion == paciente1:
                for indice, registro in enumerate(paciente.historial_clinico):
                    if id_historial == registro.id_historial:
                        paciente.historial_clinico[indice] = historial
                        mostrar_mensaje("Registro Actualizado", "El historial ha sido actualizado exitosamente.")
                        ventana.destroy()
                        break
                else:
                    mostrar_mensaje("Error", "No se encontró el historial con el ID proporcionado.")
                break
        else:
            mostrar_mensaje("Error", "No se encontró el paciente con la identificación proporcionada.")

    btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_registro, bg='#9E9CA1', fg='#2B282E')
    btn_guardar.pack(side="top", padx=20, pady=10, fill=tk.X)

    btn_regresar = tk.Button(ventana, text="Regresar", command=regresar, bg='#9E9CA1', fg='#2B282E')
    btn_regresar.pack(side="top", padx=20, pady=10, fill=tk.X)

    ventana.mainloop()

def obtener_registros_pacientes():
    return registros_pacientes

def obtener_paciente_por_id(id_paciente):
    for paciente in registros_pacientes:
        if paciente.identificacion == id_paciente:
            return paciente
    return None

