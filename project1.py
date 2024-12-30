import random



def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Must be between 2 to 4 players.")
    else:
        print("Invalid, Try again.")


max_score = 50
player_score = [0 for _ in range(players)]


while max(player_score) < max_score:
    for player_idx in range(players):
        print("\n Player number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_score[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll(y)? ")
            if should_roll.lower() != "y":
                break
        
            value = roll()
            if value == 1:
                print("You rolled 1, turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
            print("Your score is:", current_score)
        player_score[player_idx] += current_score
        print("Your total score is: ", player_score[player_idx])

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("Player number ", winning_idx + 1, 
      "is winner with the score of", max_score)



