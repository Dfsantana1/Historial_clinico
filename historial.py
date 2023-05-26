class HistorialClinico:
    def __init__(self, numero_documento, nombre, edad, sexo, altura, peso, telefono, email, direccion,
                 sintomas, fecha_inicio_sintomas, quejas, alergias, medicamentos, enfermedades_hereditarias,
                 enfermedades_actuales, fecha_consulta):
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

class HistorialClinicoMayoresHombres(HistorialClinico):
    def __init__(self, numero_documento, nombre, edad, altura, peso, telefono, email, direccion,
                 sintomas, fecha_inicio_sintomas, quejas, alergias, medicamentos, enfermedades_hereditarias,
                 enfermedades_actuales, fecha_consulta, enfermedades_transmision_sexual):
        super().__init__(numero_documento, nombre, edad, "Hombre", altura, peso, telefono, email, direccion,
                         sintomas, fecha_inicio_sintomas, quejas, alergias, medicamentos, enfermedades_hereditarias,
                         enfermedades_actuales, fecha_consulta)
        self.enfermedades_transmision_sexual = enfermedades_transmision_sexual

class HistorialClinicoMayoresMujeres(HistorialClinico):
    def __init__(self, numero_documento, nombre, edad, altura, peso, telefono, email, direccion,
                 sintomas, fecha_inicio_sintomas, quejas, alergias, medicamentos, enfermedades_hereditarias,
                 enfermedades_actuales, fecha_consulta, enfermedades_transmision_sexual, metodo_planificacion,
                 estado_embarazo):
        super().__init__(numero_documento, nombre, edad, "Mujer", altura, peso, telefono, email, direccion,
                         sintomas, fecha_inicio_sintomas, quejas, alergias, medicamentos, enfermedades_hereditarias,
                         enfermedades_actuales, fecha_consulta)
        self.enfermedades_transmision_sexual = enfermedades_transmision_sexual
        self.metodo_planificacion = metodo_planificacion
        self.estado_embarazo = estado_embarazo

class HistorialClinicoMenores(HistorialClinico):
    def __init__(self, numero_documento, nombre, edad, altura, peso, telefono, email, direccion,
                 sintomas, fecha_inicio_sintomas, quejas, alergias, medicamentos, enfermedades_hereditarias,
                 enfermedades_actuales, fecha_consulta):
        super().__init__(numero_documento, nombre, edad, "Menor", altura, peso, telefono, email, direccion,
                         sintomas, fecha_inicio_sintomas, quejas, alergias, medicamentos, enfermedades_hereditarias,
                         enfermedades_actuales, fecha_consulta)
