from ventanas.mostrar import mostrar_mensaje
import tkinter as tk
import tkinter.ttk as ttk

citas = []

def ver_mis_citas(id):
    mis_citas=[]
    for cita in citas:
        if cita.identificacion==id:
            mis_citas.append(cita)
    return mis_citas


def guardar_cita(cita):
    citas.append(cita)
    mostrar_mensaje("Registro Exitoso", "La cita ha sido agendada correctamente.")



def mostrar_citas():
    ventana = tk.Toplevel()
    ventana.title("Mostrar Citas")

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
    frame_citas = ttk.Frame(lienzo)
    lienzo.create_window((0, 0), window=frame_citas, anchor=tk.NW)

    if len(citas) == 0:
        label_no_citas = ttk.Label(frame_citas, text="No hay citas guardadas.")
        label_no_citas.pack()
    else:
        for cita in citas:
            label_identificacion = ttk.Label(frame_citas, text="Identificación: " + cita.identificacion)
            label_identificacion.pack()

            label_dia = ttk.Label(frame_citas, text="Día: " + cita.dia)
            label_dia.pack()

            label_hora = ttk.Label(frame_citas, text="Hora: " + cita.hora)
            label_hora.pack()

            label_medico = ttk.Label(frame_citas, text="Médico: " + cita.medico.nombre)
            label_medico.pack()

            label_tipo_cita = ttk.Label(frame_citas, text="Tipo cita: " + cita.tipo_cita)
            label_tipo_cita.pack()

            label_descripcion = ttk.Label(frame_citas, text="Descripción: " + cita.descripcion)
            label_descripcion.pack()

            ttk.Separator(frame_citas, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)


    frame_citas.update_idletasks()
    lienzo.configure(scrollregion=lienzo.bbox("all"))

    ventana.mainloop()


def mostrar_mis_citas(id):
    ventana = tk.Toplevel()
    ventana.title("Mostrar Mis Citas")

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
    frame_citas = ttk.Frame(lienzo)
    lienzo.create_window((0, 0), window=frame_citas, anchor=tk.NW)

    if len(citas) == 0:
        label_no_citas = ttk.Label(frame_citas, text="No hay citas guardadas.")
        label_no_citas.pack()
    else:
        for cita in citas:
            if cita.identificacion == id:
                label_identificacion = ttk.Label(frame_citas, text="Identificación: " + cita.identificacion)
                label_identificacion.pack()

                label_dia = ttk.Label(frame_citas, text="Día: " + cita.dia)
                label_dia.pack()

                label_hora = ttk.Label(frame_citas, text="Hora: " + cita.hora)
                label_hora.pack()

                label_medico = ttk.Label(frame_citas, text="Médico: " + cita.medico.nombre)
                label_medico.pack()

                label_tipo_cita = ttk.Label(frame_citas, text="Tipo cita: " + cita.tipo_cita)
                label_tipo_cita.pack()

                label_descripcion = ttk.Label(frame_citas, text="Descripción: " + cita.descripcion)
                label_descripcion.pack()

                ttk.Separator(frame_citas, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)

                btn_eliminar = ttk.Button(frame_citas, text="Eliminar", command=lambda cita=cita: eliminar_cita(cita))
                btn_eliminar.pack()

        # Configurar el desplazamiento del lienzo
        frame_citas.update_idletasks()
        lienzo.configure(scrollregion=lienzo.bbox("all"))

        ventana.mainloop()

def eliminar_cita(cita):
    ventana = tk.Toplevel()
    # Eliminar la cita de la lista de citas
    citas.remove(cita)

    frame_principal = ttk.Frame(ventana)
    lienzo = tk.Canvas(frame_principal)
    frame_citas = ttk.Frame(lienzo)

    # Destruir todos los widgets dentro del frame de la cita
    for widget in frame_citas.winfo_children():
        widget.destroy()

    # Volver a mostrar las citas restantes
    ventana.destroy()
    mostrar_mis_citas(id)

def validar_disponibilidad_horario(medico, dia, hora):
        for cita in citas:
            if cita.medico == medico and cita.dia == dia and cita.hora == hora:
                return False
        return True