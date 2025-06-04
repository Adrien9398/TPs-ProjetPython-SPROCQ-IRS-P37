import socket
import argparse
import threading
from queue import Queue
import csv
import sys

# Résultats partagés
open_ports = []
lock = threading.Lock()

def scan_port(ip, port, verbose):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            with lock:
                if result == 0:
                    print(f" Port {port} ouvert")
                    open_ports.append(port)
                elif verbose:
                    print(f" Port {port} fermé")
    except socket.gaierror:
        print("[!] Adresse IP invalide.")
        sys.exit(1)
    except Exception as e:
        with lock:
            print(f"[!] Erreur sur le port {port} : {e}")

def worker(ip, verbose, q):
    while not q.empty():
        port = q.get()
        scan_port(ip, port, verbose)
        q.task_done()

def main():
    parser = argparse.ArgumentParser(description="Scanner de ports TCP")
    parser.add_argument("--ip", required=True, help="Adresse IP à scanner")
    parser.add_argument("--start-port", type=int, required=True, help="Port de début")
    parser.add_argument("--end-port", type=int, required=True, help="Port de fin")
    parser.add_argument("--verbose", action="store_true", help="Afficher aussi les ports fermés")
    parser.add_argument("--threads", type=int, default=50, help="Nombre de threads (par défaut: 50)")
    parser.add_argument("--no-threads", action="store_true", help="Désactiver les threads (mode lent)")
    parser.add_argument("--output", help="Fichier de sortie (txt ou csv)")

    args = parser.parse_args()

    ip = args.ip
    ports = range(args.start_port, args.end_port + 1)

    if args.no_threads:
        # Mode mono-thread
        for port in ports:
            scan_port(ip, port, args.verbose)
    else:
        # Mode multi-thread
        q = Queue()
        for port in ports:
            q.put(port)

        threads = []
        for _ in range(args.threads):
            t = threading.Thread(target=worker, args=(ip, args.verbose, q))
            t.daemon = True
            t.start()
            threads.append(t)

        q.join()

    # Export des résultats
    if args.output:
        try:
            if args.output.endswith(".csv"):
                with open(args.output, "w", newline="") as f:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerow(["Port", "État"])
                    for port in open_ports:
                        writer.writerow([port, "Ouvert"])
            else:
                with open(args.output, "w") as f:
                    for port in open_ports:
                        f.write(f"Port {port} ouvert\n")
            print(f" Résultats enregistrés dans {args.output}")
        except Exception as e:
            print(f" Erreur de sauvegarde : {e}")

if __name__ == "__main__":
    main()