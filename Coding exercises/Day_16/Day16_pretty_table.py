from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Bulbasaur", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Grass", "Fire"])
table.align = 'l'

print(table)