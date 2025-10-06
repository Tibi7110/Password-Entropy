from password import verify_password_strength
import math

def get_input():
    val = input("Enter your value: ")

    return val

def main():
    password = get_input()
    print("Processing ...")
    bit = verify_password_strength(password)
    if bit <= 15:
        print("Very weak password")
        return
    if bit <= 30:
        print("Weak password")
        return
    if bit <= 45:
        print("Medium strength password")
        return
    if bit <= 60:
        print("Strong password")
        return
    if bit <= 75:
        print("Very strong password")
        return
    
    print("Extremely strong password")
    return

if __name__=="__main__":
    main()