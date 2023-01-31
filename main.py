answer = input("Would you like to play? (yes/no)").lower().strip()

if answer == 'yes':
    answer = input('You reach a crossroads, would you like to go left or right? (left/right)').lower().strip()
    if answer == 'left':
        answer = input('You encounter a monster, would you like to run or attack? (run/attack)').lower().strip()
        if answer == 'attack':
            print('You were fighting bare-handed. You were dead.')
        else:
            print('Good choice, you made it away safely.')
    elif answer == 'right':
        print('You walked aimlessly to the right and fell on a patch of ice. You injured your leg and cannot continue. Game over!')
    else:
        print('Invalid choice, you lost!')
else:
    print("That's too bad!")