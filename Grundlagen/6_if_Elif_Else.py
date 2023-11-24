# if-else
# Kontrollstruktur
# else darf es nur einmal geben
# elif kann es beliebig oft geben

x = 7

# if
if x == 7:
    print("In x ist eine sieben!")

# if-else
if x == 7:
    print("In x ist eine sieben!")
else:
    print("In x ist keine sieben!")

# if-elif
x = 11
if x == 7:
    print("In x ist eine sieben!")
elif x == 11:
    print("In x ist eine elf!")

# if-elif-else
x = 11
if x == 7:  # WENN
    print("In x ist eine sieben!")
elif x == 11:  # SONST WENN
    print("In x ist eine elf!")
elif x == 17:  # SONST WENN
    print("In x ist eine siebzehn!")
else:  # SONST
    print("In x ist keine sieben oder elf oder siebzehn!")

# Verschachteln
if x != 7:
    if x != 11:
        if x != 17:
            print("In x ist keine sieben oder elf oder siebzehn!")
        else:
            print("if x != 17 == False")
    else:
        print("x != 11 == False")
else:
    print("x != 7 == False")

if x != 7 and x != 11 and x != 17:
    print("In x ist keine sieben oder elf oder siebzehn!")
