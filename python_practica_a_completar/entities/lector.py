import pandas as pd
import json
import os


class Lector:
    """
    Clase base para los lectores de archivos.
    """

    def __init__(self, path: str):
        self.path = path

    def _comprueba_extension(self, extension):
        """
        Comprueba si la extensión del archivo coincide con la esperada.
        """
        _, ext = os.path.splitext(self.path)
        if ext.lower() != extension.lower():
            raise ValueError(f"Extensión incorrecta: se esperaba {extension}, se recibió {ext}")

    def lee_archivo(self):
        """
        Método genérico (debe ser sobrescrito por las subclases).
        """
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    @staticmethod
    def convierte_dict_a_csv(data: dict, ruta_salida="salida.csv"):
        """
        Convierte un diccionario en un CSV.
        """
        df = pd.DataFrame(data)
        df.to_csv(ruta_salida, index=False)
        print(f"Archivo guardado en {ruta_salida}")


class LectorCSV(Lector):
    def __init__(self, path: str):
        super().__init__(path)
        self._comprueba_extension(".csv")

    def lee_archivo(self, datetime_columns=[]):
        """
        Lee un archivo CSV y devuelve un DataFrame de pandas.
        Si hay columnas de tipo fecha, las convierte automáticamente.
        """
        df = pd.read_csv(self.path)
        for col in datetime_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")
        return df


class LectorJSON(Lector):
    def __init__(self, path: str):
        super().__init__(path)
        self._comprueba_extension(".json")

    def lee_archivo(self):
        """
        Lee un archivo JSON y lo convierte en un DataFrame.
        """
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return pd.DataFrame(data)


class LectorTXT(Lector):
    def __init__(self, path: str):
        super().__init__(path)
        self._comprueba_extension(".txt")

    def lee_archivo(self):
        """
        Lee un archivo de texto (TXT) con formato de columnas separadas por comas o tabuladores.
        """
        with open(self.path, "r", encoding="utf-8") as f:
            lineas = [line.strip().split(",") for line in f]

        # Si el archivo tiene encabezado en la primera línea
        columnas = lineas[0]
        datos = lineas[1:]
        return pd.DataFrame(datos, columns=columnas)







