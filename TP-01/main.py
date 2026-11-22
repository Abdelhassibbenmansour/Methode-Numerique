# Une fonction qui permet de lire une matrice de taille n*m
def lire_matrice():
    n = int(input("Entrer la valeur de N : "))
    m = int(input("Entrer la valeur de M : "))
    matrice = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrice[i][j] = int(input("matrice[%d][%d] : " % (i + 1, j + 1)))
    return matrice


# Une fonction qui permet de lire une matrice carrée de taille N
def lire_matrice_carree():
    n = int(input("Entrer la valeur de N : "))
    matrice = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input("T[%d][%d] = " % (i + 1, j + 1)))
    return matrice


# Une fonction qui affiche une matrice de taille n*m
def afficher_matrice(matrice, n, m):
    for i in range(n):
        for j in range(m):
            print("T[%d][%d] = %d" % (i + 1, j + 1, matrice[i][j]), end=" ")
        print()

# Une fonction qui affiche une matrice carrée de taille N
def afficher_matrice_carree(matrice,n) :
    for i in range(n):
        for j in range(n):
            print("T[%d][%d] = %d" % (i + 1, j + 1, matrice[i][j]), end=" ")
        print()

# Une fonction qui affiche une matrice d'identite de taille N
def afficher_matrice_identite(matrice,n) :
    for i in range(n):
        for j in range(n):
            if i == j:
                matrice[i][j] = 1
            else:
                matrice[i][j] = 0
    afficher_matrice_carree(matrice,n)


# Une fonction qui calcule la somme de deux matrices de taille N
def calculer_somme_matrice(matrice1, matrice2, n):
    matrice3 = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrice3[i][j] = matrice1[i][j] + matrice2[i][j]
    afficher_matrice_carree(matrice3, n)

# Une fonction qui calcule le produit de deux matrice
def calculer_produit_matrice(matrice1,matrice2):
    p1 = len(matrice1[0])
    p2 = len(matrice2)
    n = len(matrice1)
    m = len(matrice2[0])
    if p1 != p2:
        print("on peut pas calculer le produit de ces deux matrice")
        return
    matrice3 = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p1):
                matrice3[i][j] += matrice1[i][k] * matrice2[k][j]
    afficher_matrice(matrice3,n,m)

# Une fonction qui calcule la transposée d'une matrice carrée
def transposee_carree(matrice):
    n = len(matrice)
    for i in range(n):
        for j in range(0, n):
            if j > i :
                temp = matrice[i][j]
                matrice[i][j] = matrice[j][i]
                matrice[j][i] = temp
    afficher_matrice_carree(matrice,n)


# Une fonction qui teste si une matrice est triangulaire supérieure
def triangulaire_superieure(matrice):
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if j < i and matrice[i][j] != 0:
                return False
    return True


# Une fonction qui teste si une matrice est triangulaire inférieure
def triangulaire_inferieure(matrice):
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if j > i and matrice[i][j] != 0:
                return False
    return True


# Une fonction qui teste si une matrice carrée est diagonale
def diagonale(matrice):
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if i != j and matrice[i][j] != 0:
                return False
    return True


# Une fonction qui teste si une matrice carrée est symétrique
def symetrique(matrice):
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if i != j and matrice[i][j] != matrice[j][i]:
                return False
    return True


# Programme principal sous forme de menu
while True:
    print("\n========== MENU ==========")
    print("1 - Lire une matrice carrée")
    print("2 - Afficher une matrice carrée")
    print("3 - Afficher la matrice identité")
    print("4 - Calculer la somme de deux matrices")
    print("5 - Calculer le produit de deux matrices")
    print("6 - Calculer la transposée d'une matrice")
    print("7 - Tester si une matrice est triangulaire supérieure")
    print("8 - Tester si une matrice est triangulaire inférieure")
    print("9 - Tester si une matrice est diagonale")
    print("10 - Tester si une matrice est symétrique")
    print("0 - Quitter")

    choix = int(input("Entrer votre choix : "))

    if choix == 1:
        matrice = lire_matrice_carree()
        n = len(matrice)
        afficher_matrice_carree(matrice, n)
    elif choix == 2:
        matrice = lire_matrice_carree()
        n = len(matrice)
        afficher_matrice_carree(matrice, n)
    elif choix == 3:
        n = int(input("Entrer la valeur de N : "))
        matrice = [[0 for j in range(n)] for i in range(n)]
        afficher_matrice_identite(matrice, n)
    elif choix == 4:
        print("Lecture de la première matrice :")
        matrice1 = lire_matrice_carree()
        print("Lecture de la deuxième matrice :")
        matrice2 = lire_matrice_carree()
        n = len(matrice1)
        if n == len(matrice2):
            calculer_somme_matrice(matrice1, matrice2, n)
        else:
            print("Les deux matrices doivent avoir la même taille")
    elif choix == 5:
        print("Lecture de la première matrice :")
        matrice1 = lire_matrice()
        print("Lecture de la deuxième matrice :")
        matrice2 = lire_matrice()
        calculer_produit_matrice(matrice1, matrice2)
    elif choix == 6:
        matrice = lire_matrice_carree()
        transposee_carree(matrice)
    elif choix == 7:
        matrice = lire_matrice_carree()
        if triangulaire_superieure(matrice):
            print("La matrice est triangulaire supérieure")
        else:
            print("La matrice n'est pas triangulaire supérieure")
    elif choix == 8:
        matrice = lire_matrice_carree()
        if triangulaire_inferieure(matrice):
            print("La matrice est triangulaire inférieure")
        else:
            print("La matrice n'est pas triangulaire inférieure")
    elif choix == 9:
        matrice = lire_matrice_carree()
        if diagonale(matrice):
            print("La matrice est diagonale")
        else:
            print("La matrice n'est pas diagonale")
    elif choix == 10:
        matrice = lire_matrice_carree()
        if symetrique(matrice):
            print("La matrice est symétrique")
        else:
            print("La matrice n'est pas symétrique")
    elif choix == 0:
        print("Fin du programme")
        break
    else:
        print("Choix invalide")
