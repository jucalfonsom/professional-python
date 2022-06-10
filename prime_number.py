"""
Python module to know if a number is prime
"""


def is_prime(number: int) -> bool:
    """Returns if the number is prime"""
    if number == 0:
        return False
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
        if counter > 2:
            break
    
    if counter > 2:
        return False
    else:
        return True


def run():
    try:
        number: int = int(input('Write a number to check if is a prime number: '))
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