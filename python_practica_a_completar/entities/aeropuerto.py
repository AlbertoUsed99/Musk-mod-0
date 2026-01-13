import pandas as pd
from datetime import datetime, timedelta
from entities.slot import Slot


class Aeropuerto:
    """
    Clase principal que gestiona los vuelos y la asignación de slots en el aeropuerto.
    """

    def __init__(self, vuelos: pd.DataFrame, slots: int, t_embarque_nat: int, t_embarque_internat: int):
        """
        Inicializa el aeropuerto con los vuelos, los slots y los tiempos de embarque.

        :param vuelos: DataFrame con los datos de los vuelos.
        :param slots: Número total de slots disponibles.
        :param t_embarque_nat: Tiempo de embarque para vuelos nacionales (minutos).
        :param t_embarque_internat: Tiempo de embarque para vuelos internacionales (minutos).
        """
        self.df_vuelos = vuelos
        self.n_slots = slots
        self.slots = {}
        self.tiempo_embarque_nat = t_embarque_nat
        self.tiempo_embarque_internat = t_embarque_internat

        # Crear los slots (ejemplo: 1 hora cada uno, consecutivos)
        hora_inicial = datetime(2022, 5, 8, 6, 0)
        for i in range(1, self.n_slots + 1):
            inicio = hora_inicial + timedelta(hours=i - 1)
            fin = inicio + timedelta(hours=1)
            self.slots[i] = Slot(i, inicio, fin)

        # Añadir columnas al DataFrame
        self.df_vuelos["fecha_despegue"] = pd.NaT
        self.df_vuelos["slot"] = 0

    # ----------------------------------------------------------------------

    def calcula_fecha_despegue(self, row) -> pd.Series:
        """
        Calcula la fecha de despegue en función del tipo de vuelo y el tiempo de embarque.
        """
        tipo = row["tipo_vuelo"].strip().upper()

        if tipo == "NAT":  # Nacional
            row["fecha_despegue"] = row["fecha_llegada"] + timedelta(minutes=self.tiempo_embarque_nat)
        else:  # Internacional
            row["fecha_despegue"] = row["fecha_llegada"] + timedelta(minutes=self.tiempo_embarque_internat)

        return row

    # ----------------------------------------------------------------------

    def encuentra_slot(self, fecha_vuelo) -> int:
        """
        Encuentra el primer slot libre para una fecha determinada.
        Devuelve el ID del slot o -1 si no hay ninguno disponible.
        """
        for slot_id, slot in self.slots.items():
            if slot.slot_esta_libre_fecha_determinada(fecha_vuelo):
                return slot_id
        return -1

    # ----------------------------------------------------------------------

    def asigna_slot(self, vuelo) -> pd.Series:
        """
        Asigna un slot a un vuelo si hay disponibilidad.
        """
        fecha = vuelo["fecha_llegada"]
        slot_id = self.encuentra_slot(fecha)

        if slot_id == -1:
            vuelo["slot"] = 0
        else:
            vuelo["slot"] = slot_id
            slot = self.slots[slot_id]
            slot.asigna_vuelo(vuelo["id"], vuelo["fecha_llegada"], vuelo["fecha_despegue"])

        return vuelo

    # ----------------------------------------------------------------------

    def asigna_slots(self):
        """
        Recorre todos los vuelos y asigna fechas de despegue y slots.
        """
        print("🛫 Asignando slots a los vuelos...")
        self.df_vuelos = self.df_vuelos.apply(self.calcula_fecha_despegue, axis=1)
        self.df_vuelos = self.df_vuelos.apply(self.asigna_slot, axis=1)
        print("✅ Asignación completada.\n")
