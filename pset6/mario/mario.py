from cs50 import get_int

# get positive integer for height from user
def main():

    while True:
        h = get_int("Height: ")
        if h >= 1 and h <= 8:
            break

# iterate over rows
    for i in range (1, h + 1):
        spaces = h - i
        hashes = i
        # print spaces
        print(" " * spaces, end="")
        # print hashtags
        print("#" * hashes, end="")
        print()

if __name__ == "__main__":
    main()
