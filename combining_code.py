char_flags = {"c_race": "NONE", "c_weapon": "NONE"} # dictionary containing flags for race and weapon choices; this can be updated throughout the script

char_races = ["Human","Elf","Orc"] # list containing races; unlikely to be updated later in the script

char_weapons = ["Sword","Bow"] # list containing weapons; unlikely to be updated later in the script

 
# this is a long function for printing all items in char_races onto one line with different separators (, or and) 
#def test_funct(race): # function to print out selection options for race all on one line - this is silly complicated for just that
#    print("Available races are: ") # prints out a line indicating what the user should do
#    race_count = len(char_races) # counts how many entries there are in char_races and returns that as an integer
#    for x in race: # x is defined here; it loops through the list "race" setting itself equal to the current entry in race - it is the actual entry in the array, not an index number
#        current_idx = race.index(x) # sets an integer based on the current index number of the entry of race (ex: Human = 0, Elf = 1, Orc =2)
#        list_end = race_count - current_idx # determines when the list ends; number decreases each loop as current_idx increases
#        if list_end != 1: # checking if  the value of list_end has reached 1, which would indicate the end of the list (why?)
#            print(race[current_idx], end = ", ") # prints out the current value assigned to "race" based on the current_idx value, then add a , and space at the end
#        else: 
#            print("or " + race[current_idx], end = '\n\n') # prints out the current value assigned to "race" based on the current_idx value, then adds a return at the end so new prints are not on the same line

#print ("Races: ", *char_races, sep=", ")


while True:

    #test_funct(char_races) # calling the function test_funct and telling it to use char_races as the input for "race"

    # this prints out all entries in char_races as a string with , inbetween each entry
    # not sure yet how to add "and" inbetween the last two entries, or if I even want to
    print(f"Available races are: {', '.join(x for x in char_races)}")
   
    char_select = input("Please select a race: \n").lower()

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

print("Player's selected race is " + char_flags["c_race"]) # informs user of selected "c_race" value after "c_race" has been updated with user selection

q_awake = {"Question":"Are you awake?","Choice1":"Yes","Choice2":"No"}
a_awake = {"AnswerC1":"GoTo:q_floating","AnswerC2":"Enjoy your sleep."}

q_floating = {"Question":"Are you floating?","Choice1":"Yes","Choice2":"No","Choice3":"Over Jupiter"}
a_floating = {"AnswerC1":"GoTo:q_ham_hot","AnswerC2":"Sad day!","AnswerC3":"Must look pretty up there."}

q_ham_hot = {"Question":"Do you prefer hamburgers or hotdogs?","Choice1":"Hamburgers","Choice2":"Hotdogs","Choice3":"Gross!!"}
a_ham_hot = {"AnswerC1":"Awesome choice!","AnswerC2":"Well, I guess that's alright","AnswerC3":"Really?!?!"}

def question_awake():
    print(q_awake["Question"],":",q_awake["Choice1"],",",q_awake["Choice2"])
    answer = input(":: ").lower()
    if answer == q_awake["Choice1"].lower():
            question_floating()
    elif answer == q_awake["Choice2"].lower():
            print(a_awake["AnswerC2"])
    else:
        print("Bad answer, exiting")

def question_floating():
    print(q_floating["Question"],":",q_floating["Choice1"],",",q_floating["Choice2"])
    answer = input(":: ").lower()
    if answer == q_floating["Choice1"].lower():
        question_ham_hot()
    elif answer == q_floating["Choice2"].lower():
        print(a_floating["AnswerC2"])
    elif answer == q_floating["Choice3"].lower():
        print(a_floating["AnswerC3"])
    else:
        print("Bad answer, exiting")

def question_ham_hot():
    print(q_ham_hot["Question"],":",q_ham_hot["Choice1"],",",q_ham_hot["Choice2"],",",q_ham_hot["Choice3"])
    answer = input(":: ").lower()
    if answer == q_ham_hot["Choice1"].lower():
        a_ham_hot["AnswerC1"]
    elif answer == q_ham_hot["Choice2"].lower():
        a_ham_hot["AnswerC2"]
    elif answer == q_ham_hot["Choice3"].lower():
        a_ham_hot["AnswerC3"]
    else:
        print("Bad answer, exiting")
            

question_awake()