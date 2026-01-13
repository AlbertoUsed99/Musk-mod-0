# estudiante.py

class Estudiante:
    # Atributo de clase
    escuela = "Escuela Primaria XYZ"  # Valor predeterminado

    def __init__(self, nombre):
        self.nombre = nombre
        self.grade = 0  # Inicializamos la nota en 0

    def calcular_media(self, notas):
        if notas:
            self.grade = sum(notas) / len(notas)
        else:
            self.grade = 0  # Si no hay notas, la media es 0

    @staticmethod
    def imprimir_asignaturas_reprobadas(asignaturas_notas):
        # Iteramos sobre el diccionario de asignaturas y notas
        for asignatura, nota in asignaturas_notas.items():
            if nota < 5:
                print(f"La asignatura {asignatura} tiene una nota de {nota}, que es inferior a 5.")

    @classmethod
    def actualizar_escuela(cls, nueva_escuela):
        cls.escuela = nueva_escuela  # Actualiza el atributo de clase `escuela`

    # Método privado que evalúa el diccionario de asistencias
    def _evaluar_asistencias(self, asistencias):
        tiene_menos_de_4 = any(asistencia < 4 for asistencia in asistencias.values())
        tiene_entre_4_y_7 = any(4 <= asistencia < 8 for asistencia in asistencias.values())
        
        if tiene_menos_de_4:
            return 1
        elif tiene_entre_4_y_7:
            return 2
        return 3  # Si todas las asistencias son 8 o más

    # Método público para probar el método privado
    def evaluar_asistencias(self, asistencias):
        return self._evaluar_asistencias(asistencias)
