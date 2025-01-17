#!/bin/bash

clear_terminal() {
    clear  # 'clear' কমান্ডটি সব প্ল্যাটফর্মে কাজ করবে, তাই 'if' শাখা ত্যাগ করা হয়েছে
}

# Function to check if Python3 is installed
check_python() {
    if ! command -v python3 &>/dev/null; then
        echo "[!] Python3 is not installed. Please install it and try again."
        exit 1
    fi
}

# Function to call Python script for Google search
perform_python_search() {
    python3 pyshell.py "$1" "$2" "$3" "$4" "$5"
}

# Main function
main() {
    clear_terminal
    echo "===============================================================================" 
    echo "[*] Coded by ROOT@ANONYMIZER"
    echo "[*] Copyright 2024 HACKINTER"
    echo "[*] Simple tool to enhance your Google search capabilities"
    echo "[*] Thanks to ALLAH, Free Palestine"
    echo "==============================================================================="

    check_python

    read -p "[?] Save results to a file? (Y/N): " save_option
    save_results=false
    if [[ "$save_option" == "Y" || "$save_option" == "y" ]]; then
        save_results=true
        read -p "[?] Enter filename (without extension): " filename
    fi

    read -p "[?] How many results do you need? " num_results

    # Checking if the entered number is a valid integer
    while ! [[ "$num_results" =~ ^[0-9]+$ ]]; do
        echo "[!] Invalid input. Please enter a valid number."
        read -p "[?] How many results do you need? " num_results
    done

    read -p "[?] Enter your dork query (use space for multiple queries): " dorks

    # Call the Python script and pass parameters
    perform_python_search "$dorks" "$num_results" "$save_results" "$filename"
}

# Call main function
main
