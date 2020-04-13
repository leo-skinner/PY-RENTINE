import random

player_score = 0
cpu_score = 0
play_again = True

while (play_again == True):

    print('*'*22)
    print('Rock, paper, scissors')
    print('*'*22)

    print('')
    print('Make your choice')
    print('-'*22)
    print('')
    print('[1] Rock')
    print('[2] Paper')
    print('[3] Scissors')

    choice = int(input('Select Number and press enter.'))
    cpu_choice = random.randint(1, 3)

    if(choice == 1 and cpu_choice == 2):
        print('Your choice was Rock and CPU was Paper.')
        print('CPU Wins!')
        cpu_score += 1

    elif (choice == 1 and cpu_choice == 3):
        print('Your choice was Rock and CPU was Scissors.')
        print('You Win!')
        player_score += 1

    elif (choice == 2 and cpu_choice == 1):
        print('Your choice was Paper and CPU was Rock.')
        print('You Win!')
        player_score += 1

    elif (choice == 2 and cpu_choice == 3):
        print('Your choice was Paper and CPU was Scissors.')
        print('CPU Wins!')
        cpu_score += 1

    elif (choice == 3 and cpu_choice == 1):
        print('Your choice was Scissors and CPU was Rock.')
        print('CPU Wins!')
        cpu_score += 1

    elif (choice == 3 and cpu_choice == 2):
        print('Your choice was Scissors and CPU was Paper.')
        print('You Win!')
        player_score += 1

    elif (choice == 1 and cpu_choice == 1 or choice == 2 and cpu_choice == 2 or choice == 3 and cpu_choice == 3):
        print('Your choice was same as CPU.')
        print('Draw!')

    print('Your score is: {} '.format(player_score))
    print('CPU score is: {} '.format(cpu_score))

    new_game = input('Play Again ? ')
    if (new_game == 'Y'):
        play_again = True
    else:
        play_again = False
        break
