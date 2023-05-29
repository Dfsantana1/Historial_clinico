import tkinter as tk
from ventanas.mostrar import mostrar_mensaje
from usuario import Usuario
from doctor import Medico
from paciente import Paciente
from registros.registros import validar_credenciales
from registros.registroMedicos import validar_credencialesM, agregar_medico
import util.generic as utl

class Login:
    def __init__(self):
        self.ventana_login = tk.Tk()
        self.ventana_login.title("Iniciar sesión")
        self.ventana_login.configure(bg="#CBDEF6")
        self.ventana_login.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana_login, 600, 420)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 400))
        frame_principal = tk.Frame(self.ventana_login, bg='#CBDEF6')
        frame_principal.pack(fill=tk.BOTH, expand=False)

        frame_logo = tk.Frame(frame_principal, bg='#CBDEF6')
        frame_logo.pack(side="left", padx=10, pady=10)

        label = tk.Label(frame_logo, image=logo, bg='#CBDEF6')
        label.pack(fill=tk.BOTH, expand=True)

        frame_form = tk.Frame(frame_principal, bg='#CBDEF6')
        frame_form.pack(side="right", padx=5, pady=5, fill=tk.BOTH, expand=True)

        title = tk.Label(frame_form, text="Iniciar sesión", font=('Times', 20), fg="#3176EB", bg='#CBDEF6', pady=40)
        title.pack(fill=tk.X)

        form = tk.Frame(frame_form, bg='#CBDEF6')
        form.pack(fill=tk.BOTH, expand=True)

        lbl_usuario = tk.Label(form, text="Usuario:", bg="#CBDEF6", fg="#094CA2")
        lbl_usuario.pack(anchor="center", padx=10, pady=5)
        self.entry_usuario = tk.Entry(form)
        self.entry_usuario.pack(anchor="center", padx=10)

        lbl_contraseña = tk.Label(form, text="Contraseña:", bg="#CBDEF6", fg="#094CA2")
        lbl_contraseña.pack(anchor="center", padx=10, pady=5)
        self.entry_contraseña = tk.Entry(form, show="*")
        self.entry_contraseña.pack(anchor="center", padx=10)

        btn_iniciar_sesion = tk.Button(form, text="Iniciar sesión", command=self.iniciar_sesion, bg="#9E9CA1", fg="#2B282E", relief=tk.RAISED, bd=3, font=("times", 8, "bold"), padx=10, pady=5)
        btn_iniciar_sesion.pack(anchor="center", padx=10, pady=5)

        btn_registro_paciente = tk.Button(form, text="Registro de Paciente", command=Paciente.registro_paciente, bg="#9E9CA1", fg="#2B282E", relief=tk.RAISED, bd=3, font=("times", 8, "bold"), padx=7, pady=5)
        btn_registro_paciente.pack(anchor="center", padx=10, pady=5)

        btn_registro_medico = tk.Button(form, text="Registro de Médico", command=Medico.registro_medico, bg="#9E9CA1", fg="#2B282E", relief=tk.RAISED, bd=3, font=("times", 8, "bold"), padx=10, pady=5)
        btn_registro_medico.pack(anchor="center", padx=10, pady=5)

        self.ventana_login.mainloop()

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()

        medico = Medico("12", "12", "12", "12", "1234", "usuario", "12", "12", "mk")
        agregar_medico(medico)

        medico_valido = validar_credencialesM(usuario, contraseña)
        if isinstance(medico_valido, Medico):
            medico_valido.iniciar_ventana()

        paciente_valido = validar_credenciales(usuario, contraseña)
        if isinstance(paciente_valido, Paciente):
            paciente_valido.iniciar_ventana()
        else:
            mostrar_mensaje("Error", "Credenciales inválidas. Por favor, inténtalo nuevamente.")

        # Limpia los campos de entrada
        self.entry_usuario.delete(0, tk.END)
        self.entry_contraseña.delete(0, tk.END)

# Código de ejecución principal
if __name__ == "__main__":
    login = Login()

