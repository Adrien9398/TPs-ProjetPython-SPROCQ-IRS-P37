import random

def generer_mdp_valide():
    liste_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    liste_min = "abcdefghijklmnopqrstuvwxyz"
    liste_num = "0123456789"
    liste_spe = "!@#$%^&*()-_=+[]<>.?;:"
    liste_caracteres = liste_maj + liste_min + liste_num + liste_spe

    while True:
        longueur = random.randint(12, 14)  # longueur du mot de passe entre 12 et 24
        mdp = [
            random.choice(liste_maj),
            random.choice(liste_min),
            random.choice(liste_num),
            random.choice(liste_spe)
        ]
        mdp += [random.choice(liste_caracteres) for _ in range(longueur - 4)]
        mdp_sec = ''.join(mdp)

        if (
            any(c in liste_maj for c in mdp_sec) and
            any(c in liste_min for c in mdp_sec) and
            any(c in liste_num for c in mdp_sec) and
            any(c in liste_spe for c in mdp_sec)
        ):
            print("Mot de passe généré automatiquement :", mdp_sec)
            print("Mot de passe valide selon les règles de la CNIL.")
            break

# Appel de la fonction
generer_mdp_valide()
