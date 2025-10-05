# Calculating the bit length
import math

def bit_length(password):

    if not password:
        return 0
    bit = 0

    if any(c.isupper() for c in password):
        bit += 26
    if any(c.islower() for c in password):
        bit += 26
    if any(c.isdigit() for c in password):
        bit += 10
    if any(not c.isalnum() for c in password):
        bit += 32
        
    return math.log2(bit)

def verify_password_strength(password):
    bit = bit_length(password)
    length = len(password)
    entropy = bit * length
    print(length)
    return math.floor(entropy)

