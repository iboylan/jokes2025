


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")

yes = ["Yes", "yes", "y", "Y", "YES"]
no = ["No", "no", "n", "N", "NO"]
def jokes(joke):
    namelist = ["robbers", "tanks", "pencils"]
    for name in namelist:
        if name == joke.lower():
            if name == "robbers":
                input("Knock knock! ")
                input("Calder ")
                input("Calder police - I've been robbed! ")
                return
            if name == "tanks":
                input("Knock knock! ")
                input("Tanks ")
                input("You are welcome! ")
                return
            if name == "pencils":
                input("Knock Knock! ")
                input("Broken pencil ")
                input("Nevermind, it's pointless! ")
                return
        elif name != joke.lower():
            print("not an option")
            return

def newjoke():
    newjokelist = []
    newjokelist.append(input("What's your joke about?: "))
    newjokelist.append(input("What's the punchline of your joke?: "))
    input("Knock knock! ")
    input(f"{newjokelist[0]}")
    input(f"{newjokelist[1]}")  


confirm = str(input("Do you want to hear a joke?: "))
if confirm in yes:
    print("Ok!")
    var = input("Do you want to hear a joke about robbers, tanks, or pencils?: ").lower()
    jokes(var)
    confirm2 = input("Do you want to hear another joke?: ")
    if confirm2 in yes:
        print("Ok!")
        var = input("Do you want to hear a joke about robbers, tanks, or pencils?: ").lower()
        jokes(var)
    elif confirm2 in no or confirm2 not in yes:
        confirm2 = input("Ok! Do you want to make your own joke?: ")
        if confirm2 in yes:
            print("Ok!")
            newjoke()
        elif confirm2 in no or confirm2 not in yes:
            print("Ok, suit yourself.")
elif confirm in no or confirm not in yes:
    print("Ok, suit yourself.")

    # do you want to hear amother
    # if yes run jokes function again
    # do you want to make a joke
    # newjoke function if yes