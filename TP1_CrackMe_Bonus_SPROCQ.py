#Jeu pour trouver les mots de passe défini dans un fichier texte, dans le cas ou le fichier n'est pas trouvé il utilise une liste prédéfinie
import random


def liste_mots(nom_fichier="liste_mdp.txt"):
    liste_mdp = ["123456","password","admin","123456789","qwerty","abc123","letmein","welcome","monkey","football"]
    try:
        with open(nom_fichier, 'r') as f:
            mots = [l.strip() for l in f if l.strip()]
        return mots if mots else liste_mdp
    except:
        return liste_mdp

mdp_secret = random.choice(liste_mots())

print("CrackMe d'Adrien SPROCQ")
triche = input("Activer le mode triche ? (oui/non) : ").lower()
if triche == "oui":
    print(">>> Mot de passe à deviner :", mdp_secret)

limite = input("Nombre maximum d'essais (laisser vide pour illimité) : ")
limite = int(limite) if limite.isdigit() else None

historique = []

tenta = 0

while True:
    mdp_propo = input("Devinez le mot de passe : ")
    historique.append(mdp_propo)
    tenta += 1

    if mdp_propo == mdp_secret:
        print("Bravo ! Mot de passe trouvé en", tenta, "essai(s).")
        break
    else:
        print("Incorrect.")
        if len(mdp_propo) < len(mdp_secret):
            print("Indice : le mot est plus long.")
        elif len(mdp_propo) > len(mdp_secret):
            print("Indice : le mot est plus court.")
        if mdp_propo and mdp_propo[0] == mdp_secret[0]:
            print("Indice : même première lettre.")
        carac_comm = set(mdp_propo) & set(mdp_secret)
        print("Indice :", len(carac_comm), "lettre(s) en commun.")

    if limite and tenta >= limite:
        print("Nombre maximum d'essais atteint. Le mot de passe était :", mdp_secret)
        break
print("\nHistorique des tentatives :")
for i, essai in enumerate(historique, 1):
    print(f"{i}. {essai}")
