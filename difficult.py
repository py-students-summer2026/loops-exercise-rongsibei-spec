def one():
    """
    Write a program that finds the prime factors of a given number using a for loop.
    """
    print('\ndifficult.one:')

    number = 12

    for i in range(2, number + 1):

        if number % i == 0:

            is_prime = True

            for j in range(2, i):
                if i % j == 0:
                    is_prime = False

            if is_prime:
                print('\t', i)


def two():
    """
    Write a program that calculates the nth term of the Fibonacci sequence using a while loop.
    """
    print('\ndifficult.two:')

    n = 10

    a = 0
    b = 1
    count = 0

    while count < n:
        total = a + b
        a = b
        b = total
        count += 1

    print('\t', a)


def three():
    """
    Write a program that checks if a given string is an anagram using a for loop.
    """
    print('\ndifficult.three:')

    word1 = "listen"
    word2 = "silent"

    is_anagram = True

    for letter in word1:
        if word1.count(letter) != word2.count(letter):
            is_anagram = False

    print('\t', is_anagram)


def four():
    """
    Write a program that prints the first n terms of the arithmetic sequence using a while loop.
    """
    print('\ndifficult.four:')

    term = 2
    difference = 2
    count = 0

    while count < 10:
        print('\t', term)

        term += difference
        count += 1


def five(number):
    """
    Write a program that finds the median of a given list of numbers using a for loop.
    """
    print('\ndifficult.five:')

    numbers = [1, 3, 5, 7, 9, number]

    numbers.sort()

    middle = len(numbers) // 2

    median = (numbers[middle - 1] + numbers[middle]) / 2

    print('\t', f'median = {median}')


def six(number):
    """
    Write a program that checks if a given number is a perfect number using a while loop.
    """
    print('\ndifficult.six:')

    total = 0
    divisor = 1

    while divisor < number:

        if number % divisor == 0:
            total += divisor

        divisor += 1

    print('\t', total == number)


def seven():
    """
    Write a program that prints the sum of all digits in a given number using a for loop.
    """
    print('\ndifficult.seven:')

    number = 12345

    total = 0

    for digit in str(number):
        total += int(digit)

    print('\t', total)


def eight(number):
    """
    Write a program that finds the longest word in a given sentence using a while loop.
    """
    print('\ndifficult.eight:')

    sentence = "Python is a powerful programming language"

    words = sentence.split()

    longest = words[0]

    i = 0

    while i < len(words):

        if len(words[i]) > len(longest):
            longest = words[i]

        i += 1

    print('\t', longest)


def nine():
    """
    Write a program that checks if a given string is a pangram using a for loop.
    """
    print('\ndifficult.nine:')

    sentence = "The quick brown fox jumps over the lazy dog"

    sentence = sentence.lower()

    is_pangram = True

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in sentence:
            is_pangram = False

    print('\t', is_pangram)


def ten():
    """
    Write a program that prints the prime numbers between 1 and 1000 using a while loop.
    """
    print('\ndifficult.ten:')

    number = 2

    while number <= 1000:

        divisor = 2
        is_prime = True

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break

            divisor += 1

        if is_prime:
            print('\t', number)

        number += 1
