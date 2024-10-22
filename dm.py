import time
import os
import sys
from googlesearch import search

def clear_terminal():
    # সিস্টেমের টার্মিনাল পরিষ্কার করা
    os.system('cls' if os.name == 'nt' else 'clear')

def display_intro():
    print("██████╗  ██████╗ ██████╗ ██╗  ██╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ ")
    print("██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗")
    print("██║  ██║██║   ██║██████╔╝█████╔╝█████╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝")
    print("██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗")
    print("██████╔╝╚██████╔╝██║  ██║██║  ██╗     ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║")
    print("╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
    print("\n===============================================================================")
    print("[*] coded by HACKINTER@ANONYMIZER")
    print("[*] Copyright 2024 HACKINTER")
    print("[*] just simple tools to make your life easier")
    print("[*] Thanks to Allah. Palestine is independent")
    print("[*] https://github.com/hackinter (Hacking is Creative problem solving)")
    print("===============================================================================\n")
    print("[✔] Done loading!")
    time.sleep(1)  # এক সেকেন্ড অপেক্ষা করুন

def get_input():
    want_save = input("[?] want to save the dork result file (Y/N): ").strip().lower()
    if want_save == 'y':
        filename = input("[?] input filename without extension: ").strip()
        country_code = input("[*] enter country code (e.g., .bd for Bangladesh): ").strip()
        num_results = input("[?] how much do you need: ").strip()

        return filename, country_code, num_results
    else:
        sys.exit("Exiting the program.")

def search_results(dork, tld, lang, num, country_code):
    try:
        results = []
        for result in search(dork, tld=tld, lang=lang, num=int(num), stop=None, pause=3):  # পালস বাড়িয়ে দিন
            results.append(result)
        return results
    except Exception as e:
        print(f"[!] An error occurred: {e}")
        return None

def save_results(filename, results):
    with open(f"{filename}.txt", "w") as file:
        for result in results:
            file.write(result + "\n")
    print(f"[✔] Results saved in {filename}.txt")

def main():
    clear_terminal()
    display_intro()
    filename, country_code, num_results = get_input()
    dork = f"site:{country_code}"  # Dork তৈরি করুন

    results = search_results(dork, "com", "en", num_results, country_code)

    if results:
        save_results(filename, results)
    else:
        print("[!] No results found or an error occurred.")

if __name__ == "__main__":
    main()
