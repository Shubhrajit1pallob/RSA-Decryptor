factors = []

def find_prime_factors(num: int):
    global factors
    if num == 1:
        return [1]
    
    n = 2

    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    if num > 1:
        factors.append(num)

    return factors


def find_mod_inverse(e: int, t: int):
    m0, x0, x1 = t, 0, 1
    while e > 1:
        q = e // t
        t, e = e % t, t
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def find_the_totient(factors: list):
    n = 1
    for i in factors:
        n *= (i - 1)
    return n

def decrypt_message(encrypted_message: int, private_key: int, n: int):
    factors = find_prime_factors(n)
    t = find_the_totient(factors)
    if t > 0:
        d = find_mod_inverse(private_key, t)
    else:
        raise ValueError("Modulus must be greater than 0.")
        
    plain_text = pow(encrypted_message, d) % n
    
    return plain_text

# if __name__ == "__main__":
#     num = int(input("Enter a number to find its prime factors: "))
#     factors = find_prime_factors(num)
#     print(f"Prime factors of {num} are: {factors}")

#     t = find_the_totient(factors)

#     e = int(input("Enter the value e: "))
#     if t > 0:
#         d = find_mod_inverse(e, t)
#         print(f"Modular inverse of {e} mod {t} is: {d}")
#     else:
#         print("Modulus must be greater than 0.")