# Exceptionhandling / Fehlerbehandlung

# Alle Exceptions auffangen
try:
    result1 = 10 / 0
    print(result1)
except Exception as e:  # Exception as e == speichere die Fehlermeldung in der variable e
    print(e)
    print("hier wird ausgeführt wie sich das Programm verhalten soll wenn ein Fehler auftritt")

# Type-Error behandeln
try:
    result2 = 10 + "str"
except TypeError:
    result2 = "ungültige Typenkombination"
print(result2)

# mehrere Exceptions behandeln
my_list = [1, 2, 3]
try:
    # result1 = 10 / 0
    # result2 = 10 / "5"
    element = my_list[10]
except (ZeroDivisionError, TypeError):
    print("Entweder Division durch Null oder ungültiger Typ")
except (IndexError):
    print("index out of bounds / Index zu groß oder zu klein")

# finally Block
try:
    result1 = 10 / 0
    print("Das wird versucht auszuführen")
except:
    print("das wird nur ausgeführt, wenn ein Fehler auftritt")
finally:
    print("Das wird immer ausgeführt, egal ob ein Fehler auftritt oder nicht")