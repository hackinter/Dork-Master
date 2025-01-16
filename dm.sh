#!/bin/bash

# Function to print slow output
slow() {
    for c in $1; do
        echo -n "$c"
        sleep 0.04
    done
    echo
}

# Function to print medium output
med() {
    for c in $1; do
        echo -n "$c"
        sleep 0.02
    done
    echo
}

# Function to print fast output
fast() {
    for c in $1; do
        echo -n "$c"
        sleep 0.006
    done
    echo
}

# Clear the terminal screen
clear() {
    if [ "$(uname)" == "Darwin" ]; then
        clear
    else
        clear
    fi
}

# Function to display the banner
banner() {
    slow "██████╗  ██████╗ ██████╗ ██╗  ██╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ "
    slow "██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗"
    slow "██║  ██║██║   ██║██████╔╝█████╔╝█████╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝"
    slow "██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗"
    slow "██████╔╝╚██████╔╝██║  ██║██║  ██╗     ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║"
    slow "╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝"
}

# Function to validate Python version (Shifting to shell equivalent)
validate_python_version() {
    python_version=$(python3 --version 2>&1)
    if [[ $python_version != *"Python 3"* ]]; then
        slow "[x] This script requires Python 3. Exiting..."
        exit 1
    fi
    slow "[!] Python 3 detected. Proceeding..."
    sleep 1
}

# Function to save results to a file
save_to_file() {
    echo "$1" >> "$2.txt"
}

# Function to perform Google search
perform_search() {
    slow "[+] Performing Google search..."
    query="https://www.google.com/search?q=$1&num=$2"
    links=$(curl -s "$query" | grep -oP '/url\?q=\K[^&]+')

    count=0
    for link in $links; do
        echo "[*] $link"
        count=$((count + 1))
        if [ "$3" == "true" ]; then
            save_to_file "$link" "$4"
        fi
        if [ "$count" -ge "$2" ]; then
            break
        fi
    done
    fast "[!] Total results found: $count"
}

# Main function
main() {
    clear
    banner
    med "=============================================================================== "
    med "[*] Coded by ROOT@ANONYMIZER"
    med "[*] Copyright 2024 HACKINTER"
    med "[*] Simple tool to enhance your Google search capabilities"
    med "[*] Thanks to ALLAH, Free Palestine"
    med "==============================================================================="

    read -p "[?] Save results to a file? (Y/N): " save_option
    save_results=false
    if [[ "$save_option" == "Y" || "$save_option" == "y" ]]; then
        save_results=true
        read -p "[?] Enter filename (without extension): " filename
    fi

    read -p "[?] How many results do you need? " num_results
    read -p "[?] Enter your dork query: " dork

    perform_search "$dork" "$num_results" "$save_results" "$filename"

    slow "[!] Search completed successfully. Exiting..."
}

# Call main function
main
