from password import verify_password_strength
import math

def get_input():
    val = input("Enter your value: ")

    return val

def main():
    password = get_input()
    print("Processing ...")
    bit = verify_password_strength(password)
    print(bit)

if __name__=="__main__":
    main()