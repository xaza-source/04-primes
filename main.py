#### Fonction secondaire
"""
Programme principal permettant d'afficher les nombres premiers
entre 0 et 99 et d'afficher les détails du test de primalité.
"""
def isprime(chiffre):
    """
    Détermine si un nombre est premier.

    Paramètres
    ----------
    chiffre : int
        Le nombre à tester.

    Retourne
    --------
    bool
        True si le nombre est premier, False sinon.
    """
    if chiffre < 2:
        return False
    for n in range(2, chiffre):
        if chiffre % n == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Fonction principale.
    Affiche tous les nombres premiers entre 0 et 99.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
