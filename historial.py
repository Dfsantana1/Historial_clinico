class HistorialClinico:
    def __init__(self , numero_documento, nombre, edad, sexo, altura, peso, telefono, email, direccion,
                 sintomas, fecha_inicio_sintomas, quejas, alergias, medicamentos, enfermedades_hereditarias,
                 enfermedades_actuales, fecha_consulta, id_historial=0):
        self.id_historial = id_historial
        self.numero_documento = numero_documento
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.sintomas = sintomas
        self.fecha_inicio_sintomas = fecha_inicio_sintomas
        self.quejas = quejas
        self.alergias = alergias
        self.medicamentos = medicamentos
        self.enfermedades_hereditarias = enfermedades_hereditarias
        self.enfermedades_actuales = enfermedades_actuales
        self.fecha_consulta = fecha_consulta

