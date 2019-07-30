import sys
from cs50 import get_string

def main():

    n = len(sys.argv[1])

    if len(sys.argv) == 2:
        for i in range (n):
            third = sys.argv[1][i]
            if third.isdigit() == False:
                print("Usage: python ex.py key")
                return 0
        key = int(sys.argv[1])
    else:
        print("Usage: python ex.py key")

# prompt user for plaintext
    while True:
        plaintext = get_string("Plaintext: ")
        if plaintext.isalpha() == True:
            break

    length = len(plaintext)
    print("Ciphertext: ", end="")

# iterate over strings
    for j in range (length):
        if plaintext.isalpha == False:
            print(plaintext[j], end="")
        else:
            if plaintext[j].islower() == True:
                translate = ord(plaintext[j])
                temp = (((translate - 97 + key) % 26) + 97)
                print(chr(temp), end="")
            else:
                translate = (ord(plaintext[j]))
                temp = (((translate - 65 + key) % 26) + 65)
                print(chr(temp), end="")
    print()


if __name__ == "__main__":
    main()