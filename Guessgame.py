import random as r
secret_number = r.randint(1, 20)
# print(f"Secret Number: {secret_number}")
guess_limit = 3
guess_number = 0
guess_count = 1
while guess_number != secret_number:
    guess_number = int(input(f"Guess Number ({guess_count})? "))
    if guess_number == secret_number:
        print('Urime, keni fituar!')
        print(f"Secret Number: {secret_number}")
        break

    if guess_number > secret_number:
        print('Your guess is higher!')
    else:
        print('Your guess is lower!')

    if guess_count >= guess_limit:
        print(f'Your limit is over {guess_count}!')
        break

    guess_count = guess_count + 1
