from math import gcd

def RSA(p: int, q: int, m: int):
    n=p*q
    t=(p-1)*(q-1)
    for i in range(2, t):
        if gcd(i, t) == 1:
            encrypt = i
            break
    j = 1
    while True:
        if (j * encrypt) % t == 1:
            decrypt = r
            break
        j += 1
    cipher = (m ** encrypt) % n
    print(f"Encrypted message is {cipher}")
    message = (cipher ** decrypt) % n
    print(f"Decrypted message is {message}")
RSA(p=11,q=13,m=13)
