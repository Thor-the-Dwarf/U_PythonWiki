# Random

import random

# Generiert eine Zufallszahl zwischen 0 und 1
zufalls_float = random.random()
print(f"Zufallszahl zwischen 0 und 1: {zufalls_float}")

# Generiert eine zufällige Ganzzahl zwischen 1 und 10
zufallszahl = random.randint(1, 10)
print(f"Zufallszahl zwischen 1 und 10: {zufallszahl}")

# Generiert eine Zufallszahl zwischen zwei gegebenen Werten
zufalls_float_bereich = random.uniform(88, 100)
print(f"Zufallszahl zwischen 1 und 100: {zufalls_float_bereich}")
