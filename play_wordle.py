from wordle import Wordle

def main():
    print('Welcome to Wordle...')
    wordle = Wordle('AUDIO')
    while True:
        guess = input('Take a guess: ')
        if guess == wordle.secret:
            print('Good Job')
            break
        print('Sorry you are incorrect.')

if __name__ == '__main__':
    main()