class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

# Crear la instancia np2005
np2005 = Nobel("Peace", 2005, "Muhammad Yunus")

# Imprimir los atributos de la instancia
print(np2005.category, np2005.year, np2005.winner)