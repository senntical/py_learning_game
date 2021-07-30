#do = input(":: ")
#if do == "LOOK":
#    print("You are stuck in a sand ditch.")
#    print("Crawl out LEFT or RIGHT.")
#
#   do = input(":: ")
#    if do == "LEFT":
#        print("You make it out and see a ship!")
#        print("You survived!")
#    elif do == "RIGHT":
#        print("No can do. That side is very slippery.")
#        print("You fall very far into some weird cavern.")
#        print("You do not survive :(")
#else:
#    print("You can only do actions shown in capital letters.")
#    print("Try again!")


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