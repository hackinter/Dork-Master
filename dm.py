import sys
import time
import os

# custom speed strings
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
    os.system("pip3 install google")
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

def clear():  # clear function XD
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')

# check python version
if sys.version.startswith("3"):
    slow("[!] python3 detected ...")
    time.sleep(3)
else:
    slow("[x] you must be run using python3 ...")
    time.sleep(3)
    sys.exit(1)

# print starting XD
slow('[!] starting ... ')
time.sleep(2)
clear()
time.sleep(1)
banner()
med("""
===============================================================================
[*] coded by root@x-krypt0n-x                                               [*]
[*] Copyright 2020 SystemOfPekalongan                                       [*]
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
    time.sleep(0.5)
    print("\n[!] exit")
    sys.exit(1)

def savefile(namefile):
    with open(dork + ".txt", "a") as file:
        file.write(str(namefile))
        file.write("\n")

if namefile.lower() == "y":
    print("[!] input filename without extension")
    dork = input("[?] enter the file name : ")
else:
    print("[*] file not saved \n")

def akhir():
    try:
        dork = input("\n[*] enter your dork (e.g., 'site:.bd') : ")
        uneed = input("[?] how many results do you need : ")
        print("\n")

        requ = 0

        for results in search(dork, tld="com", lang="en", num=int(uneed), start=0, stop=None, pause=2):
            print("[*]", results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(uneed):
                break
            
            savefile(results)

    except KeyboardInterrupt:
        print("\n")
        print("[!] you pressed ctrl + c ... !")
        print("[!] exit ..")
        time.sleep(0.5)
        sys.exit(1)

    slow("[!] done ... ")
    sys.exit()

akhir()
