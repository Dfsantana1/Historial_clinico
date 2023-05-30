class Horario:
    def __init__(self, dia, hora_inicio, hora_fin, cita_asignada=None, disponible=True):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.cita_asignada = cita_asignada
        self.disponible = disponible