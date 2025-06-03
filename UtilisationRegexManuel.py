import re

def test_ip(ip):
    regex = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'
    return re.match(regex, ip) is not None

while True:
    ip = input("Entrez une adresse IP (ou 'q' pour quitter) : ").strip()
    
    if ip.lower() == 'q':
        print("Programme terminé.")
        break

    if test_ip(ip):
        print("Adresse IP valide.\n")
    else:
        print("Adresse IP invalide.\n")
