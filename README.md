# Task 01
### Create a function get_days_from_today(date) that calculates the number of days between a given date and the current date.

# Task 02
### To win the main prize of the lottery, it is necessary to match several numbers on the lottery ticket with numbers that fell out randomly and in a certain range during the next draw. For example, you need to guess six numbers from 1 to 49 or five numbers from 1 to 36, etc.

### You need to write a function get_numbers_ticket(min, max, quantity), which will help generate a set of unique random numbers for such lotteries.

### It will return a random set of numbers within the specified parameters, and all random numbers in the set must be unique.

# Task 03
### Your company is running an active marketing campaign using SMS mailings. To do this, you collect customer phone numbers from a database, but you often encounter numbers written in different formats.

### Your mailing service can only send messages effectively when phone numbers are presented in the correct format. Therefore, you need a function that automatically normalizes phone numbers to the desired format, removing all unnecessary characters and adding the international country code, if necessary.

### Develop a function normalize_phone(phone_number), which normalizes phone numbers to the standard format, leaving only digits and the '+' symbol at the beginning. The function accepts one argument - a string with a phone number in any format and converts it to the standard format, leaving only digits and the '+' symbol. If the number does not contain an international code, the function automatically adds the code '+38' (for Ukraine). This ensures that all numbers are suitable for sending SMS.
