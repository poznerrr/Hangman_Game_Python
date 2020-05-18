import random
import string

def game():
    gameover = input('Type "play" to play the game, "exit" to quit:')
    if gameover == 'exit':
        return False
    elif gameover == 'play':
        pass
    else:
        return True 
    print()
    variants = ['python', 'java', 'kotlin', 'javascript']
    answer = random.choice(variants)
    hint ='-' * len(answer)
    shower=list(hint)
    my_set=set(answer)
    answer_set = set()
    trying = 8
    while trying > 0:
        print(hint)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should print a single letter")
            print()
            continue
        if guess not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            print()
            continue
        if guess in answer_set:
                print("You already typed this letter")
                print()
                continue
        if guess in my_set:
            for z in range(len(answer)):
                if guess == answer[z]:
                    shower[z] = guess
                    answer_set.add(guess)
                    hint=''.join(shower)
                    if hint == answer:
                        break
        
        if guess not in my_set:
            print("No such letter in the word")
            answer_set.add(guess)
            trying -= 1       
            if trying == 0:
                break
        print()
    if trying > 0:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")
    print()
    return True
        
    
print("H A N G M A N")
menu = True
while menu == True:
    menu = game()
