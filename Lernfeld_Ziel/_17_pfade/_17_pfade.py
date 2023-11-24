# Pfade

## relative Pfade
# .. == überordner
with open("../txt_Fyle.txt", "r") as datei:
    # Liest den gesamten Inhalt
    inhalt = datei.read()
    print(f"[r] Inhalt der Datei: {inhalt}")


with open("../../Grundlagen/9_schleifen/1_while_schleife.py", "r") as datei:
    # Liest den gesamten Inhalt
    inhalt = datei.read()
    print(f"[r] Inhalt der Datei: {inhalt}")

try:
    with open("C:\\Users/Thor/OneDrive/Desktop\\beispiel.txt", "x") as datei:
        # Erstellt eine neue Datei und schreibt den Text hinein
        datei.write("\n \t[x]hat das hier erzeugt. Und zwar die ganze Datei!")
except FileExistsError:
    print("[x] Datei existiert bereits!")