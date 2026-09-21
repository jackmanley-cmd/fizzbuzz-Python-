def fizzbuzz(number):
    # Check if the number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


# Run FizzBuzz for numbers 1 to 100
if __name__ == "__main__":
    for number in range(1, 101):
        print(fizzbuzz(number))
