import random

print ("The player wakes up in a mysterious forest and must navigate through different choices. The goal is to find a way out, encountering obstacles, items, and challenges along the way.")

items = ['key', 'torch', 'weapons', 'food']

player_choice = int(input("You wake up in a dark forest. You see three paths ahead: 1) Left, 2) Right, and 3) Forward. Which number will you choose? "))

inventory = []

monster = True

if player_choice < 1 or player_choice > 3:
    player_choice = int(input('Error, that choice doesnt exist, please pick again: '))

while player_choice == 1 or player_choice == 2 or player_choice == 3:

    if player_choice == 1:
        player_choice = int(input('You find an old rusted key on the ground. Do you take it? (1 for yes / 2 for no) '))
        if player_choice == 2:
            print('You left the item behind ')
            print('The path then leads to an abandoned house with a locked door, since you dont have the key you may not enter. ')
            player_choice = int(input('Do you wish to go back and retrieve the key? (1 for yes / 2 for no) '))
            if player_choice == 1:
                inventory.append("Key")
                print ('The key is added to your inventory')
            else:
                print('You hear something behind you. A wild monster appears. You are dead!')
                print ('Game Over')
                break

        else:
            print('The key is added to your inventory')
            inventory.append('Key')
            print('The path then leads to an abandoned house with a locked door. You enter the house.')
            surprise = random.randint(1,3)
            if surprise == 1:
                print('You found a medkit and added it to your inventory')
                inventory.append('Medkit')
                player_choice = int(input('Do you wish to go back and choose another path, or end the game here? (1 for Go Back / 2 for End Game) '))
                if player_choice == 1:
                    player_choice = int(input('You have returned to the beginning, which path would you like to go to? 1) Left, 2) Right, or 3) Forward? '))

                else:
                    print('Game Over')
                    break

            elif surprise == 2:
                print('You found a loaded pistol and added it to your inventory')
                inventory.append('Pistol')
                player_choice = int(input('Do you wish to go back and choose another path? (1 for yes / 2 for no) '))
                if player_choice == 1:
                    player_choice = int(input(
                        'You have returned to the beginning, which path would you like to go to? 1) Left, 2) Right, or 3) Forward? '))

                else:
                    print('Game Over')
                    break

            else:
                print('You have been attacked by a monster.')
                if 'Pistol' in inventory:
                    print('You pull out the pistol in time, and kill the monster. You are safe, for now.')
                    player_choice = int(
                        input('Do you wish to go back and choose another path? (1 for yes / 2 for no) '))
                    if player_choice == 1:
                        player_choice = int(input(
                            'You have returned to the beginning, which path would you like to go to? 1) Left, 2) Right, or 3) Forward? '))

                elif 'Pistol' not in inventory:
                        print('Game Over')
                        break

    if player_choice == 2:
        while monster:
            print('You hear rustling in the bushes. A wild creature appears!')
            player_choice = int(input(('You can either choose to 1) Run, 2) Fight, or 3) Hide: ')))
            if player_choice == 1:
                random_chance = random.randint(1, 2)
                if random_chance == 1:
                    print('You manage to escape, barely.')
                    player_choice = int(input('Do you wish to go back and choose another path? (1 for yes / 2 for no) '))
                    if player_choice == 1:
                        player_choice = int(input(
                            'You have returned to the beginning, which path would you like to go to? 1) Left, 2) Right, or 3) Forward? '))
                        break

                    else:
                        print('Game Over')
                        break

                else:
                    print('The beast catches up to you. You are dead')
                    print('Game Over')
                    break

            if player_choice == 2 and 'Pistol' in inventory:
                print('You manage to kill the monster. You are safe, for now. ')
                monster = False
                player_choice = int(input('Do you wish to go back and choose another path? (1 for yes / 2 for no) '))
                if player_choice == 1:
                    player_choice = int(input(
                        'You have returned to the beginning, which path would you like to go to? 1) Left, 2) Right, or 3) Forward? '))
                    break

                else:
                    print('Game Over')
                    break
            elif player_choice == 2 and 'Pistol' not in inventory:
                luck = random.randint(1, 2)
                if luck == 1:
                    print ('You somehow managed to kill the monster, because you were extremly lucky. Be careful you wont always be. ')
                    monster = False
                    player_choice = int(
                        input('Do you wish to go back and choose another path? (1 for yes / 2 for no) '))
                    if player_choice == 1:
                        player_choice = int(input(
                            'You have returned to the beginning, which path would you like to go to? 1) Left, 2) Right, or 3) Forward? '))
                        break

                    else:
                        print('Game Over')
                        break

                else:
                    print('The fight was shortlived. You are dead.')
                    print('Game Over')
                    break

            if player_choice == 3:
                print('You find a bush to hide. Time is passing, but you know the monster is still looking for you.')
                monster_move = random.randint(1, 2)
                if monster_move == 1:
                    player_choice = int(input(
                        'The monster leaves you be, you are now safe. You can either choose to go back or end the game here. 1) Go back, 2) End the game '))
                    if player_choice == 1:
                        player_choice = int(input(
                            'You have returned to the beginning, which path would you like to go to? 1) Left, 2) Right, or 3) Forward? '))

                    else:
                        print('Game Over')
                        break

                else:
                    print('The monster found you. You are dead.')
                    print('Game Over')
                    break

        while not monster and player_choice == 2:
            print ('There is nothing you can do here anymore.')
            player_choice = int(
                input('Do you wish to go back and choose another path? (1 for yes / 2 for no) '))
            if player_choice == 1:
                player_choice = int(input(
                    'You have returned to the beginning, which path would you like to go to? 1) Left, 2) Right, or 3) Forward? '))

            else:
                print('Game Over')
                break


    if player_choice == 3:
        first_time = True
        while first_time:
            print('You notice a cave from afar. You decide to enter.')
            print('A stone door is in front of you. The door has three buttons. You have to pick one')
            player_choice = int(input('1) Moon    2) Sun   3) Star '  ))
            if player_choice == 1:
                print('The cave collapses')
                print('Game Over')
                break
            elif player_choice == 2:
                print('You have fallen into a trap. Unfortunately there is no way out.')
                print('Game Over')
                break
            else:
                print('The door opens, and a beam of light shines through.')
                print('You have won the game!!!')
                break
        break


