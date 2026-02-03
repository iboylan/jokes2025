


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

yes = ["Yes", "yes", "y", "Y", "YES"]
no = ["No", "no", "n", "N", "NO"]

def jokes(joke):
    namelist = ["robbers", "tanks", "pencils"]
    joke = joke.lower()
    found = False

    for name in namelist:
        if name == joke:
            found = True
            if name == "robbers":
                input("Knock knock! ")
                input("Calder ")
                input("Calder police - I've been robbed! ")
            elif name == "tanks":
                input("Knock knock! ")
                input("Tanks ")
                input("You're welcome! ")
            elif name == "pencils":
                input("Knock knock! ")
                input("Broken pencil ")
                input("Nevermind, it's pointless! ")
            break

    if not found:
        print("Not an option.")
        
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