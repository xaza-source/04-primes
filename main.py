from math import sqrt

#### Fonction secondaire


def isprime(chiffre):

    premier = True;
    if chiffre < 2:
        premier = False
        return False
    else:
        for n in range(2, chiffre):
            if chiffre % n == 0:
                premier = False
                return False
                break;
        return True

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
