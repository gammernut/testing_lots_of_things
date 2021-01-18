def main():
    x = get_user_input()
    get_factorial(x)


def get_user_input():
    x = int(input('enter a number to find the factorial'))
    return x


def get_factorial(x):
    factorial = 1
    if x < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif x == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, x + 1):
            factorial = factorial * i
        print("The factorial of", x, "is", factorial)

    k = input('wait')


if __name__ == '__main__':
    main()
