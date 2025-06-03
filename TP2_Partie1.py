import re
from collections import Counter

with open('auth.log', 'r') as file:
    lignes = file.readlines()

lignes_echec = [ligne for ligne in lignes if "Failed password" in ligne]

regex_ip = r'(\d{1,3}(?:\.\d{1,3}){3})'
ips_echec = [re.search(regex_ip, ligne).group(1) for ligne in lignes_echec if re.search(regex_ip, ligne)]

compteur_ips = Counter(ips_echec)

print("Top 5 IPs avec le plus de tentatives échouées :")
for ip, count in compteur_ips.most_common(5):
    print(f"{ip} : {count} échecs")
