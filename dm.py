import os
import sys
import time
import random
from googlesearch import search

def savefile(results, filename):
    with open(f"{filename}.txt", "a") as f:
        f.write(results + "\n")

def slow(message):
    print(message)
    time.sleep(1)

def display_banner():
    banner = """
██████╗  ██████╗ ██████╗ ██╗  ██╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║  ██║██║   ██║██████╔╝█████╔╝█████╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║  ██║██║  ██╗     ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """
    print(banner)
    print("===============================================================================")
    print("[*] coded by HACKINTER@ANONYMIZER")
    print("[*] Copyright 2024 HACKINTER")
    print("[*] just simple tools to make your life easier")
    print("[*] Thanks to Allah. Palestine is independent")
    print("[*] https://github.com/hackinter (Hacking is Creative problem solving)")
    print("===============================================================================")

def clear_terminal():
    os.system('clear' if os.name != 'nt' else 'cls')

def animate_loading():
    loading_animation = ["[•]", "[◐]", "[◓]", "[◑]"]
    for _ in range(10):  # Animation loop
        for frame in loading_animation:
            print("\r" + frame, end="")
            time.sleep(0.2)
    print("\r[✔] Done loading!          ")

def akhir():
    try:
        filename = input("[?] input filename without extension: ").strip()
        country_code = input("[*] enter country code (e.g., .bd for Bangladesh): ").strip()
        dork = f"site:*{country_code}"
        uneed = input("[?] how much do you need: ")
        print("\n")

        requ = 0

        # Custom user agent
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

        for results in search(dork, tld="com", lang="en", num=int(uneed), start=0, stop=None, pause=random.uniform(5, 10), user_agent=user_agent):
            print("[*]", results)
            savefile(results, filename)
            requ += 1
            
            if requ >= int(uneed):
                break

        slow("[!] done ... ")
        
    except KeyboardInterrupt:
        print("\n")
        print("[!] you pressed ctrl + c ... !")
        print("[!] exit ..")
        time.sleep(0.5)
        sys.exit(1)

    except Exception as e:
        print(f"[!] An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    clear_terminal()  # Clear the terminal
    display_banner()  # Call the function to display the banner
    animate_loading()  # Call the loading animation

    save_result = input("[?] want to save the dork result file (Y/N): ").strip().lower()
    if save_result == 'y':
        akhir()
    else:
        print("[*] Exiting without saving.")
        sys.exit(0)
