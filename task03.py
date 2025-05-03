import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to the international format used for SMS delivery.

    - Keeps only digits and an optional '+' at the beginning.
    - Adds the Ukrainian international code '+38' if it's missing.
    - Handles various formats including:
        - Numbers starting with '+380' (already correct format).
        - Numbers starting with '380' (missing '+').
        - Numbers starting with '0' (local Ukrainian format, add '+38').
        - Other cases assumed to be local and treated accordingly.

    Args:
        phone_number (str): Raw phone number in any format.

    Returns:
        str: Normalized phone number in international format, e.g., '+380501234567'.
    """

    # Remove all characters except digits and '+'
    cleaned = re.sub(r'[^\d+]', '', phone_number)

    # If the number already starts with '+380', return as is
    if cleaned.startswith('+380'):
        return cleaned
    # If the number starts with '380' but missing '+', add it
    elif cleaned.startswith('380'):
        return '+' + cleaned
    # If the number starts with '0', assume local format and add '+38'
    elif cleaned.startswith('0'):
        return '+38' + cleaned
    # If the number starts with any other '+', return as is (non-UA international)
    elif cleaned.startswith('+'):
        return cleaned
    # Default case: treat as local number and prepend '+38'
    else:
        return '+38' + cleaned

# Example usage
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(f"Normalized phone numbers for SMS-sending: {sanitized_numbers}")
