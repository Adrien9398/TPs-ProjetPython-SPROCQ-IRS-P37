import re

def test_ip(ip):
    regex = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'
    return re.match(regex, ip) is not None

try:
    with open("liste_ip.txt", "r") as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            adresse = ligne.strip()
            if adresse:
                print(f"{adresse} -> {'Valide' if test_ip(adresse) else 'Invalide'}")
except FileNotFoundError:
    print("Le fichier 'liste_ip.txt' est introuvable.")
