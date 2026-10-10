alphabet_upper = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
# alfabetul folosit in matrice (30 litere, fara J)
alphabet_matrix = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
LINII = 5
COLOANE = 6
 
# afisam optiunile si citirea de la tastatura
print("1 - Criptarea")
print("2 - Decriptarea")
alege_text = input("Alege optiunea: ")
 
# verificam daca optiunea nu e 1 sau 2
if alege_text != "1" and alege_text != "2":
    print("Optiune gresita! Alegeti 1 sau 2.")
    exit(1)
alege = int(alege_text)
 
# cerem cheia
cheie = input("Introduceti cheia: ")
 
# verificam daca cheia are cel putin 7 caractere
if len(cheie) < 7:
    print("Cheia trebuie sa aiba cel putin 7 caractere!")
    exit(1)
 
# verificam daca cheia contine doar litere ale alfabetului
cheie_majuscule = ""
for litera in cheie:
    # convertim litera in majuscula
    litera = litera.upper()
    # verificam daca litera apartine alfabetului
    if litera not in alphabet_upper:
        print("Cheia trebuie sa contina doar litere din alfabetul roman")
        exit(1)
    # inlocuim J cu I
    if litera == "J":
        litera = "I"
    cheie_majuscule += litera
 
# eliminam literele care se repeta in cheie 
cheie_finala = ""
for litera in cheie_majuscule:
    if litera not in cheie_finala:
        cheie_finala += litera
 
# cerem textul
text = input("Introduceti textul: ")
 
# verificam daca textul contine doar litere si spatii
text_final = ""
for litera in text:
    # spatiile se elimina
    if litera == " ":
        continue
    # convertim litera in majuscula
    litera = litera.upper()
    # verificam daca litera apartine alfabetului
    if litera not in alphabet_upper:
        print("Text invalid! Sunt acceptate doar literele din alfabetul roman")
        exit(1)
    # inlocuim J cu I
    if litera == "J":
        litera = "I"
    text_final += litera
 
# verificam daca textul nu e gol
if len(text_final) == 0:
    print("Textul nu poate fi gol!")
    exit(1)
 
# construim matricea: mai intai cheia, apoi literele ramase in ordine alfabetica
matrice = cheie_finala
for litera in alphabet_matrix:
    if litera not in matrice:
        matrice += litera
 
# afisam matricea de criptare
print("\nMatricea de criptare:")
for i in range(LINII):
    print(" ".join(matrice[i * COLOANE:(i + 1) * COLOANE]))
 
# pregatirea perechilor de litere
perechi = []
if alege == 1:
    # la criptare: imparțim textul in perechi si inseram X intre literele identice
    i = 0
    while i < len(text_final):
        a = text_final[i]
        # daca a ramas o singura litera, adaugam X la sfarsit
        if i + 1 == len(text_final):
            b = "X" if a != "X" else "Q"
            i += 1
        # daca literele din pereche sunt identice, inseram X intre ele
        elif text_final[i + 1] == a:
            b = "X" if a != "X" else "Q"
            i += 1
        else:
            b = text_final[i + 1]
            i += 2
        perechi.append(a + b)
else:
    # la decriptare: criptograma trebuie sa aiba lungime para
    if len(text_final) % 2 != 0:
        print("Criptograma trebuie sa aiba un numar par de litere!")
        exit(1)
    for i in range(0, len(text_final), 2):
        perechi.append(text_final[i] + text_final[i + 1])
 
# pasul de deplasare: +1 la criptare, -1 la decriptare
pas = 1 if alege == 1 else -1
 
# criptam sau decriptam fiecare pereche
rezultat = ""
for pereche in perechi:
    # aflam pozitia fiecarei litere in matrice (linia si coloana)
    poz1 = matrice.index(pereche[0])
    poz2 = matrice.index(pereche[1])
    linie1, coloana1 = poz1 // COLOANE, poz1 % COLOANE
    linie2, coloana2 = poz2 // COLOANE, poz2 % COLOANE
 
    # literele sunt pe aceeasi linie: deplasam pe coloana
    if linie1 == linie2:
        coloana1 = (coloana1 + pas) % COLOANE
        coloana2 = (coloana2 + pas) % COLOANE
    # literele sunt pe aceeasi coloana: deplasam pe linie
    elif coloana1 == coloana2:
        linie1 = (linie1 + pas) % LINII
        linie2 = (linie2 + pas) % LINII
    # literele formeaza un dreptunghi: schimbam coloanele intre ele
    else:
        coloana1, coloana2 = coloana2, coloana1
 
    # adaugam literele noi in rezultat
    rezultat += matrice[linie1 * COLOANE + coloana1]
    rezultat += matrice[linie2 * COLOANE + coloana2]
 
# afisam rezultatul
if alege == 1:
    print(f"\nMesajul criptat este: {rezultat}")
else:
    print(f"\nMesajul decriptat este: {rezultat}")
    print("(Spatiile si literele X/Q auxiliare se corecteaza manual.)")
