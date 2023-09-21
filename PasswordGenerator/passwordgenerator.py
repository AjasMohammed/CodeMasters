import string
import random
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digits = string.digits
special_characters = "!@#$%^&*_-+=<>?"


def generate_password(strength, complexity):
    characters = shuffle_characters(complexity)

    password = ''
    for i in range(strength):
        password += random.choice(characters)
    return password


def shuffle_characters(complexity):
    char = list(upper_case + lower_case + digits + special_characters)
    for i in range(complexity):
        random.shuffle(char)
    return char


strength = int(input('Password Length: '))
complexity = int(input('Enter Complexity: '))
password = generate_password(strength, complexity)

print(f'\nGenerated Password: {password}\n')