print("\nWelcome to Rainbow! We have the classic pool game... but on a computer and without water!") #Title for no real reason
print("\nPress 'I' for instructions.") #The key "I" will read you the instructions
print("Press 'L' for the list of acceptable colours.") #The key "L" will read out the 25 colours to choose from
print("Press 'P' to play the game.") #The key "P" will actually start the game
print("Press 'S' to stop the program.") #The key "S" will close the window
print("I'm not cap sensitive :)\n") #Quality of life feature :)

nerdz = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "Grey", "White", "Brown", "Gold", "Silver", "Bronze", "Lime", "Pink", "Magenta", "Turquoise", "Aquamarine", "Scarlet", "Maroon", "Beige", "Navy", "Mango", "Cream"] #The list of 25 colours

while True: #This loop is kept True so that you can repeat commands or if you want to play another game without reopening the program
    print("\nUse 'I', 'L', 'P', and 'S' to navigate.\n") #Reminder of what to use
    
    pog = str(input()) #This is the variable that determines which function is carried out
    
    if pog == "I" or pog == "i": #This block will handle what will happen when the key "I" is pressed
        print("\nWhen 'P' is pressed, the game will begin.\nThe program will then randomly select a colour.\nYou will then try to guess that colour.") #How to play
        print("When you do, you will have won the game.\nYou could then play again if you so please.\n") #How to play continued

    if pog == "L" or pog == "l": #This block will handle what will heppen when the key "L" is pressed
        print("\n") #Skips a line to look a little cleaner
        print(nerdz) #Reads out the list of 25 colours
        print("\n") #Skips a line to look a little cleaner

    if pog == "P" or pog == "p": #This block is where the actual game is
        
        THICC = 0 #When this variable turns into a "1", the while loop will end
        Nugget = 0 #This variable makes sure only one colour is generated per game

        import random #I need this to make sure the colour is psudo-random

        if Nugget == 0: #This makes sure I don't generate a new colour every turn
            for piaochamp in range(1): #The generator will only generate one colour
                Simp = random.randint(0, 24) #The integer is generated in a range of 25 values, but structered to fit the list
                yeet = nerdz[Simp] #Turns the random integer into a colour
                Nugget = 1 #Makes sure that only one colour is generated per game

        if Nugget == 1: #This will only happen once a colour is generated
            
            print("\nYou may begin the guessing, gl! :)") #Let the guessing commence!
            print("Also, you can access the list of colours by using 'L' or 'l' again!") #Quality of life feature :)
            print("Also, you can leave the game by using 'S' or 's'. :)") #In case you give up
            print("MAKE SURE THAT ALL OF YOUR GUESS ARE CAPITALIZED\n") #Quite an important bit of information
            
            while THICC == 0: #The while loop encompassing the game

                Stonks = str(input()) #The players guess at the correct colour

                if Stonks == "L" or Stonks == "l": #In case you forgot or are stumpted
                    print("\n") #Skips a line to look a little cleaner
                    print(nerdz) #Reads out the list of 25 colours
                    print("\n") #Skips a line to look a little cleaner

                if Stonks == "S" or Stonks == "s": #In case the player gives up
                    print("\nGiving up, eh? Honestly, I don't blame you.\n") #Bit of empathetic feedback
                    break #To send you back to the rest of the program
                
                if Stonks == yeet: #If you guessed correctly, this stuff happens
                    print("\nEyyyyyy, you won!") #Celebration :)
                    print("The colour was " + str(yeet) + ".\nYou can play again if you want! :)\n") #In case you forgot what it was
                    break #To send you back to the rest of the program

                if Stonks != yeet and Stonks != "L" and Stonks != "l": #If you guessed incorrectly, this happens
                    print("\nNot the one I had in mind, try again!\n") #Feedback
                    continue #idk if it needs to be here or not :p

    if pog == "S" or pog == "s":
        print("\n") #Skips a line to look a little cleaner
        print("Come back when your bored out of you're mind again!\n") #Cya later message
        quit() #Exits the program (Also nice ;) )