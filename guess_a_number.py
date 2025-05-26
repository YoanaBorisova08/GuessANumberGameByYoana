import random

computer_number = random.randint(1, 100)
range_number = 100
round = 1
tries = 10

while True:
    player_input = input(f"Round {round}! {\n}You have {tries} tries! {\n}Guess the number (1-{range_number}): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("You guessed right!")
        play_again = input("Type [yes] if you want to go to the NEXT ROUND. Else type [no].")
        if play_again == "yes":
            round+=1
            tries -=1
            range_number+=100
            continue
        break
    elif player_number < computer_number:
        print("Too Low!")
        tries-=1
    else:
        print("Too High!")
        tries-=1

    if tries==1:
        print("One last try. Be careful!")
    elif tries==0:
        print("You lost! {\n} Type [yes] if you want to PLAY AGAIN. Else type [no].")
        if play_again == "yes":
            round = 1
            tries = 10
            range_number = 100
        else:
            break