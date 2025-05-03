from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Returns the number of days between the current date and the given date ('YYYY-MM-DD').
    Positive if the date is in the past, negative if in the future.
    """
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date() # Convert the string date to a datetime object
        today = datetime.today().date() # Get today's date
        delta = today - input_date # Calculate the difference in days
        return delta.days # Return the difference in days
    
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None


# Example usage
print(get_days_from_today("2025-05-01"))  # 2
print(get_days_from_today("2025-05-10"))  #-7
print(get_days_from_today("invalid-date"))  #Invalid date format. Please use YYYY-MM-DD.
print(get_days_from_today("2021-10-09")) #1302