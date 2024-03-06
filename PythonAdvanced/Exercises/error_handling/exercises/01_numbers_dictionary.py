numbers_dictionary = {}
VALID_KEY_VALUE_PAIRS = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
    }


class KeyDoesNotMatchValue(Exception):
    """
    The exception is raised when the key does not match the value in kvp.
    This should not happen because the logic of the program is just like so.
    """
    pass


def check_key_value_matching(key: str, curr_value: int) -> None:
    """
    The main logic about adding kvp(key-value pairs) is that they should match.
    Let me show you and example of how exactly:
    {'one': 1, 'two': 2, 'three': 3} and so on...

    This functions will check whether the key matches the value and if
    it doesn't an exception is going to be thrown - (KeyDoesNotMatchValue).
    """
    try:  # try to access the expected value
        expected_value = VALID_KEY_VALUE_PAIRS[key]
    except KeyError:  # if the key is not in the dictionary.keys() throw an exception
        print('Invalid key!')
    else:
        if expected_value == curr_value:  # if the expected value matches the actual one
            print(f'Valid key-value pair added! №-{len(numbers_dictionary) + 1}')


# Read User input
line = input()  # Adding numbers to the dictionary
while line != "Search":
    number_as_string = line  # 'one'

    try:  # Check if a valid number is given and if the number_as_str matches the number_as_int at the same time
        number = int(input())
        check_key_value_matching(number_as_string, number)  # calling a function
    except ValueError:  # Exception
        print('The variable number must be an integer!')
    else:  # if valid add - {key: value} to the dict
        numbers_dictionary[number_as_string] = number

    line = input()

# Read User input
line = input()
while line != "Remove":  # Print pairs from the dictionary
    searched = line

    try:  # Take the key and access its value in order to print it to the User
        print(f"Key {numbers_dictionary[searched]} founded!")
    except KeyError:  # if the dict does not contain the key - throw an exception
        print('Number does not exist in the dictionary!')

    line = input()

# Read User input
line = input()
while line != "End":  # Remove pairs from the dictionary
    searched = line
    try:  # try to delete a pair from the dictionary
        del numbers_dictionary[searched]
    except KeyError:  # if the dict does not contain the key - throw an exception
        print('Number does not exist in the dictionary!')

    line = input()

# Print User output
print(numbers_dictionary)
