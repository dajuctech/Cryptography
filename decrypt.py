import time
# Input...
ciphertext = input("Enter the ciphertext to decrypt: ")
key = int(input("Input the key used to encrypt the message (a number between 1 and 10): "))

def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(0, len(ciphertext)):
        if i % (key+1) == 0:
            plaintext += ciphertext[i]
    return plaintext

while not (key >= 1 and key <= 10):
    print("Invalid key, try again!")
    key = int(input("Input the key used to encrypt the message (a number between 1 and 10): "))

# Process... 
print("...")
time.sleep(1)
print("Decrypting ciphertext...")
time.sleep(1)
print("...")
time.sleep(1)

plaintext = decrypt(ciphertext, key)

# Output...
print("Plaintext:")
print(plaintext)
