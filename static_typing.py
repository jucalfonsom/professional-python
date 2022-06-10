"""
This program was used to learn static typing in Python
"""

from typing import Dict, List, Tuple


# Variables
a: int = 5
print(a)

b: str = "Hola"
print(b)

c: bool = True
print(c)


# Functions
def suma(a: int, b: int) -> int:
	return a + b

print(suma(1,2))


# Lists, dicts, and tuples

# Lists
positives: List [int] = [1,2,3,4,5]

# Dictionaries
users: Dict [str, int] = {
	"argentina": 1,
	"mexico": 34,
	"colombia": 45,
}
print(users)


# List of dictionaries
countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]
print(countries)

# Tuples
tupleExample: Tuple[int, str, int, int, str] = (2, 'Hola', 4, 6, 'Adiós')
print(tupleExample)


# List of dictionary of string: tuple
coordinatesType = List[Dict[str, Tuple[int, int]]] # Alias

coordinates: coordinatesType= [
    {
        'coord1': (1, 2),
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1),
        'coord2': (2, 5)
    }
]

print(coordinates)