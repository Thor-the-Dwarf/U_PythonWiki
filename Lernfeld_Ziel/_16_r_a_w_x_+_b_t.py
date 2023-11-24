# # Dateien durch Python manipulieren
#
# # 'r' öffnet eine Datei im Lese-Modus / Readmode
# with open("python_Fyle.py", "r") as datei:
#     # Liest den gesamten Inhalt
#     inhalt = datei.read()
#     print(f"[r] Inhalt der Datei: {inhalt}")
#     print(type(inhalt))
#
# # 'a' öffnet eine Datei im Anhängemodus / Apendmode
# with open("python_Fyle.py", "a") as datei:
#     # Fügt am Ende einer Datei Text hinzu
#     datei.write(("\n[a] war hier! :P"))
#
# # # 'w' öffnet eine Datei im Schreib-modus / Writemode
# # with open("python_Fyle.py", "w") as datei:
# #     # Überschreibt den gesamten Inhalt
# #     datei.write(("\n[w] hat den gesamten Text überschrieben"))
#
# # 'x' öffnet eine Datei im exklusivem-Erstellungsmodus / Xclusivemode
# # exklusiv, weil es einen Fehler gibt, wenn die Datei bereits existiert
# try:
#     with open("pythons_txt_Fyle.txt", "x") as datei:
#         # Erstellt eine neue Datei und schreibt den Text hinein
#         datei.write("\n[x] hat das hier erzeugt. Und zwar die ganze Datei!")
# except FileExistsError:
#     print("[x] Datei existiert bereits!")
#
#
# # 'r+' öffnet eine Datei im Lese- und Schreibmodus / Read+
# with open("txt_Fyle.txt", "r+") as datei:
#     # Liest und schreibt in der gleichen Datei
#     inhalt = datei.read()
#     datei.write("\n[r+] kann lesen und schreiben")
#     print(f"[r+] Inhalt der Datei: {inhalt}")

# 'rb' öffnet eine Datei im Binärmodus / ReadByte
with open("txt_Fyle.txt", "rb") as datei: # Streamt durch die Datei
    inhalt = datei.read()
    # Umwandlung der Bytes in binäre Darstellung
    bin_inhalt = ' '.join(format(byte, '08b') for byte in inhalt)
    print(f"Binärer Inhalt der Datei: {bin_inhalt}")
