Brute Force Password Cracker

Overview

This Brute Force Password Cracker attempts to crack hashed passwords using two methods:

Dictionary Attack – Tries passwords from a predefined wordlist.

Brute-Force Attack – Generates all possible character combinations up to a given length.

Features

Supports hashing algorithms (MD5, SHA-1, SHA-256, etc.).

Uses dictionary files for faster cracking.

Can brute-force short passwords by generating combinations.

Prerequisites

Python 3.x

Installation

# Clone the repository
git clone https://github.com/yourusername/Brute-Force-Cracker.git
cd Brute-Force-Cracker

# Install dependencies (if any, currently none)
pip install -r requirements.txt

Usage

Brute-force attack

python3 src/brute_force.py

Dictionary attack

Modify wordlist.txt and run:

python3 src/brute_force.py --wordlist wordlist.txt

Notes

The brute-force attack is slow for long passwords.

Use a strong wordlist for dictionary attacks.

License

This project is licensed under the MIT License.

