import hashlib
import itertools

def hash_password(password, algorithm='sha256'):
    """Hashes a password using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    hash_func.update(password.encode('utf-8'))
    return hash_func.hexdigest()

def brute_force_attack(hash_value, charset, max_length, algorithm='sha256'):
    """Attempts to brute-force a hashed password by generating possible passwords."""
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt_password = ''.join(attempt)
            if hash_password(attempt_password, algorithm) == hash_value:
                return attempt_password
    return None

def dictionary_attack(hash_value, wordlist, algorithm='sha256'):
    """Attempts to crack a hashed password using a wordlist."""
    with open(wordlist, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if hash_password(word, algorithm) == hash_value:
                return word
    return None

if __name__ == "__main__":
    test_hash = hash_password("password123")
    print("Testing brute-force attack...")
    result = brute_force_attack(test_hash, "abcdefghijklmnopqrstuvwxyz", 4)
    print("Cracked Password:", result)
