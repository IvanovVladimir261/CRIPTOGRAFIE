alphabet_upper = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
alphabet_matrix = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
LINII = 5
COLOANE = 6

print("1 - Criptarea")
print("2 - Decriptarea")
alege_text = input("Alege optiunea: ")

if alege_text != "1" and alege_text != "2":
    print("Optiune gresita! Alegeti 1 sau 2.")
    exit(1)
alege = int(alege_text)

cheie = input("Introduceti cheia: ")

if len(cheie) < 7:
    print("Cheia trebuie sa aiba cel putin 7 caractere!")
    exit(1)

cheie_majuscule = ""
for litera in cheie:
    litera = litera.upper()
    if litera not in alphabet_upper:
        print("Cheia trebuie sa contina doar litere din alfabetul roman")
        exit(1)
    if litera == "J":
        litera = "I"
    cheie_majuscule += litera

cheie_finala = ""
for litera in cheie_majuscule:
    if litera not in cheie_finala:
        cheie_finala += litera

text = input("Introduceti textul: ")

text_final = ""
for litera in text:
    if litera == " ":
        continue
    litera = litera.upper()
    if litera not in alphabet_upper:
        print("Text invalid! Sunt acceptate doar literele din alfabetul roman")
        exit(1)
    if litera == "J":
        litera = "I"
    text_final += litera

if len(text_final) == 0:
    print("Textul nu poate fi gol!")
    exit(1)

matrice = cheie_finala
for litera in alphabet_matrix:
    if litera not in matrice:
        matrice += litera

print("\nMatricea de criptare:")
for i in range(LINII):
    print(" ".join(matrice[i * COLOANE:(i + 1) * COLOANE]))

perechi = []
if alege == 1:
    i = 0
    while i < len(text_final):
        a = text_final[i]
        if i + 1 == len(text_final):
            b = "X" if a != "X" else "Q"
            i += 1
        elif text_final[i + 1] == a:
            b = "X" if a != "X" else "Q"
            i += 1
        else:
            b = text_final[i + 1]
            i += 2
        perechi.append(a + b)
else:
    if len(text_final) % 2 != 0:
        print("Criptograma trebuie sa aiba un numar par de litere!")
        exit(1)
    for i in range(0, len(text_final), 2):
        perechi.append(text_final[i] + text_final[i + 1])

pas = 1 if alege == 1 else -1

rezultat = ""
for pereche in perechi:
    poz1 = matrice.index(pereche[0])
    poz2 = matrice.index(pereche[1])
    linie1, coloana1 = poz1 // COLOANE, poz1 % COLOANE
    linie2, coloana2 = poz2 // COLOANE, poz2 % COLOANE

    if linie1 == linie2:
        coloana1 = (coloana1 + pas) % COLOANE
        coloana2 = (coloana2 + pas) % COLOANE
    elif coloana1 == coloana2:
        linie1 = (linie1 + pas) % LINII
        linie2 = (linie2 + pas) % LINII
    else:
        coloana1, coloana2 = coloana2, coloana1

    rezultat += matrice[linie1 * COLOANE + coloana1]
    rezultat += matrice[linie2 * COLOANE + coloana2]

if alege == 1:
    print(f"\nMesajul criptat este: {rezultat}")
else:
    print(f"\nMesajul decriptat este: {rezultat}")
    print("(Spatiile si literele X/Q auxiliare se corecteaza manual.)")
