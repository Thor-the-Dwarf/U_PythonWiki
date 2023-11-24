# Vergleichsoperatoren
# ==, !=, <, >, <=, >=
# Ein Ausdruck mit einem Vergleichsoperator evaluiert immer zu einem Boolean (True oder False).

print(3 == 4)  # False      # gleich
print(2 != 7)  # True       # nichtgleich
print(3 < 5)  # True        # kleiner als
print(2 > 7)  # False       # groesser als
print(3 <= 3)  # True       # kleinergleich
print(2 >= 3)  # False      # groessergleich

# In Python können alle numerischen Typen mit == verglichen werden.
# Der Integer wird implizit zum Float konvertiert:
print(3 == 3.0)  # True
print(3 == "3.0")  # False
print(3 == "3")  # False
print(1 == True)  # True
print(1.0 == True)  # True





