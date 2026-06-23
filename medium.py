def one():
    """
    Write a program that finds the largest element in a given list using a for loop.
    """
    print('\nmedium.one:')

    numbers = [3, 9, 2, 10, 5]

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print('\t', f'largest = {largest}')


def two():
    """
    Write a program that calculates the average of a list of numbers using a while loop.
    """
    print('\nmedium.two:')

    numbers = [10, 20, 30, 40]

    total = 0
    i = 0

    while i < len(numbers):
        total += numbers[i]
        i += 1

    average = total / len(numbers)

    print('\t', f'average = {average}')


def three():
    """
    Write a program that checks if a given string is a palindrome using a for loop.
    """
    print('\nmedium.three:')

    text = 'radar'

    is_palindrome = True

    for i in range(len(text)):
        if text[i] != text[len(text)-1-i]:
            is_palindrome = False

    if is_palindrome:
        print('\t', f'"{text}" is a palindrome')
    else:
        print('\t', f'"{text}" is not a palindrome')


def four():
    """
    Write a program that prints the first n terms of the geometric sequence using a while loop.
    """
    print('\nmedium.four:')

    n = 10
    term = 2
    ratio = 2

    count = 0

    while count < n:
        print('\t', term)
        term *= ratio
        count += 1


def five(number):
    """
    Write a program that finds the second largest element in a given list using a for loop.
    """
    print('\nmedium.five:')

    numbers = [3, 9, 2, number, 5]

    largest = numbers[0]
    second_largest = numbers[0]

    for value in numbers:
        if value > largest:
            second_largest = largest
            largest = value
        elif value > second_largest and value != largest:
            second_largest = value

    print('\t', f'second largest = {second_largest}')


def six(number):
    """
    Write a program that calculates the factorial of a given number using a while loop.
    """
    print('\nmedium.six:')

    factorial = 1

    while number > 0:
        factorial *= number
        number -= 1

    print('\t', factorial)


def seven():
    """
    Write a program that checks if a given number is a perfect square using a for loop.
    """
    print('\nmedium.seven:')

    number = 25

    is_square = False

    for i in range(1, number + 1):
        if i * i == number:
            is_square = True

    print('\t', f'{number} perfect square = {is_square}')


def eight(number):
    """
    Write a program that prints the sum of all prime numbers between 1 and 100 using a while loop.
    """
    print('\nmedium.eight:')

    total = 0
    n = 2

    while n <= 100:

        divisor = 2
        is_prime = True

        while divisor < n:
            if n % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            total += n

        n += 1

    print('\t', f'sum of primes = {total}')


def nine():
    """
    Write a program that counts the number of words in a given sentence using a for loop.
    """
    print('\nmedium.nine:')

    sentence = "Hello world this is python"

    words = sentence.split()

    total = 0

    for word in words:
        total += 1

    print('\t', f'word count = {total}')


def ten():
    """
    Write a program that prints the common elements between two lists using a while loop.
    """
    print('\nmedium.ten:')

    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]

    i = 0

    while i < len(list1):
        if list1[i] in list2:
            print('\t', list1[i])

        i += 1