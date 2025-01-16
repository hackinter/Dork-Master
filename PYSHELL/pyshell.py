import sys
import requests
from bs4 import BeautifulSoup
import time
import os

def save_to_file(filename, content):
    try:
        with open(f"{filename}.txt", "a", encoding="utf-8") as file:
            file.write(content + "\n")
    except Exception as e:
        print(f"[!] Error saving to file: {str(e)}")

def perform_search(dorks, num_results, save_results=False, filename=None):
    print("[+] Performing Google search...\n")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
    
    dork_list = dorks.split()  # Split if multiple queries are provided
    for dork in dork_list:
        print(f"[+] Searching for: {dork}")
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
                        print(f"[*] {link}")
                        count += 1
                        if save_results and filename:
                            save_to_file(filename, link)
                    if count >= int(num_results):
                        break
                print(f"\n[!] Total results found for '{dork}': {count}\n")
            else:
                print(f"[!] Failed to fetch results for '{dork}'.")
        except Exception as e:
            print(f"\n[!] An error occurred for '{dork}': {str(e)}")

def main():
    if len(sys.argv) < 5:
        print("[!] Usage: python script.py <dorks> <num_results> <save_results> <filename (if save_results=true)>")
        sys.exit(1)

    dorks = sys.argv[1]
    num_results = sys.argv[2]
    save_results = sys.argv[3].lower() == 'true'
    filename = sys.argv[4] if save_results else None

    # Add delay between searches to prevent blocking
    time.sleep(1)

    perform_search(dorks, num_results, save_results, filename)

if __name__ == "__main__":
    main()
