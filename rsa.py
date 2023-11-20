import random
from sympy import isprime

def large_prime():
    
def generate(keysize):
    
def encrypt(pub, message):
    
def decrypt(priv, encrypted):

def main():
    keysize = 1024
    pub, priv = generate(keysize)
    
    message = "sample"
    encrypted = encrypt(pub, message)
    
    decrypted = decrypt(priv, encrypted)
    
    print(pub + "\n" + priv)
    print(message)
    print(encrypted)
    print(decrypted)
    
if __name__ == "__main__":
    main()