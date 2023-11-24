# Funktion

# Das Schlüsselwort "def" beginnt die Funktionsdefinition.
# "funktionsname" ist der Name der Funktion.
# "parameter1" und "parameter2" sind Parameter (optional).
def funktionsname(parameter1, parameter2):
    # der Funktionskörper beginnt hier.
    pass # "pass" ist ein Platzhalter der keine Aktion ausführt


# void-Methoden == Methoden ohne Rückgabewert
def voidMethode_ohneparameter():
    print("void-Methode ohen Parameter")

def ein_parameter(bratwurst):
    print(f"ein {bratwurst}")

def zwei_parameter(a, b):
    print(f"{a} {b}")

## Return-Methoden
def returnMethode1(wert1, wert2): # reciever / antworter
    return_wert = wert1 + wert2
    return return_wert

def returnMethode2(a):
    #Kurzschreibweise
    return "Ey " + str(a) + "!"

# void-Methoden Aufrufe
voidMethode_ohneparameter()
ein_parameter("Parameter")
ein_parameter(1234567)
zwei_parameter("python", "ist toll")
zwei_parameter("zwei", "Parameter")
# zwei_parameter("Parameter") # missing 1 required positional argument: 'b'

# return-Methoden Aufrufe
value1 = returnMethode1(1, 23) # caler /rufer
print("returnMethode1: ", value1)
value2 = returnMethode2("Du rockst das hier total")
print("returnMethode2: ", value2)

# rekursive Methode
def summe_bis_n(n):
    if n == 0:
        print("if ausgeführt")
        return 0
    else:
        print("else ausgeführt")
        print(n)
        return n + summe_bis_n(n - 1)
print(summe_bis_n(5))

# hier ist was im rekursiven Methodenaufruf stattfindet abgebildet
flag = True
m = 5
ausgabe = 0
while flag:
    while m > 0:
        ausgabe += m
        m -= 1
        if m == 0:
            flag = False

print(ausgabe)