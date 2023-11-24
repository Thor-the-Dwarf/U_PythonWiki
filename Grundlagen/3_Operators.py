# Rechenoperatoren
print(3 + 7)  # 10
print("3" + "7")  # 37
print("3" + str(7))  # 37
print(13 - 7)  # 6
print(3 * 7)  # 21
print(21 / 7)  # 3.0

# Bei zwei Integern wird ein float zurückgegeben (Division)
print(11 / 2)  # 5.5

# Wenn mindestens eine Fließkommazahl dabei ist, wird ein float zurückgegeben
print(10.0 / 2)  # 5.0
print(10 / 2.0)  # 5.0
print(10.0 / 2.0)  # 5.0

# Modulo - Restwert-Division
print(9 % 3) # 0
print(10 % 3) # 1
print(11 % 3) # 2
print(12 % 3) # 0

print(37 % 7)  # 2
print(7 % 7)  # 0
print(4 % 7)  # 4 (die erste Zahl)

# Inkrement- & Dekrementoperator
x = 7
x += 1
print(x)  # 8
x -= 2
print(x)  # 6