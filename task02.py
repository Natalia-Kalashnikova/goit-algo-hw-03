import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:
    """
    Returns a sorted list of unique random numbers within the given range.

    Parameters:
    - min_value (int): Minimum number in the range (at least 1).
    - max_value (int): Maximum number in the range (no more than 1000).
    - quantity (int): Number of unique random numbers to generate (must be between min and max).

    Returns:
    - list: Sorted list of unique random numbers, or empty list if parameters are invalid.
    """
    if (
        not (1 <= min_value <= 1000)
        or not (1 <= max_value <= 1000)
        or min_value > max_value
        or quantity > (max_value - min_value + 1)
    ):
        return []
    
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)

# Example usage
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)#[1, 18, 26, 35, 40, 43]