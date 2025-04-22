import hashlib

# Hashed password (target)
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

# Sample dictionary (you can load from a file)
dictionary = ["123456", "admin", "letmein", "password", "welcome"]

for word in dictionary:
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    if hashed_word == target_hash:
        print(f"[+] Password found: {word}")
        break
else:
    print("[-] Password not found.")
