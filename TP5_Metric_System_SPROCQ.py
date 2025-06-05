import psutil
import os
import platform
import time

def clear_screen():
    """Efface l'écran selon l'OS"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def display_cpu_usage():
    print("=== Utilisation CPU ===")
    cpu_percents = psutil.cpu_percent(percpu=True)
    for i, percent in enumerate(cpu_percents):
        bar = "#" * int(percent / 5)
        print(f"  Coeur {i}: {percent:.1f}% | {bar}")
    total = psutil.cpu_percent()
    print(f"  Total CPU: {total:.1f}%\n")

def display_memory_info():
    print("=== Mémoire RAM ===")
    mem = psutil.virtual_memory()
    print(f"  Totale: {mem.total // (1024 ** 2)} Mo")
    print(f"  Utilisée: {mem.used // (1024 ** 2)} Mo")
    print(f"  Libre: {mem.available // (1024 ** 2)} Mo\n")

def display_disk_info():
    print("=== Utilisation Disque ===")
    partitions = psutil.disk_partitions()
    for part in partitions:
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"  {part.device} ({part.mountpoint}) - Utilisé: {usage.percent:.1f}%")
        except PermissionError:
            continue
    print()

def display_network_info():
    print("=== Activité Réseau ===")
    net_io = psutil.net_io_counters()
    print(f"  Octets envoyés: {net_io.bytes_sent}")
    print(f"  Octets reçus: {net_io.bytes_recv}")
    print(f"  Paquets envoyés: {net_io.packets_sent}")
    print(f"  Paquets reçus: {net_io.packets_recv}\n")

    print("=== Statistiques par Interface ===")
    net_stats = psutil.net_io_counters(pernic=True)
    for iface, stats in net_stats.items():
        print(f"  {iface}: Envoyés: {stats.bytes_sent} | Reçus: {stats.bytes_recv}")
    print()

def display_temperature_info():
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        if temps:
            print("=== Température CPU ===")
            for name, entries in temps.items():
                for entry in entries:
                    print(f"  {name} - {entry.label or 'CPU'}: {entry.current}°C")
            print()

def export_to_log():
    with open("system_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- {time.ctime()} ---\n")
        
        cpu_percents = psutil.cpu_percent(percpu=True)
        f.write("Utilisation CPU:\n")
        for i, percent in enumerate(cpu_percents):
            f.write(f"  Coeur {i}: {percent:.1f}%\n")
        total = psutil.cpu_percent()
        f.write(f"  Total CPU: {total:.1f}%\n\n")
        
        mem = psutil.virtual_memory()
        f.write("Mémoire RAM:\n")
        f.write(f"  Totale: {mem.total // (1024 ** 2)} Mo\n")
        f.write(f"  Utilisée: {mem.used // (1024 ** 2)} Mo\n")
        f.write(f"  Libre: {mem.available // (1024 ** 2)} Mo\n\n")
        f.write("Utilisation Disque:\n")
        partitions = psutil.disk_partitions()
        for part in partitions:
            try:
                usage = psutil.disk_usage(part.mountpoint)
                f.write(f"  {part.device} ({part.mountpoint}) - Utilisé: {usage.percent:.1f}%\n")
            except PermissionError:
                continue
        f.write("\n")
        
        net_io = psutil.net_io_counters()
        f.write("Activité Réseau:\n")
        f.write(f"  Octets envoyés: {net_io.bytes_sent}\n")
        f.write(f"  Octets reçus: {net_io.bytes_recv}\n")
        f.write(f"  Paquets envoyés: {net_io.packets_sent}\n")
        f.write(f"  Paquets reçus: {net_io.packets_recv}\n\n")
        
        f.write("Statistiques par Interface:\n")
        net_stats = psutil.net_io_counters(pernic=True)
        for iface, stats in net_stats.items():
            f.write(f"  {iface}: Envoyés: {stats.bytes_sent} | Reçus: {stats.bytes_recv}\n")
        f.write("\n")

        if hasattr(psutil, "sensors_temperatures"):
            temps = psutil.sensors_temperatures()
            if temps:
                f.write("Température CPU:\n")
                for name, entries in temps.items():
                    for entry in entries:
                        f.write(f"  {name} - {entry.label or 'CPU'}: {entry.current}°C\n")
                f.write("\n")

def display_dashboard():
    try:
        while True:
            clear_screen()
            display_cpu_usage()
            display_memory_info()
            display_disk_info()
            display_network_info()
            display_temperature_info()
            export_to_log() 

            print("Actualisation dans 5 secondes... (Ctrl+C pour quitter)")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nArrêt du tableau de bord par l'utilisateur.")

if __name__ == "__main__":
    display_dashboard()