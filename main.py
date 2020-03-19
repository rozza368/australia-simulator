# ensure user enters only a certain set of answers
def check_input(*args):
    bad = True  # assume the input is unacceptable
    while bad:  # if the input is not acceptable
        inp = input()
        for arg in args:
            if inp == str(arg): # if the input matches one of the arguments then the input is good, program continues
                bad = False
                break
        if bad:
            print("Invalid answer, try again.")
    return inp
# eg check_input(1, 2) will ensure the user can only answer with 1 or 2


def main():
    # set variables to check later whether user has won or lost
    lost = False
    won = False
    while not lost and not won:
        print("\n\nWelcome to Australia Simulator.\nEnter the number between the brackets to answer the questions.\n")
        print("You wake up and realise there is no milk for your cereal. Where do you go to buy some? IGA [1] or Woolworths [2]")
        answer1 = check_input(1, 2)  # check to see if the user inputs 1 or 2

        print("You walk down the street to the shop. Suddenly, you hear squawking behind you. You turn around and notice a magpie flying towards you, ready to swoop. Do you stop and crouch [1] or start running [2]?")
        answer2 = check_input(1, 2)
        if answer2 == "1":
            print("You crouch and cover your head. You hear the squawking get louder and feel a powerful peck on your ear. You get scared and run back home. You don’t want to leave the house in fear of the magpie attacking again. The end. (LOSS)")
            lost = True
            break  # exit the game loop
        elif answer2 == "2":
            print("You run the rest of the way to the shop and the magpie loses interest. You’re safe! You enter the shop and make your way to the milk section.")

        if answer1 == "1":
            print("In IGA, you grab the milk you usually get and buy it. Back at home, you fill your bowl with cereal and then milk and eat it.")
        elif answer1 == "2":
            print("Unfortunately Woolworths ran out of milk by the time you got there. ¯\\_(ツ)_/¯ You go back home and feel sad that you can’t have any milk. The end. (LOSS)")
            lost = True
            break


        print("By the time you get home you’re flushed and sweaty. Will you go to the beach [1] or stay at home [2]?")
        answer3 = check_input(1, 2)

        if answer3 == "1":
            print("You suggest to your mates to go to the beach with you. They agree, so you need to get ready quickly. Do you take either your cap [1] or your sunnies [2]?")
            answer3_1 = check_input(1, 2)

            print("You go to the beach and meet your friends. You all decide to have a snack first, do you choose ice-cream [1] or hot chips [2]?")
            answer3_11 = check_input(1, 2)
            if answer3_11 == "1":
                print("You go and buy ice-cream for everyone. You bring it back and you and your friends enjoy the day at the beach.")
                print("You arrive home in the evening by yourself feeling happy about your day. You go to wash your face and look at yourself in the mirror.")
                if answer3_1 == "1":
                    print("Since you wore a cap to the beach, your face did not get sunburnt! You can spend the rest of your day comfortably. The end (WIN).")
                    won = True
                    break
                elif answer3_1 == "2":
                    print("Since you only wore sunglasses to the beach, your face got fairly burnt. You realise that was the reason your face feels sore. You wash your face and apply moisturiser, but you know the pain will last for a while. The end (LOSS).")
                    lost = True
                    break
                    
                
            elif answer3_11 == "2":
                print("You go and buy a box of hot chips. As you bring it back to your friends, you become bombarded with hungry seagulls who knock the chips out of your hands. Your friends become annoyed towards you and tell you to go back home. The end. (LOSS)")
                lost = True
                break
            

        elif answer3 == "2":
            print("You decide to stay home. It’s getting hot inside, though, so do you turn on the air conditioning [1], turn on the ceiling fan [2] or do nothing [3]")
            selected = False
            while not selected:
                answer3_2 = check_input(1, 2, 3)
                if answer3_2 == "1":
                    print("You find that the air conditioning has broken down. Try something else maybe?")
                elif answer3_2 == "2":
                    print("You switch on the ceiling fan. It’s starting to feel more bearable inside.")
                    print("You relax at home comfortably for the rest of the day. The end (WIN).")
                    won = True
                    selected = True
                elif answer3_2 == "3":
                    print("If you don’t do anything you’ll probably get heatstroke!")
            break

    # Prints an ending message
    if won:
        print("Congratulations, you won! Play again? [y/n]")
    else:
        print("You lost...\nTry again? [y/n]")

    # Lets the user play again if they wish
    if input().startswith("y"):
        main()
    else:
        return True # tell the program that the user wants to exit


if main(): # call function to start program
    # true when user wants to quit, quits program too
    exit()
