from typing import List, Tuple


def calculate_lcm(numbers: List[int]) -> int:
    """Calculates the least common multiple of a list of integers."""
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = (lcm * numbers[i]) // gcd(lcm, numbers[i])

    return lcm


def validate_numbers(numbers: List[int]) -> Tuple[bool, str]:
    """validation of numbers greater than 0"""
    if len(numbers) == 0:
        return False, "Debe proporcionar al menos un número"
    for num in numbers:
        if num <= 0:
            return False, f"El número {num} no es válido, debe ser un entero positivo"
    return True, ""
