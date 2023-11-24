# list

# Eine leere Liste erstellen
leere_liste = []
print("leere_liste:", leere_liste)

# Liste mit Elementen erstellen
# eine list kann alle Datentypen auch gleichzeitig enthalten
meine_liste = [1, 2.345, "string", True]
print("meine_liste:", meine_liste)


# Auf Listen - Elemente zugreifen
listen_element = meine_liste[3]
print("listen_element:", listen_element)

# Element anhängen
meine_liste.append(4)
print("Element anhängen:", meine_liste)

# Element an spezifischer Position einfügen
meine_liste.insert(3, "element")
print("Element einfügen:", meine_liste)

# Element entfernen
meine_liste.remove("element")
print("Element entfernen:", meine_liste)

# Element an einer Position löschen
del meine_liste[2]
print("Element löschen:", meine_liste)

# Liste sortieren
zu_sortierende_list1 = [1, 2, 9, 111, 8]
zu_sortierende_list2 = ["1", "abc", "Hans", "Barbara"]
zu_sortierende_list3 = [1.0, 2.798, 9.7852, 111.7851, 8.784]
zu_sortierende_list4 = ["]", "abc", "Barbara", "1"]
zu_sortierende_list5 = [1.1, 1, 9.7852, 100, 8.784]
zu_sortierende_list1.sort()
zu_sortierende_list2.sort()
zu_sortierende_list3.sort()
zu_sortierende_list4.sort()
zu_sortierende_list5.sort()
print("Liste sortieren1:", zu_sortierende_list1.sort())
print("Liste sortieren2:", zu_sortierende_list2)
print("Liste sortieren3:", zu_sortierende_list3)
print("Liste sortieren4:", zu_sortierende_list4)
print("Liste sortieren5:", zu_sortierende_list5)

# Liste umdrehen
zu_sortierende_list5.reverse()
print("Liste umdrehen:", zu_sortierende_list5)



# Häufige Fehler
# 1. Indizes beginnen bei 0
# erstes_element = meine_liste[0]
# 2. Zugriff auf nicht vorhandenen Indizes führt zu einem Fehler
# vermeindlich_letztes_element = meine_liste[4]
# 3. Bei der Methode sort() werden Grossbuchstaben vor kleinbuchstaben sortiert

