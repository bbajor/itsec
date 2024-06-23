#!/usr/bin/python

import subprocess
import sys

def read_wordlist(file_path):
    with open(file_path, 'r', encoding = "ISO-8859-1") as file:
        return [line.strip() for line in file]

def run_gobuster_scan(hostname, wordlist_dir, wordlist_subdirs_path):
    try:
        command = ['gobuster', 'dir', '-u', hostname + "/", '-w', wordlist_subdirs_path] #, '-x', 'txt']
        print(f"Running: {' '.join(command)}")
        result = subprocess.run(command, stdout=None, stderr=None, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error running gobuster: {e}", file=sys.stderr)

def recursive_scan(hostname, wordlist_a, wordlist_b):
    for directory in wordlist_a:
        subdir_url = f"{hostname}/{directory}"
        print(f"Scanning {subdir_url}...")
        run_gobuster_scan(subdir_url, directory, wordlist_b_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <known_directories> <common_dir_wordlist> <hostname>")
        sys.exit(1)

    wordlist_a_path = sys.argv[2]
    wordlist_b_path = sys.argv[3]
    hostname = sys.argv[1]

    wordlist_a = read_wordlist(wordlist_a_path)

    recursive_scan(hostname, wordlist_a, wordlist_b_path)
