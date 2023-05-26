import tkinter as tk
from ventanas.mostrar import mostrar_mensaje
from usuario import Usuario
from doctor import Medico
from paciente import Paciente
from registros.registros import validar_credenciales
from registros.registroMedicos import validar_credencialesM,agregar_medico

class Login:
    def __init__(self):
        self.ventana_login = tk.Tk()
        self.ventana_login.title("Iniciar sesión")

        lbl_usuario = tk.Label(self.ventana_login, text="Usuario:")
        lbl_usuario.grid(row=0, column=0)
        self.entry_usuario = tk.Entry(self.ventana_login)
        self.entry_usuario.grid(row=0, column=1)

        lbl_contraseña = tk.Label(self.ventana_login, text="Contraseña:")
        lbl_contraseña.grid(row=1, column=0)
        self.entry_contraseña = tk.Entry(self.ventana_login, show="*")
        self.entry_contraseña.grid(row=1, column=1)

        btn_iniciar_sesion = tk.Button(self.ventana_login, text="Iniciar sesión", command=self.iniciar_sesion)
        btn_iniciar_sesion.grid(row=2, column=0, columnspan=2)

        btn_registro_paciente = tk.Button(self.ventana_login, text="Registro de Paciente", command=Paciente.registro_paciente)
        btn_registro_paciente.grid(row=3, column=0, columnspan=2)

        btn_registro_medico = tk.Button(self.ventana_login, text="Registro de Médico", command=Medico.registro_medico)
        btn_registro_medico.grid(row=4, column=0, columnspan=2)

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
