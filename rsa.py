import random
from sympy import isprime

def large_prime(keysize):
    while True:
        num = random.randbits(keysize)
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
    
# def encrypt(pub, message):
    
# def decrypt(priv, encrypted):

def main():
    keysize = 1024
    pub, priv = generate(keysize)
    
    # message = "sample"
    # encrypted = encrypt(pub, message)
    
    # decrypted = decrypt(priv, encrypted)
    
    print(pub + "\n" + priv)
    # print(message)
    # print(encrypted)
    # print(decrypted)
    
if __name__ == "__main__":
    main()