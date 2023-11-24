# while-Schleife
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# unendliche while-Schleife
# j = 0
# while True:
#     while j < 200:
#         j += 1
#         if j == 111:
#             break
#         print(j)
#
#     print("läuft noch")


aeusserer_loop_zaehler = 0
while aeusserer_loop_zaehler < 10:
    print(f"erster_loop: {aeusserer_loop_zaehler}")
    aeusserer_loop_zaehler += 1
    inner_loop_zaehler = 0
    while inner_loop_zaehler < 3:
        print(f"zweiter_loop:{inner_loop_zaehler}")
        inner_loop_zaehler += 1
        print("hier ist der zweite loop zu ende")
    print("erster_loop Ende")
