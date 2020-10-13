#
# Python    3.8.5
#
# Purpose   Learn to code with functions and parameters
#


def start(nice =0, mean=0, name=""): # set default values that will be overwritten, if user does not provide values
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)
    print(name)


def describe_game(name):
    """
        Check if thisis a new game or not.
        If it is new, get the user name.
        If it is not a new game, thank the player for
        playing agan and continue with the game.
    """
    # meaning if we do not already have this user's name,
    # then he is a new player and we need to get his name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nwhat is your name?\n>>>").capitalize()
                if name != "":
                    print("Welcome, {}".format(name))
                    print("\nIn this game you will be greeted \nby several different people. \nYou can choose to be nice or mean \nbut at the end of the game your fate \nwill be sealed by your actions")
                    stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? N/M\n>>>").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice += 1
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms of...")
            mean += 1
            stop = False
    score(nice, mean, name)


def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)


def win(nice, mean, name):
    print("\nNice Job {}, you win.\nEveryone loves you".format(name))
    again(nice, mean, name)


def lose(nice, mean, name):
    print("\nToo bad, {}. You lose".format(name))
    again(nice, mean, name)


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("So sad to see you go.")
            stop = False
            quit()
        else:
            print("\n Enter Y for 'Yes' and N for 'No'\n>>>")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)



if __name__ == "__main__":
    start()
