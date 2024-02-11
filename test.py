import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

# value = roll()
# print(value)

while True:
    players = input("Enter the number of players (2-4) : ")
    if players.isdigit():
        players  = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 - 4.")
    else:
        print("Please enter a valid number.")

print(players)

max_score = 50
player_scores = []
for i in range(players):
    player_scores.append(0)

while max(player_scores) < max_score:

    for player_index in range(players): # covering for each player using for loop
        print("\n Player number",player_index + 1," HAS JUST STARTED \n")
        current_score = 0

        while True:                     #repeating the actions for each player.
            answer = input("do you want to roll the die (y) ? :  ")
            if answer.lower() != "y":
                break
            value = roll()
            
            if value == 1:
                current_score = 0
                print("You rolled 1, You lost your chance to roll again. ")
                break
            else:
                current_score += value
                print("you rolled ",value)

        player_scores[player_index] += current_score                 #adding the current score to the players score list.
        print("Your total score is : ", player_scores[player_index]) #printing players score at the index, giving total score.

