file = 'questions.txt'

score = 0
def check_answer(user_inp, options, answer):
    if len(user_inp) > 1:
        if ans.lower() == answer:
            return True
        else:
            return False
    else:
        for option in options:
            if user_inp + ')' in option and answer in option.lower():
                return True
        return False


with open(file) as f:
    content = f.readlines()
    options = []
    for i in content:
        if ")" in i:
            options.append(i.strip())
        if 'Answer' in i:
            ans = input("Answer: ")
            answer = i.replace('Answer:', '').lower().strip()

            check = check_answer(ans, options, answer)
            if check:
                score += 1
                print(f'Your Answer is Correct, Score: {score}')
                options = []
            else:
                print('Wrong!')
                print(f'The Correct Answer is, {answer}')
                options = []
        else:
            print(i.strip())


print(f"\n\tYour Total Score = {score}")