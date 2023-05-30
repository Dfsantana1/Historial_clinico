class Usuario:
    def __init__(self, identificacion, nombre, genero, direccion, contraseña, usuario, rol, telefono, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.direccion = direccion
        self.contraseña = contraseña  # Hacer la contraseña privada
        self.usuario = usuario
        self.rol = rol
        self.telefono = telefono
        self.correo = correo
