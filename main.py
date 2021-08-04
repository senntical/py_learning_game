class Player:
    name = ""
    tags = {}

    def __init__(self, name, tags):
        self.name = name
        self.tags = tags

class Scene:
    title = ""
    description = ""
    choices = []

    def __init__(self, title, description, choices):
        self.title = title
        self.description = description
        self.choices = choices

class Choice:
    reqTags = {}
    givesTags = {}
    scene = ""
    description = ""
    toScene = ""

    def __init__(self, reqTags, givesTags, scene, description, toScene):
        self.reqTags = reqTags
        self.givesTags = givesTags
        self.scene = scene
        self.description = description
        self.toScene = toScene

def importStory(filename):
    # store values
    choices = []
    scenes = []
    tags = {}

    # parse the file
    currSection = ""
    readFile = open(filename)
    for line in readFile:
        line = line.strip()
        line = line.split("\\t")
        if(len(line) == 1):
            currSection = line[0]
        else:
            if(currSection == "CHOICES"):
                # tag interpretation
                newReqTags = {}
                reqTagStr = line[0]
                reqTagStr = reqTagStr.replace("{","")
                reqTagStr = reqTagStr.replace("}","")
                reqTagStr = reqTagStr.split(",")
                for item in reqTagStr:
                    item = item.split(":")
                    if(len(item) == 2):
                        newReqTags[item[0]] = item[1]

                # tag interpretation
                newGiveTags = {}
                giveTagStr = line[1]
                giveTagStr = giveTagStr.replace("{","")
                giveTagStr = giveTagStr.replace("}","")
                giveTagStr = giveTagStr.split(",")
                for item in giveTagStr:
                    item = item.split(":")
                    if(len(item) == 2):
                        newGiveTags[item[0]] = item[1]
                newChoice = Choice(newReqTags,newGiveTags,line[2],line[3],line[4])
                choices.append(newChoice)
            elif(currSection == "SCENES"):
                sceneChoices = []
                for c in choices:
                    if c.scene == line[0]:
                        sceneChoices.append(c)
                newScene = Scene(line[0],line[1],sceneChoices)
                scenes.append(newScene)
            elif(currSection == "TAGS"):
                tags[line[0]] = line[1]
    return scenes, tags

def main():
    scenes, playerTags = importStory("story.tsv")
    playerName = input("please enter your name:")
    newPlayer = Player(playerName, playerTags)
    playerInput = ""
    currentScene = scenes[0]

    # main loop
    while(1):
        print(currentScene.title)
        print(currentScene.description)
        indexNum = 0
        # display each choice
        for choice in currentScene.choices:
            # check if there are requirements
            if(len(choice.reqTags) > 0):
                for t in choice.reqTags:
                    if(t in newPlayer.tags):
                        if(newPlayer.tags[t] == choice.reqTags[t]):
                            print(str(indexNum) + ":   " + choice.description)
                            indexNum += 1
            else:
                print(str(indexNum) + ":   " + choice.description)
                indexNum += 1

        while(playerInput != "q"):
            playerInput = input("make a choice:")
            if playerInput == "q":
                exit()
            try:
                playerInput = int(playerInput)
            except ValueError:
                print("unexpected value")
                continue
            if(playerInput >= indexNum):
                print("invalid choice")
                continue
            # update tags
            for giveTag in currentScene.choices[playerInput].givesTags:
                print(currentScene.choices[playerInput].givesTags[giveTag])
                newPlayer.tags[giveTag] = currentScene.choices[playerInput].givesTags[giveTag]
            for s in scenes:
                # change scene
                if s.title == currentScene.choices[playerInput].toScene:
                    currentScene = s
                    break
            break


if __name__ == '__main__':
    main()
