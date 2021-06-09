
def split(cuvant):
    litere = []
    for caracter in cuvant:
        litere.append(caracter)
    return litere


def main():
    f = open("afd.in", "r")
    toate_liniile = []
    # citire linii
    linie = f.readline()
    while linie:
        if linie[-1] == '\n':
            linie = linie[: - 1]
        toate_liniile.append(linie)
        # print(linie)
        linie = f.readline()

    n = int(toate_liniile[0])  # indice maxim al unei stari
    caract_stari_finale = toate_liniile[1].split(' ')  # vector de caract al starilor
    # print(stari_finale)
    alfabet = split(toate_liniile[2])
    # print(alfabet)

    sf = toate_liniile[3].split(' ')  # multimea de stari finale
    stari_finale = [int(elem) for elem in sf]
    # print(stari_finale)

    k = int(toate_liniile[4])  # k relatii de adiacenta
    # print(k)
    matrice = [[[] for i in range(len(alfabet))] for j in range(n+1)]
    for i in range(k):
        linie = toate_liniile[5 + i].split(' ')
        matrice[int(linie[1])][alfabet.index(linie[0])] = int(linie[2])

    for i in range(n+1):
        for j in range(len(alfabet)):
            print(matrice[i][j], end=" ")
        print("")

    m = int(toate_liniile[4 + k + 1])  # nr de cuvinte
    cuvinte = []
    for i in range(m):
        cuvinte.append(toate_liniile[4 + k + 2 + i])  # cuvintele de testat
    # print(cuvinte)

    f = open("afd.out", "w")

    for cuvant in cuvinte:
        stare_curenta = 0
        ok = True
        for litera in cuvant:
            if matrice[stare_curenta][alfabet.index(litera)]:
                stare_curenta = matrice[stare_curenta][alfabet.index(litera)]
            else:
                ok = False
                break
        if ok and stare_curenta in stari_finale:
            print(1)
            f.write("1\n")

        else:
                print(0)
                f.write("0\n")
    f.close()


if __name__ == "__main__":
    main()
