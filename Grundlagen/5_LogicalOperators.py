# Logische Operatoren
# Boolsche Operatoren: and, or, not

# and - UND (sowohl als auch)
print(3 >= 2 and 7 != 9)  # True
print((3 >= 2) and (7 != 9))  # True

# Nur True, wenn beide True sind
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False
#
if True and True:
    print("bedingungen sind beide erfüllt")

if True and False:
    print("eine der Bedingungen ist nicht erfüllt")

if False and True:
    print("eine der Bedingungen ist nicht erfüllt")

if False and False:
    print("eine der Bedingungen ist nicht erfüllt")


#
# or - ODER (entweder oder)
# Nur False, wenn beide False sind
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

if False or False:
    print("Beide Bedingungen sind nicht erfüllt")

if True or False:
    print("eine der Bedingungen erfüllt")

if 1 == 1 or False:
    print("eine der Bedingungen erfüllt")


#
# # not - NICHT
# not kehrt den Boolean um
print(not (1 == 1))  # False
print(not True)  # False
print(not False)  # True
