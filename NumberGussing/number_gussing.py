import random

attempt = 5
num = random.randint(1, 10)

def guess_number(n):
    global attempt

    if n == num:
        print("Great Your Answer is Correct.")
        return True
    elif n < num:
        print(f'{n} is Low!')
        attempt -= 1
    elif n > num:
        print(f"{n} is High!")
        attempt -= 1

print('Guess a Number Between 1 & 10')

while attempt != 0:
    print(f'Attempts Left: {attempt}')
    user_inp = int(input('>>> '))
    guess = guess_number(user_inp)
    if guess == True:
        break