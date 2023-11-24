# Dies ist ein einfacher Kommentar. Er wird nicht vom Computer interpretiert.
# Er wird von Anwendungsentwicklern benutzt, um ihren Code verständlich zu machen
# Einzeilige Kommentare beginnen mit einem Rautenzeichen (#).

"""
Mehrzeilige Kommentare können
mit drei einfachen Anführungszeichen erstellt werden.
"""

# Variablendeklaration und Zuweisung
a = "Hallo! was bist du denn für ein geiler Mensch!"
print(a)
b = 5
print(b)

# Auskommentierter fehlerhafter Code
# x = 5 + "Hello"  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Bedingungsanweisungen
if b > 1:
    print("a ist größer als 1")  # Einrückung ist wichtig in Python
    print("a ist größer als 1")  # Einrückung ist wichtig in Python

# Auskommentierter fehlerhafter Code
# if a > 1  # SyntaxError: expected ':'

# Schleifen
for i in range(5):
    print(i)  # Ausgabe von 0 bis 4


# Auskommentierter fehlerhafter Code
# for i in range("Hello"):  # TypeError: 'str' object cannot be interpreted as an integer

# Funktionen
def my_function(arg1, arg2):
    return arg1 + arg2

# Funktionsaufruf
result = my_function(1, 2)
print(result)  # Ausgabe: 3

# Auskommentierter fehlerhafter Code
# my_function(1)  # TypeError: my_function() missing 1 required positional argument: 'arg2'

# Listen
my_list = [1, 2, 3]

# Zugriff auf Listenelemente
print(my_list[0])  # Ausgabe: 1

# Auskommentierter fehlerhafter Code
# print(my_list[5])  # IndexError: list index out of range
