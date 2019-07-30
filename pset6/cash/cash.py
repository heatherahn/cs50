from cs50 import get_float

def main():
    while True:
        change = get_float("Change owed: ")
        if change > 0:
            break

    cents = round(change * 100)

    q, d, n, p = 0, 0, 0, 0

    while cents >= 25:
        cents = cents - 25
        q+=1

    while cents >= 10:
        cents = cents - 10
        d+=1

    while cents >= 5:
        cents = cents - 5
        n+=1

    while cents >= 1:
        cents = cents - 1
        p+=1

    coins = q + d + n + p

    print(str(coins) + " is the fewest number of coins for change")

if __name__ == "__main__":
    main()