char_flags = {"c_race": "NONE", "c_weapon": "NONE"} # dictionary containing flags for race and weapon choices; this can be updated throughout the script

char_races = ["Human","Elf","Orc"] # list containing races; unlikely to be updated later in the script

char_weapons = ["Sword","Bow"] # list containing weapons; unlikely to be updated later in the script

 
def test_funct(race): # function to print out selection options for race all on one line - this is silly complicated for just that
    print("Available races are: ") # prints out a line indicating what the user should do
    race_count = len(char_races) # counts how many entries there are in char_races and returns that as an integer
    for x in race: # x is defined here; it loops through the list "race" setting itself equal to the current entry in race - it is the actual entry in the array, not an index number
        current_idx = race.index(x) # sets an integer based on the current index number of the entry of race (ex: Human = 0, Elf = 1, Orc =2)
        list_end = race_count - current_idx # determines when the list ends; number decreases each loop as current_idx increases
        if list_end != 1: # checking if  the value of list_end has reached 1, which would indicate the end of the list (why?)
            print(race[current_idx], end = ", ") # prints out the current value assigned to "race" based on the current_idx value, then add a , and space at the end
        else: 
            print("or " + race[current_idx], end = '\n\n') # prints out the current value assigned to "race" based on the current_idx value, then adds a return at the end so new prints are not on the same line

print ("Races: ", *char_races, sep=", ")


while True:

    test_funct(char_races) # calling the function test_funct and telling it to use char_races as the input for "race"

   
    char_select = input("   Please select a race: \n").lower()

    char_races_lower = [x.lower() for x in char_races]  # creates a new list called char_races_lower from char_races that is all lower case

    if char_select == char_races_lower[0]: # forces char_select to be all lower case and then checks if it is in the char_races_lower list
        char_flags["c_race"] = char_races[0]
        break
    elif char_select == char_races_lower[1]:
        char_flags["c_race"] = char_races[1]
        break
    elif char_select == char_races_lower[2]:
        char_flags["c_race"] = char_races[2]
        break
    else:
        print("--Not a valid race--\n")



#char_flags["c_race"] = "Elf" # for testing purposes, this set "c_race" to "Elf" - this will be replaced with user input

print("Player's selected race is " + char_flags["c_race"]) # informs user of selected "c_race" value after "c_race" has been updated with user selection
