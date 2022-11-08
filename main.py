from players import dominos
from gameboard import gameboard
import json

if __name__ == "__main__":

    print("SETTING UP THE GAME")
    while True:
        try:
            num_players = int(input("How many players to play the game? "))
            if num_players == 2:
                break
            print("Only 2 players please")
        except Exception as e:
            print(e)
    while True:
        try:
            player_a_name = input("Player 1 please enter your name: ")
            if player_a_name.isalpha():
                break
            print("Please only put alpha characters")
        except Exception as e:
            print(e)
    while True:
        try:
            player_b_name = input("Player 2 please enter your name: ")
            if player_b_name.isalpha():
                break
            print("Please only put alpha characters")
        except Exception as e:
            print(e)
    while True:
        try:
            total_games = int(
                input(
                    "How many games do you want to play? (Choose an odd number): "
                ))
            if total_games % 2 == 1:
                break
            print("Number of games to be played must be odd")
        except Exception as e:
            print(e)
    print("\n ---Statistics Menu---")
    while True:
        try:
            store_wins = str(
                input("Would you like to store the number of wins? (Yes/no): ")
            ).lower()
            if store_wins == "yes" or store_wins == "no":
                break
            print("Please answer yes or no")
        except Exception as e:
            print(e)
    while True:
        try:
            store_losses = str(
                input(
                    "Would you like to store the number of losses? (Yes/no): ")
            ).lower()
            if store_losses == "yes" or store_losses == "no":
                break
            print("Please answer yes or no")
        except Exception as e:
            print(e)

    gameboard = gameboard()
    for game_number in range(0, total_games):

        print(f"------Gameboard Menu------")
        print(f"Game number {game_number + 1}")

        print(f"{player_a_name}, draw your dominos")
        player_a = dominos()
        while player_a.length() < 7:
            player_a.pick_domino()
        print(f"{player_a_name} dominos: {player_a}")

        print(f"{player_b_name}, draw your dominos")
        player_b = dominos()
        while player_b.length() < 7:
            player_b.pick_domino()
        print(f"{player_b_name} dominos: {player_b}")

        if player_b.doubles() == 12 or player_b.doubles() > player_a.doubles():
            first_player = "b"
            print(f"\n{player_b_name} shall be going first.")
        else:
            first_player = "a"
            print(f"\n{player_a_name} shall be going first.")

        if first_player == "a":
            chosen = int(
                input(
                    f"{player_a_name} please choose a domino to place: ")) - 1
            gameboard.add(player_a.remove(chosen))
            print(gameboard)
            while gameboard.length() < 13 or player_a.score(
            ) == player_b.score():
                #Player B turn
                if len(
                        player_b.lastnum(
                            gameboard.last_number(gameboard.length() -
                                                  1))) == 0:
                    player_b.pick_domino()
                    if len(
                            player_b.lastnum(
                                gameboard.last_number(gameboard.length() -
                                                      1))) == 1:
                        gameboard.add(player_b.remove(player_b.length() - 1))
                        print(gameboard)
                    print(f"{player_b_name} drew a domino")
                else:
                    last = gameboard.last_number(gameboard.length() - 1)
                    valid = player_b.lastnum(last)
                    chosen = int(
                        input(f"{player_b_name} choose dominos: {valid} ")) - 1
                    number_picked = valid[chosen]
                    index = player_b.index(number_picked)
                    gameboard.add(player_b.remove(index))
                    print(gameboard)

                #Player A turn
                if len(
                        player_a.lastnum(
                            gameboard.last_number(gameboard.length() -
                                                  1))) == 0:
                    player_a.pick_domino()
                    if len(
                            player_a.lastnum(
                                gameboard.last_number(gameboard.length() -
                                                      1))) == 1:
                        gameboard.add(player_a.remove(player_a.length() - 1))
                        print(gameboard)
                    print(f"{player_a_name} drew a domino")
                else:
                    last = gameboard.last_number(gameboard.length() - 1)
                    valid = player_a.lastnum(last)
                    chosen = int(
                        input(f"{player_a_name} choose dominos: {valid} ")) - 1
                    number_picked = valid[chosen]
                    index = player_a.index(number_picked)
                    gameboard.add(player_a.remove(index))
                    print(gameboard)
        elif first_player == "b":
            chosen = int(
                input(
                    f"{player_b_name} please choose a domino to place: ")) - 1
            gameboard.add(player_b.remove(chosen))
            print(gameboard)
            while gameboard.length() < 13 or player_a.score(
            ) == player_b.score():

                #Player A turn
                if len(
                        player_a.lastnum(
                            gameboard.last_number(gameboard.length() -
                                                  1))) == 0:
                    player_a.pick_domino()
                    if len(
                            player_a.lastnum(
                                gameboard.last_number(gameboard.length() -
                                                      1))) == 1:
                        gameboard.add(player_a.remove(player_a.length() - 1))
                        print(gameboard)
                    print(f"{player_a_name} drew a domino")
                else:
                    last = gameboard.last_number(gameboard.length() - 1)
                    valid = player_a.lastnum(last)
                    chosen = int(
                        input(f"{player_a_name} choose dominos: {valid} ")) - 1
                    number_picked = valid[chosen]
                    index = player_a.index(number_picked)
                    gameboard.add(player_a.remove(index))
                    print(gameboard)

                #Player B turn
                if len(
                        player_b.lastnum(
                            gameboard.last_number(gameboard.length() -
                                                  1))) == 0:
                    player_b.pick_domino()
                    if len(
                            player_b.lastnum(
                                gameboard.last_number(gameboard.length() -
                                                      1))) == 1:
                        gameboard.add(player_b.remove(player_b.length() - 1))
                        print(gameboard)
                    print(f"{player_b_name} drew a domino")
                else:
                    last = gameboard.last_number(gameboard.length() - 1)
                    valid = player_b.lastnum(last)
                    chosen = int(
                        input(f"{player_b_name} choose dominos: {valid} ")) - 1
                    number_picked = valid[chosen]
                    index = player_b.index(number_picked)
                    gameboard.add(player_b.remove(index))
                    print(gameboard)

        #To check the winner, the game checks for the player with the largest remaining sum of domino numbers. Stores wins and losses depending on if the user picked it from the statistics menu

        with open("statistics.json", "r") as f:
            statistics = json.load(f)
        if player_a.score() > player_b.score():
            print(f"{player_a_name} won")
            if store_wins == "yes":
                statistics["Player A"]["Wins"] += 1
            if store_losses == "yes":
                statistics["Player B"]["Losses"] += 1
            with open("statistics.json", "w") as f:
                json.dump(statistics, f)
        else:
            print("Player B won")
            if store_wins == "yes":
                statistics["Player B"]["Wins"] += 1
            if store_losses == "yes":
                statistics["Player A"]["Losses"] += 1
            with open("statistics.json", "w") as f:
                json.dump(statistics, f)

        player_a.refresh()
        player_b.refresh()
        gameboard.refresh()

    while True:
        try:
            show_statistics = str(
                input(
                    "\n Would you like to see the statistics of the game? (Yes/no): "
                )).lower()
            if show_statistics == "yes":
                with open("statistics.json", "r") as f:
                    statistics = json.load(f)
                B_wins = statistics["Player B"]["Wins"]
                A_wins = statistics["Player A"]["Wins"]
                A_losses = statistics["Player A"]["Losses"]
                B_losses = statistics["Player B"]["Losses"]
                print(
                    f"Player A has won {A_wins} of the games while losing {A_losses} of the games."
                )
                print(
                    f"Player B has won {B_wins} of the games while losing {B_losses} of the games."
                )
                break
            print("Please answer yes or no")
        except Exception as e:
            print(e)
