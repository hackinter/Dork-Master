from bs4 import BeautifulSoup
import requests
import sys
import time
import os
from termcolor import colored

def slow(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

def med(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

def fast(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.006)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    banner_text = """
    ██████╗  ██████╗ ██████╗ ██╗  ██╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ██║  ██║██║   ██║██████╔╝█████╔╝█████╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
    ██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝██║  ██║██║  ██╗     ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """
    slow(banner_text)

def validate_python_version():
    if not sys.version.startswith("3"):
        slow("[x] This script requires Python 3. Exiting...")
        sys.exit(1)
    slow("[!] Python 3 detected. Proceeding...")
    time.sleep(1)

def save_to_file(filename, content):
    with open(f"{filename}.txt", "a", encoding="utf-8") as file:
        file.write(content + "\n")

def perform_search(dork, num_results, save_results=False, filename=None):
    fast("[+] Performing Google search...\n")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
    query = f"https://www.google.com/search?q={dork}&num={num_results}"
    try:
        response = requests.get(query, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("a")
            count = 0
            for result in results:
                link = result.get("href")
                if link and "/url?q=" in link:
                    link = link.split("/url?q=")[1].split("&sa=")[0]
                    print(colored(f"[*] {link}", "yellow"))
                    count += 1
                    if save_results and filename:
                        save_to_file(filename, link)
                    if count >= int(num_results):
                        break
            fast(f"\n[!] Total results found: {count}\n")
        else:
            fast("[!] Failed to fetch results from Google.")

    except Exception as e:
        fast(f"\n[!] An error occurred: {str(e)}")
        sys.exit(1)

def main():
    clear()
    banner()
    med("""
=============================================================================== 
[*] Coded by ROOT@ANONYMIZER                                                [*] 
[*] Copyright 2024 HACKINTER                                                [*] 
[*] Simple tool to enhance your Google search capabilities                  [*] 
[*] Thanks to ALLAH, Free Palestine                                         [*] 
===============================================================================
""")

    validate_python_version()

    try:
        save_option = input(colored("\n[?] Save results to a file? (Y/N): ", "cyan")).strip().lower()
        save_results = save_option == "y"

        if save_results:
            filename = input(colored("[?] Enter filename (without extension): ", "cyan")).strip()
        else:
            filename = None

        num_results = input(colored("[?] How many results do you need? ", "cyan")).strip()
        dork = input(colored("[?] Enter your dork query: ", "cyan")).strip()

        perform_search(dork, num_results, save_results, filename)

    except KeyboardInterrupt:
        fast("\n[!] Program interrupted by user.")
        sys.exit(1)

    slow("[!] Search completed successfully. Exiting...")

if __name__ == "__main__":
    main()
