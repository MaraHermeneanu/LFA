
def split(cuvant):
    litere = []
    for caracter in cuvant:
        litere.append(caracter)
    return litere

def main():
    f = open("afn.in", "r")
    toate_liniile = []

    # citire linii
    linie = f.readline()
    while linie:
        if linie[-1] == '\n':
            linie = linie[: -1]
        toate_liniile.append(linie)
        # print(linie)
        linie = f.readline()

    n = int(toate_liniile[0])  # indice max stare
    # print(n)

    caract_stari_finale = toate_liniile[1].split(' ')  # vector caract stari
    # print(caract_stari_finale)

    alfabet = split(toate_liniile[2])
    # print(alfabet)

    finale = toate_liniile[3].split(' ')
    stari_finale = []
    for i in range(len(finale)):
        stari_finale.append(int(finale[i]))
    # print(finale)
    print(stari_finale)

    k = int(toate_liniile[4])  # k relatii de adiacenta
    # print(k)

    matrice = [[[] for i in range(len(alfabet))] for j in range(n+1)]
    for i in range(k):
        linie = toate_liniile[5 + i].split(' ')
        matrice[int(linie[1])][alfabet.index(linie[0])].append(int(linie[2]))

    m = int(toate_liniile[4 + k + 1])  # nr de cuvinte
    # print(m)

    cuvinte = []  # cuvinte de testat
    for i in range(m):
        cuvinte.append(toate_liniile[4 + k + 2 + i])
        # print(cuvinte[i])

    for i in range(n+1):
        for j in range(len(alfabet)):
            print(matrice[i][j], end=" ")
        print("")

    f = open("afn.out", "w")

    for cuvant in cuvinte:
        multime_stari = [0]
        for litera in cuvant:
            next_stare =[]
            stari = []
            for stare_curenta in multime_stari:
                if matrice[stare_curenta][alfabet.index(litera)]:
                    stari += matrice[stare_curenta][alfabet.index(litera)]
            next_stare = stari
            if len(next_stare):
                multime_stari = set(next_stare);
            else:
                break
        if set(next_stare) & set(stari_finale):
            print(1)
            f.write('1\n')
        else:
            print(0)
            f.wrtie('0\n')
   f.close()	

if __name__ == "__main__":
    main()