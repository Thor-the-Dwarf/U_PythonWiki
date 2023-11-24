# Casting

# Casting ist der Vorgang, bei dem eine Variable von
# einem Datentyp in einen anderen umgewandelt wird

## Integer

# Von String zu Integer
x = "42"
y = int(x)
print(type(y)) # <class 'int'>

# Vom Float zum Integer
# Wenn man einen Float zum Integer castet,
# wird die Nachkommastelle abgeschnitten
x = 42.9
y = int(x)
print(y) # 42
print(type(y)) # <class 'int'>

# Aufpassen! Python castet auch automatisch
integer1 = 5
integer2 = 5
float1 = integer2 / integer1
print(float1)
print(type(float1))

# Von Boolean zu Integer
x = False
y = int(x)
print(y)
print(type(y))

## Float

# vom String zum Float
x = "42.0"
y = float(x)
print(y)
print(type(y))

# vom Integer zum Float
x = 444
y = float(x)
print(y)
print(type(y))

# vom Boolean zum Float
x = False
y = float(x)
print(y)
print(type(y))

## Boolean

# vom Integer zum Boolean
# 0 ist der einzige Integer der False wird, alle anderen werden True
x = 0
y = bool(x)
print(y)
print(type(y))

# vom Float zum Boolean
# 0.0 ist der einzige Float der False wird, alle anderen werden True
x = -0.1231654896
y = bool(x)
print(y)
print(x)
print(type(y))

# vom String zum Boolean
# "" ist der einzige String der False wird, alle anderen werden True
x = "False"
y = bool(x)
print(y)
print(x)
print(type(y))

# String
# von boolean zum String
x = False
y = str(x)
print(y)
print(x)
print(type(y))

# von Integer zum String
x = 1
y = str(x)
print(y)
print(x)
print(type(y))

# von Float zum String
x = 1.15
y = str(x)
print(y)
print(x)
print(type(y))
