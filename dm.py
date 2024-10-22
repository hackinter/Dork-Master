import sys
import time
import os

# custom speed strings
def slow(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2)  # Increased to 2 seconds

def med(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2)  # Kept at 2 seconds

def fast(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2)  # Increased to 2 seconds

try:
    from googlesearch import search
except ImportError:
    fast("[!] you must install google ..")
    med("[*] wait a moment, this program will install the module ...")
    os.system("pip3 install google")
    time.sleep(3)
    med("[*] done ...")

def banner():
    print("""\
██████╗  ██████╗ ██████╗ ██╗  ██╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║  ██║██║   ██║██████╔╝█████╔╝█████╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║  ██║██║  ██╗     ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """)

def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')

# check python version   
if sys.version.startswith("3"):
    slow("[!] python3 detected ...")
    time.sleep(2)  # Increased to 2 seconds
else:
    slow("[x] you must be run using python3 ...")
    time.sleep(2)  # Increased to 2 seconds
    sys.exit(1)

# print starting
slow('[!] starting ... ')
time.sleep(2)
clear()
time.sleep(2)
banner()
med(""" 
=============================================================================== 
[*] coded by root@HACKINTER                                                 [*] 
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
    print("\n[!] you pressed ctrl + c")
    time.sleep(2)  # Increased to 2 seconds
    print("\n[!] exit")
    sys.exit(1)

def savefile(result, dork_name):
    with open(f"{dork_name}.txt", "a") as file:
        file.write(str(result) + "\n")

if namefile.lower().startswith("y"):
    print("[!] input filename without extension")
    dork = input("[?] enter the file name : ")
else:
    print("[*] file not saved \n")

def akhir():
    try:
        country_code = input("\n[*] enter country code (e.g., .bd for Bangladesh) : ").strip()
        dork_query = f"site:*{country_code}"
        uneed = input("[?] how much do you need : ")
        print("\n")

        requ = 0

        for results in search(dork_query, tld="com", lang="en", num=int(uneed), start=0, stop=None, pause=2):
            print("[*]", results)
            time.sleep(2)  # Increased to 2 seconds
            requ += 1
            if requ >= int(uneed):
                break

            if dork:  # Check if dork is not empty
                savefile(results, dork)
            time.sleep(2)  # Increased to 2 seconds

    except KeyboardInterrupt:
        print("\n")
        print("[!] you pressed ctrl + c ... !")
        print("[!] exit ..")
        time.sleep(2)  # Increased to 2 seconds
        sys.exit(1)

    slow("[!] done ... ")
    sys.exit()

akhir()
