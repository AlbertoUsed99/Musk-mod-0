from datetime import datetime

class Slot:
    """
    Representa un slot de tiempo en el aeropuerto.
    Un slot puede estar ocupado por un vuelo o libre.
    """

    def __init__(self, id_slot, fecha_inicial, fecha_final):
        self.id = id_slot
        self.fecha_inicial = fecha_inicial
        self.fecha_final = fecha_final
        self.vuelo_asignado = None

    def asigna_vuelo(self, id_vuelo, fecha_llegada, fecha_despegue):
        if self.vuelo_asignado is not None:
            raise ValueError(f"El slot {self.id} ya tiene un vuelo asignado.")

        self.vuelo_asignado = {
            "id_vuelo": id_vuelo,
            "fecha_llegada": fecha_llegada,
            "fecha_despegue": fecha_despegue
        }

    def slot_esta_libre_fecha_determinada(self, fecha):
        if self.vuelo_asignado is not None:
            return False
        if not (self.fecha_inicial <= fecha <= self.fecha_final):
            return False
        return True

    def __repr__(self):
        estado = "libre" if self.vuelo_asignado is None else f"ocupado por {self.vuelo_asignado['id_vuelo']}"
        return f"<Slot {self.id}: {self.fecha_inicial} - {self.fecha_final}, {estado}>"
