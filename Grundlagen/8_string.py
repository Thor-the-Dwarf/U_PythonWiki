# String

# String Konkatination
mein_string = "Hallo Welt"
print("mein_string" + mein_string) # ohne Leerzeichen
print("mein_string", mein_string)   # mit lehrzeichen
print(mein_string + "7") # ohne Leerzeichen
print(mein_string + str(7)) # der Integer wurde zum String gecastet  # ohne Leerzeichen
print(mein_string, 7)   # mit lehrzeichen

# folgendes Produziert einen Fehler
# print(mein_string + 7) #  can only concatenate str (not "int") to str

print(mein_string + ", Sonnensystem")
komma = mein_string, ", hat jetzt n Komma"
print(komma)
print(mein_string)

mein_string_addiert = mein_string + ", Sonnensystem"
print(mein_string_addiert)      # Hallo Welt, Sonnensystem
print(mein_string)      # Hallo Welt, Sonnensystem


# # # String verhaelt sich aehnlich einer list
print("mein_string[0]", mein_string[0]) # H
print("mein_string[0]", mein_string[1]) # a
print("mein_string[0]", mein_string[2]) # l

#
# # String Methoden
# # len() -Methode
# # gibt die Laenge des Strings zurueck
laenge = len(mein_string)
print(laenge) #10
#
# # String- Teilung
erster_teil = mein_string[:5] # exclusive des 5.-Index Hallo
print(erster_teil) # Hallo
# #
zweiter_teil = mein_string[5:] # inklusive des 5.-Index
print(zweiter_teil) # Welt
#
teil_ab_index_bis_index = mein_string[3:8] # erster index ist inklusive der zweite ist exclusive
print(teil_ab_index_bis_index)
#
# # upper()
gross = mein_string.upper() # Methoden-Aufruf
print(gross) # HALLO WELT
# #
# # # lower()
klein = mein_string.lower()
print(klein) # hallo welt
#
# # # replace()
ersetzt = mein_string.replace("Welt", "Python")
print(ersetzt) # Hallo Python
#
mein_anderer_string = "Otto oder Anna"
ersetzt1 = mein_anderer_string.replace("o", "i", 1)
ersetzt2 = mein_anderer_string.replace("o", "i")
print(ersetzt1)
print(ersetzt2)

mein_anderer_string1 = mein_anderer_string[3].replace("o", "i")
print(mein_anderer_string1)
#
# # find()
position = mein_string.find("Welt") # gibt den Index zurueck bei dem das Wort anfängt
print(position) # 6
position = mein_string.find("t") # gibt den Index zurueck bei dem das Wort anfängt
print(position) # 9
#
# #
# String-Formatierung Teil 1
meine_zahl = 7
formartierter_string = f"hier {meine_zahl} wurde eine variable eingefügt"
print(formartierter_string)

for i in range(5):
    print(f"irgendwas hat den wert: {i}")




