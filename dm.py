import sys
import time
import os

# Custom speed strings
def slow(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def med(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)

def fast(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 170)

try:
    from googlesearch import search
except ImportError:
    fast("[!] you must install google ..")
    med("[*] wait a moment, this program will install the module ...")
    os.system("pip install google")
    time.sleep(3)
    med("[*] done ...")

def banner():
    print("""
██████╗  ██████╗ ██████╗ ██╗  ██╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║  ██║██║   ██║██████╔╝█████╔╝█████╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║  ██║██║  ██╗     ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """)

def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux or Mac
        os.system('clear')

# Check Python version
if sys.version_info[0] != 3:
    slow("[x] you must be run using python3 ...")
    time.sleep(3)
    sys.exit(1)

# Print starting
slow('[!] starting ... ')
time.sleep(2)
clear()
time.sleep(1)
banner()
med(""" 
=============================================================================== 
[*] coded by HACKINTER@ANONYMIZER                                           [*] 
[*] Copyright 2024 HACKINTER                                                [*] 
[*] just simple tools to make your life easier                              [*] 
[*] Thanks to Allah. Palestine is independent                               [*] 
[*] https://github.com/hackinter (Hacking is Creative problem solving)      [*] 
===============================================================================""")
time.sleep(2)

try:
    namefile = input("\n[?] want to save the dork result file (Y/N) ").strip()
    dork = ""
except KeyboardInterrupt:
    print ("\n[!] you pressed ctrl + c")
    time.sleep(0.5)
    print("\n[!] exit")
    sys.exit(1)

def savefile(results):
    with open(f"{dork}.txt", "a") as file:
        file.write(str(results) + "\n")

if namefile.lower().startswith("y"):
    print("[!] input filename without extension")
    dork = input("[?] enter the file name : ")
else:
    print ("[*] file not saved \n")

def akhir():
    try:
        country_code = input("\n[*] enter country code (e.g., .bd for Bangladesh) : ").strip()
        dork = f"site:*{country_code}"
        uneed = input("[?] how much do you need : ")
        print("\n")

        requ = 0

        # Increase the pause time between requests to avoid 429 errors
        for results in search(dork, tld="com", lang="en", num=int(uneed), start=0, stop=None, pause=5):
            print("[*]", results)
            time.sleep(0.1)
            requ += 1
            
            # Save the results if filename is provided
            if namefile.lower().startswith("y"):
                savefile(results)
            
            if requ >= int(uneed):
                break

    except KeyboardInterrupt:
        print("\n")
        print("[!] you pressed ctrl + c ... !")
        print("[!] exit ..")
        time.sleep(0.5)
        sys.exit(1)

    slow("[!] done ... ")
    sys.exit()

akhir()
