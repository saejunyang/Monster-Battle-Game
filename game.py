game_running = True 

while game_running == True:
    new_round = True
    player = {"name" : "input", "attack": 13, "heal": 16, "health": 100} 
    monster ={"name" : "Monster", "attack" : 14, "health" : 100}

    print("-" * 18)
    print("Enter Player Name: ")
    player["name"] = input()

    print("-" * 18)
    print("Welcome to the battle " + player["name"] + ", destroy the monster!")
    print(player["name"] + " has " + str(player["health"]) + " health")
    print(monster["name"] + " has " + str(monster["health"]) + " health")

    while new_round == True:

        player_won = False
        monster_won = False

        print("-" * 18)
        print("Please select action")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit Game")

        player_choice = input()

        if player_choice == "1":
            monster["health"] = monster["health"] - player["attack"]
            if monster["health"] <= 0:
                player_won = True

            else:
                player["health"] = player["health"] - monster["attack"]
                if player["health"] <= 0:
                    monster_won = True

            print(monster["health"])
            print(player["health"])

        elif player_choice == "2":
            player["health"] = player["health"] + player["heal"]

            player["health"] = player["health"] - monster["attack"]
            if player["health"] <= 0:
                    monster_won = True
 
        elif player_choice == "3":
            new_round = False
            game_running = False

        else: 
            print("invalid input")

        if player_won == False and monster_won == False:
            print(player["name"] + " has " + str(player["health"]) + " health remaining")
            print(monster["name"] + " has " + str(monster["health"]) + " health remaining")

        elif player_won:
            print("You have defeated the monster")
            new_round = False

        elif monster_won:
            print("You have been defeated")
            new_round = False
            