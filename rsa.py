import random
from math import gcd
from sympy import isprime

def large_prime(keysize):
    while True:
        num = random.getrandbits(keysize)
        if isprime(num):
            return num
        
def generate(keysize):
    p = large_prime(keysize)
    q = large_prime(keysize)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))
    
def encrypt(pub, message):
    e, n = pub
    encrypted = []
    for char in message:
        m = ord(char)
        c = pow(m, e, n)
        encrypted.append(c)
    return encrypted
    
def decrypt(priv, encrypted):
    d, n = priv
    decrypted = ""
    for num in encrypted:
        m = pow(num, d, n)
        char = chr(m)
        decrypted += char
    return decrypted

def main():
    keysize = 1024
    pub, priv = generate(keysize)
    message = "sample"
    encrypted = encrypt(pub, message)
    decrypted = decrypt(priv, encrypted)
    print(pub)
    print(priv)
    print(message)
    print(encrypted)
    print(decrypted)
    
if __name__ == "__main__":
    main()