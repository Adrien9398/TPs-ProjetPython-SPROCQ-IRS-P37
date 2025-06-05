import re
import pandas as pd
import matplotlib.pyplot as plt

def parse_log_line(line):
    pattern = (
        r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] '
        r'"(?P<method>\S+)? (?P<url>\S+)? \S+" (?P<status>\d{3}) \S+ '
        r'"[^"]*" "(?P<user_agent>[^"]*)"'
    )
    match = re.match(pattern, line)
    return match.groupdict() if match else None

def load_log_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        data = [parse_log_line(line) for line in f if parse_log_line(line)]
    df = pd.DataFrame(data)
    df['status'] = df['status'].astype(int)
    return df

def get_404_errors(df):
    df_404 = df[df['status'] == 404]
    print("\nErreurs 404 :\n", df_404.head())
    return df_404

def top_5_ips(df_404):
    top = df_404['ip'].value_counts().head(5)
    print("\nTop 5 IPs fautives :\n", top)
    return top

def plot_404_errors(top_ips):
    top_ips.plot(kind='bar', color='coral', figsize=(10, 6))
    plt.title("Top 5 IPs - Erreurs 404")
    plt.xlabel("IP")
    plt.ylabel("Nombre d'erreurs")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def detect_bots(df_404):
    bots = df_404[df_404['user_agent'].str.contains('bot|crawler|spider', case=False, na=False)]
    bot_ips = bots['ip'].value_counts()
    pct = (len(bots) / len(df_404)) * 100 if len(df_404) else 0
    print(f"\n=== Bots détectés ===\n{bot_ips}")
    print(f"\n% erreurs 404 dues aux bots : {pct:.2f}%")
    return bots

def main():
    df = load_log_file("access.log")
    print("\nAperçu :\n", df.head())

    df_404 = get_404_errors(df)
    top_ips = top_5_ips(df_404)
    plot_404_errors(top_ips)
    detect_bots(df_404)

if __name__ == "__main__":
    main()