# Define a function
def kwargs_length(**kwargs):
    return len(kwargs)


# Test Code
dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))
