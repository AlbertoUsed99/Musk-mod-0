class Nobel:
    # Lista para guardar todas las instancias
    all_awards = []

    def __init__(self, category, year, winner):
        if not isinstance(year, int) or year < 1900 or year > 2100:
            raise ValueError("El año debe ser un número entre 1900 y 2100")
        self.category = category
        self.year = year
        self.winner = winner
        
        # Guardar esta instancia en la lista de premios
        Nobel.all_awards.append(self)
    
    def __str__(self):
        return f"Nobel de {self.category} ({self.year}): {self.winner}"
    
    def update_winner(self, new_winner):
        self.winner = new_winner
        print(f"Ganador actualizado a: {self.winner}")
    
    @classmethod
    def show_all_awards(cls):
        for award in cls.all_awards:
            print(award)

# Crear la instancia np2005
np2005 = Nobel("Peace", 2005, "Muhammad Yunus")

# Imprimir la instancia usando __str__
print(np2005)

# Actualizar el ganador
np2005.update_winner("Otro Ganador")

# Crear otro premio
np2010 = Nobel("Physics", 2010, "Andre Geim")

# Mostrar todos los premios guardados
Nobel.show_all_awards()

