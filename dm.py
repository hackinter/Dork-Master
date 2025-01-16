from bs4 import BeautifulSoup
from googlesearch import search
import requests
import sys
import time
import os
from termcolor import colored


# Text display with delays for better user experience
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


# Clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Display the banner
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


# Validate the Python version
def validate_python_version():
    if not sys.version.startswith("3"):
        slow("[x] This script requires Python 3. Exiting...")
        sys.exit(1)
    slow("[!] Python 3 detected. Proceeding...")
    time.sleep(1)


# Save results to a file
def save_to_file(filename, content):
    with open(f"{filename}.txt", "a", encoding="utf-8") as file:
        file.write(content + "\n")


# Perform the search
def perform_search(dork, num_results, save_results=False, filename=None):
    fast("[+] Performing Google search...\n")
    try:
        results = []
        for link in search(dork, num=int(num_results), pause=2):
            print(colored(f"[*] {link}", "yellow"))
            results.append(link)
            if save_results and filename:
                save_to_file(filename, link)

        fast(f"\n[!] Total results found: {len(results)}\n")

    except Exception as e:
        fast(f"\n[!] An error occurred: {str(e)}")
        sys.exit(1)


# Main function
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
