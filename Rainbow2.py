print("\nWelcome to Rainbow! We have the classic pool game... but on a computer and without water!") #Title for no real reason
print("\nPress 'I' for instructions.") #The key "I" will read you the instructions
print("Press 'L' for the list of acceptable colours.") #The key "L" will read out the 25 colours to choose from
print("Press 'P' to play the game.") #The key "P" will actually start the game
print("Press 'C' to add colours to the list. (No I doesn't have to be an actual colour, you can add 'Turtle' to the list if you want)") #The key "C" will allow the player to add colours or other strings to the list
print("Press 'S' to stop the program.") #The key "S" will close the window
print("\nI'm not cap sensitive :)") #Quality of life feature :)

nerdz = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "Grey", "White", "Brown", "Gold", "Silver", "Bronze", "Lime", "Pink", "Magenta", "Turquoise", "Aquamarine", "Scarlet", "Maroon", "Beige", "Navy", "Mango", "Cream"] #The starting list of 25 colours

THICC = 24

while True: #This loop is kept True so that you can repeat commands or if you want to play another game without reopening the program
    print("\n(MENU) Use 'I', 'L', 'P', 'C', and 'S' to navigate.\n") #Lets player know that they are in the menu, and serves as a reminder of what to use
    
    pog = str(input()) #This is the variable that determines which function is carried out
    
    if pog == "I" or pog == "i": #This block will handle what will happen when the key "I" is pressed
        print("\nWhen 'P' is pressed, the game will begin.") #How to play
        print("The program will then randomly select a colour.") #How to play continued
        print("You will then try to guess that colour.") #How to play continued
        print("When you do, you will have won the game.") #How to play continued
        print("You could then play again if you so please.") #How to play continued

    if pog == "L" or pog == "l": #This block will handle what will happen when the key "L" is pressed
        print("\n")
        print(nerdz) #Reads out the list of 25 colours

    if pog == "P" or pog == "p": #This block is where the actual game is
        import random #I need this to make sure the colour is pseudo-random
        
        Nugget = 0 #This variable makes sure only one colour is generated per game

        if Nugget == 0: #This makes sure I don't generate a new colour every turn
            for piaochamp in range(1): #The generator will only generate one colour
                Simp = random.randint(0, THICC) #The integer is generated in a range of 25 values, but structered to fit the list
                yeet = nerdz[Simp] #Turns the random integer into a colour
                Nugget = 1 #Makes sure that only one colour is generated per game

        if Nugget == 1: #This will only happen once a colour is generated
            
            print("\nYou may begin the guessing, gl! :)") #Let the guessing commence!
            print("Also, you can access the list of colours by using 'L' or 'l' again!") #Quality of life feature :)
            print("Also, you can leave the game by using 'B' or 'b'. :)") #In case you give up
            print("\nMAKE SURE THAT ALL OF YOUR GUESSES ARE CAPITALIZED\n") #Quite an important bit of information
            
            while True: #The while loop encompassing the game

                Stonks = str(input()) #The players guess at the correct colour

                if Stonks == "L" or Stonks == "l": #In case you forgot or are stumpted
                    print("\n") #Skips a line to look a little cleaner
                    print(nerdz) #Reads out the list of 25 colours
                    print("\n") #Skips a line to look a little cleaner

                if Stonks == "B" or Stonks == "b": #In case the player gives up
                    print("\nGiving up? I honestly don't blame you...") #Bit of empathetic feedback
                    print("\nReturning to menu...") #Just letting the player know
                    break #To send you back to the rest of the program
                
                if Stonks == yeet: #If you guessed correctly, this stuff happens
                    print("\nEyyyyyy, you won!") #Celebration :)
                    print("The colour was " + str(yeet) + ".\nYou can play again if you want! :)\n") #In case you forgot what it was
                    break #To send you back to the rest of the program

                if Stonks != yeet and Stonks != "L" and Stonks != "l": #If you guessed incorrectly, this happens
                    print("\nNot the one I had in mind, try again!\n") #Feedback
                    continue #idk if it needs to be here or not :p

    if pog == "C" or pog == "c": #This block will allow the user to add items to the list
        while True: #This loop will let the player add new items without being sent to the menu after every entry
            print("\nYou may now put a new item into the list.") #Giving the player the "Go ahead!"
            print("You can return to the menu by typing in 'Back'.\n")
            
            derp = str(input()) #This variable will be what the player decides to add, or will return the player to the menu
            
            if derp == "Back" or derp == "back": #This block will send the player to the menu if they choose to
                print("\nReturning to menu...") #Just letting the player know
                break #Returns the player to the menu
            
            if derp != "Back" or derp != "back":
                nerdz.append(derp) #This adds the player's custom item to the list
                THICC += 1 #This increases the range so that new items will be included in the random colour generator

                print("\n" + derp + " has been added to the list, press '1' to add another item, or '2' to return to the menu.\n") #Giving the player the option to add new items

                trump = str(input()) #This variable will either return the player to the menu, or let the player add a new item

                if trump == "1": #This block will let the player add a new item
                    continue #Nothing happens, except that the player can add a new item
                
                if trump == "2": #This block will return the player to the menu
                    print("\nReturning to menu...") #Just letting the player know
                    break #Returns the player to the menu

    if pog == "S" or pog == "s": #This block will let the player exit the program
        print("\nIf you really want to leave, press 'Y'. If you do not, press 'N'.\n") #A bit of a conformation
        print("LEAVING THE PROGRAM WILL ERASE ANY ADDITIONS MADE TO THE LIST!\n") #This may change the player's mind

        harambe = str(input()) #This variable will either let the player stay or go

        if harambe == "Y" or harambe == "y": #This block will make the player leave
            print("\n") #Skips a line to look a little cleaner
            print("Come back when your bored out of you're mind again!\n") #Cya later message
            quit() #Exits the program (Also nice ;) )

        if harambe == "N" or harambe == "n": #This block will return the player to the menu
            print("\nReturning to menu...") #Just letting the player know