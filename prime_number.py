"""
Python module to know if a number is prime
"""


def is_prime(number: int) -> bool:
    """Returns if the number is prime"""
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def run():
    try:
        number: int = int(input('Write a number: '))
        if number < 0:
            raise ValueError()
        
        prime = is_prime(number)
        if prime:
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')

    except ValueError:
        print('Please enter only positive integers')


if __name__ == '__main__':
    run()