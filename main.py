import random



choices = ('rock', 'paper', 'scissors')
exit_call = False


def get_winner(player_choice: int, machine_choice: int):
    if player_choice == machine_choice:
        return None
    elif player_choice == 0:
        return 'Machine' if machine_choice == 1 else 'Player'
    elif player_choice == 1:
        return 'Machine' if machine_choice == 2 else 'Player'
    else:
        return 'Machine' if machine_choice == 0 else 'Player'

while True:
    player_choice = None

    print('\nRock, Paper or Scissors?')
    try:
        player_choice = input('!>> ').lower()
        if exit_call:
            exit_call = False
    except KeyboardInterrupt:
        # Throws the player out of the game if the exit command was called
        # last time.
        if exit_call:
            from sys import exit
            exit(0)
        else:
            print('Use Ctrl^C once again to leave the game. You can also use Ctrl^Z to force the program to quit.')
            exit_call = True
            continue
    
    matching_player_choices = filter(lambda c: player_choice in c, choices)
    matching_player_choices = list(matching_player_choices)

    if not len(matching_player_choices):
        print('Invalid argument')
        continue
    elif len(matching_player_choices) > 1:
        print(f'Multiple matches for [{player_choice}] -> [{", ".join(matching_player_choices)}]. Using first result...')
    
    player_choice = choices.index(matching_player_choices[0])

    machine_choice = random.randint(0, 2)
    
    match_winner = get_winner(player_choice, machine_choice)

    if not match_winner:
        print('No one has won this battle! It was a match!')
        print(f'{choices[player_choice]} vs {choices[machine_choice]};')
        continue
    
    print(f'{match_winner} has own this match!')
    print(f'{choices[player_choice]} vs {choices[machine_choice]};')

