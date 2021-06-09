def replace(lista,indice, lista_mare):
   for i in range(len(lista_mare)):
       for j in range(len(alfabet)+1):
           if lista_mare[i][j] == lista:
               lista_mare[i][j] = indice

def split(cuvant):
    litere = []
    for caracter in cuvant:
        litere.append(caracter)
    return litere

def elemente_comune(lista1, lista2):
    multime1 = set(lista1)
    multime2 = set(lista2)
    if (multime1 & multime2):
        return True
    else:
        return False

def noi_linii(stare, matrice, alfabet, stari_finale):
    coada = [stare]
    if stare not in gasite:
        gasite.append(stare)
    j = 0

    while len(coada) != 0:
        stare = coada.pop(0)
        if elemente_comune(stare, stari_finale):
            stari_finale_p.append(list(set(stare)))

        # print(stare)
        for litera in alfabet:
            stari = []
            for st in stare:
                # print(st)
                if matrice[st][alfabet.index(litera)]:
                    stari += matrice[st][alfabet.index(litera)]
            stari.sort()
            relatii.append([litera, stare, list(set(stari))])
            j += 1
            # print(stari)
            if stari != [] and list(set(stari)) not in gasite:
                gasite.append(list(set(stari)))
                coada.append(list(set(stari)))
    return relatii



f = open("afnn.in", "r")
toate_liniile = []

# citire linii
linie = f.readline()
while linie:
    if linie[-1] == '\n':
        linie = linie[: - 1]
    toate_liniile.append(linie)
    # print(linie)
    linie = f.readline()

n = int(toate_liniile[0])  # indice max stare
# print(n)

gasite = []
for i in range(0, n + 1):
    gasite.append([i])
# print(gasite)

relatii = []
stari_finale_p = []


caract_stari_finale = toate_liniile[1].split(' ')  # vector caract stari
# print(caract_stari_finale)

alfabet = split(toate_liniile[2])  # REVINOOOOOOOOOOOOOOOOOOOO AICIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
# print(alfabet)

sf = toate_liniile[3].split(' ')
stari_finale =[]
for i in sf:
    stari_finale.append(int(i))
# print(stari_finale)

k = int(toate_liniile[4])  # k relatii de adiacenta
# print(k)

matrice = [[[] for i in range(len(alfabet))] for j in range(n+1)]
for i in range(k):
    linie = toate_liniile[5 + i].split(' ')
    matrice[int(linie[1])][alfabet.index(linie[0])].append(int(linie[2]))


for i in range(n+1):
    print(matrice[i], end=" ")
    print("")

m = int(toate_liniile[4 + k + 1])  # nr de cuvinte
# print(m)

cuvinte = []  # cuvinte de testat
for i in range(m):
    cuvinte.append(toate_liniile[4 + k + 2 + i])
    # print(cuvinte[i])

f = open("transform.out", "w")

np = 0 # indice max stari AFD
kp = k  # nr de relatii de adiacenta AFD


stari_compuse = []
for i in range(len(matrice)):
    for j in range(len(alfabet)):
        if len(matrice[i][j]) > 1:
            stari_compuse.append(list(set(matrice[i][j])))
# print(stari_compuse)

for i in stari_compuse:
    noi_linii(i, matrice, alfabet, stari_finale)


alte_relatii = []
for i in range(n+1):
    for j in range(len(alfabet)):
        if matrice[i][j]:
            alte_relatii.append([alfabet[j], [i], list(set(matrice[i][j]))])


for elem in stari_finale:
    stari_finale_p.append([elem])
#stari_finale_p += stari_finale
# print(stari_finale_p)

np = len(gasite)
# print(np)
kp += len(relatii)
# print(kp)

alte_relatii += relatii


for elem in gasite:
    if(len(elem) > 1):
        replace(elem, n+1, alte_relatii)
        n += 1
    else:
        replace(elem, elem[0], alte_relatii)

for i in range(len(alte_relatii)):
    print(alte_relatii[i], end=" ")
    print("")

# matrice AFD

matrix = [[[] for i in range(len(alfabet))] for j in range(np)]

for i in range(len(alte_relatii)):
        matrix[alte_relatii[i][1]][alfabet.index(alte_relatii[i][0])] = alte_relatii[i][2]

for i in range(np):
    for j in range(len(alfabet)):
        print(matrix[i][j], end=" ")
    print("")

# np e defapt -1

print(stari_finale_p)

for cuvant in cuvinte:
    stare_curenta = 0
    ok = True
    for litera in cuvant:
        if matrix[stare_curenta][alfabet.index(litera)]:
            stare_curenta = matrix[stare_curenta][alfabet.index(litera)]
            # print(stare_curenta)
        else:
            ok = False
            break

    for stare in stari_finale_p:
        # print(stare)
        if ok is True and elemente_comune([stare_curenta], stare):
            print(1)
            f.write("1\n")
            break
    else:
        print(0)
        f.write("0\n")

f.close()



