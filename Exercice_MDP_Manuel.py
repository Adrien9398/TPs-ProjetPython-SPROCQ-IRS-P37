#Test de mots de passe entré manuellement par l'utilisateur 
def mdp_valide(mdp):
    liste_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    liste_min = "abcdefghijklmnopqrstuvwxyz" 
    liste_num = "0123456789"
    liste_spe = "!@#$%^&*()-_=+[]<>.?;:"

    if len(mdp) < 12:
        print("Le mot de passe doit contenir minimum 12 caracteres")
        return False

    verif_maj = any(c in liste_maj for c in mdp)
    verif_min = any(c in liste_min for c in mdp)
    verif_num = any(c in liste_num for c in mdp)
    verif_spe = any(c in liste_spe for c in mdp)

    if not (verif_maj and verif_min and verif_num and verif_spe):
        print("Le mot de passe doit contenir au moins : une majuscule, une minuscule, un chiffre et un caractere special")
        return False

    print("Mot de passe valide selon les regles de la CNIL")
    return True

while True:
    utilisateur_mdp = input("Entrez votre mot de passe : ")
    if mdp_valide(utilisateur_mdp):
        break
    else:
        print("Veuillez réessayer.\n")
