# Import


import math

# Mathematische Konstanten
print("Pi:", math.pi)  # Pi
print("e:", math.e)  # Euler's number

# Methoden
print("pow(2, 3):", math.pow(2, 3))  # Potenz: 2^3
print("sqrt(16):", math.sqrt(16))  # Quadratwurzel: √16
print("gcd(60, 48):", math.gcd(60, 48))  # Größter gemeinsamer Teiler

# Rundungsmethoden
print("ceil(4.2):", math.ceil(4.2))  # Aufrunden auf die nächste ganze Zahl
print("floor(4.9):", math.floor(4.9))  # Abrunden auf die nächste ganze Zahl


# Auf eine Kommastelle runden
ceil_eine_nachkommastelle = (math.ceil(4.23184981 * 10) / 10)
print("Auf eine Kommastelle gerundet:", ceil_eine_nachkommastelle)

# Auf zwei Kommastellen runden
ceil_zwei_nachkommastelle = (math.ceil(4.23184981 * 100) / 100)
print("Auf zwei Kommastellen gerundet:", ceil_zwei_nachkommastelle)




