"""
Python module to know if a string is a palindrome
"""


def is_palindrome(string: str) -> bool:
    """Returns if the string is palindrome"""
    string = string.lower()
    string = string.replace(' ', '') 
    return (string == string[::-1])


def run():
    word = input('Write a word: ')
    palindrome = is_palindrome(word)
    if palindrome:
        print(f'The word {word} is a palindrome')
    else:
        print(f'The word {word} is not a palindrome')


if __name__ == '__main__':
    run()