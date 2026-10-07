# Program: Fibonacci Series
# Author: M.Pallavi


def generate_fibonacci(count):
    series = []

    first = 0
    second = 1

    for _ in range(count):
        series.append(first)
        first, second = second, first + second

    return series


def main():
    print("================================")
    print("        FIBONACCI SERIES")
    print("================================")

    try:
        count = int(input("Enter number of terms: "))

        if count <= 0:
            print("\nPlease enter a positive number.")
            return

        series = generate_fibonacci(count)

        print("\nFibonacci Series:")
        print(*series)

        print("\nNumber of Terms :", count)
        print("First Term      :", series[0])
        print("Last Term       :", series[-1])
        print("Sum of Terms    :", sum(series))

    except ValueError:
        print("\nInvalid input!")
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
