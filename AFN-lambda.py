
def inchidere(stare, marcate, matrice, n, lista):
    marcate.append(stare)
    for indice in range(n+1):
        if matrice[stare][indice] == 'L' and indice not in marcate:

            lista += [stare] + inchidere(indice, marcate, matrice, n, lista)
        else:
            lista += [stare]
    return [stare]


def split(cuvant):
    litere = []
    for caracter in cuvant:
        litere.append(caracter)
    return litere


def main():
    f = open("afn_lambda.in", "r")
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

    alfabet = split(toate_liniile[1])
    alfabet.append('L')
    # print(alfabet)

    finale = toate_liniile[2].split(' ')
    # print(stari_finale)
    stari_finale = []
    for i in range(len(finale)):
        stari_finale.append(int(finale[i]))

    k = int(toate_liniile[3])  # k relatii de adiacenta
    # print(k)

    m = int(toate_liniile[3 + k + 1])  # nr de cuvinte
    # print(m)

    cuvinte = []  # cuvinte de testat
    for i in range(m):
        cuvinte.append(toate_liniile[3 + k + 2 + i])
        # print(cuvinte[i])

    # matrice nxn
    matrix = [[[] for i in range(n+1)] for j in range(n+1)]
    for i in range(k):
        linie = toate_liniile[4 + i].split(' ')
        matrix[int(linie[1])][int(linie[2])] = linie[0]

    # print matrice
    '''
    for i in range(n+1):
        for j in range(n+1):
            print(matrix[i][j], end=" ")
        print("")
    '''

    # matrice nx2
    matrice = [[[] for i in range(len(alfabet))] for j in range(n + 1)]
    for i in range(k):
        linie = toate_liniile[4 + i].split(' ')
        matrice[int(linie[1])][alfabet.index(linie[0])].append(int(linie[2]))

    # print('###########')
    # print matrice
    for i in range(n + 1):
        for j in range(len(alfabet)):
            print(matrice[i][j], end=" ")
        print("")

    inchideri = []
    for i in range(n+1):
        lista = []
        marcate = []
        inchidere(i, marcate, matrix, n, lista)
        inchideri.append(list(set(lista)))
    # print(inchideri)

    f = open("afn_lambda.out", "w")

    for cuvant in cuvinte:
        stare_curenta = [0]
        for litera in cuvant:
            st_next = []
            for stare in stare_curenta:
                for closure in inchideri[stare]:
                    st_next += matrice[closure][alfabet.index(litera)]
                stare_curenta = st_next
                # print(stare_curenta)
        if len(st_next) == 0:
            f.write("0\n")
            print('0')
        else:
            if set(stare_curenta) & set(stari_finale):
                f.write("1\n")
                print('1')
            else:
                f.write("0\n")
                print('0')

if __name__ == "__main__":
    main()
