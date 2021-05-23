from State_Inventory import State
from story.tutorial.tutorial_maps import asciimain,asciiright,asciileft,asciifront

def tutorial_story_states():
    start = State("Hello and Welcome to the tutorial, in this digital escape room you will be providied with one or more options and you choose what you want to do by typing the number before the option and pressing enter. \nAt anytime you can enter 'i' to open you inventory. \nThere is also a map above this text, here is a quick key\n\n| or - = wall\n[0] = the player\nH = low wall (such as a counter or shelfs)\n= = a chair or bench\nO = a table\n" ,asciimain,["Left","Forward","Right"],[])

    left = State("A room with just one table.",asciileft,["Examine table","Go back"])

    forward = State("A strong metal door with a small key pad, no way your breaking through that. You will need to find the code.",asciifront,["Go back"],[],4863)

    right = State("Nothing seems to be there, but out of the corner of your eye you see an object in a dark corner. Someone was trying to hide it.",asciiright,["Examine corner","Go back"])

    lockedbox = State("It is a small locked box, if only you could open it.",asciiright,["Go back"])


    boxoppend = State("The box opens, it has numbers written on the bottom, 4863. I wonder what that could mean.",asciiright, ["Go back"])

    crowbar = State("",asciileft)

    win = State("win")
    #######################

    lockedbox.useitemsetup("crowbar","The open box is just lying there. It still has the numbers writen on the bottom, 4863.",boxoppend)

    crowbar.defineitem("crowbar","Its a rusty crowbar, it might be able to brake open something small but its pretty old and weak.","You just see a outline of dust where the crowbar used to be.","In the shadows covered in dust and spiderwebs you see a rusty crowbar, it must have been there forever.")

    #######################

    start.makenextstate([left,forward,right])

    left.makenextstate([crowbar,start])

    forward.makenextstate([win])

    right.makenextstate([lockedbox,start])

    lockedbox.makenextstate([right])

    boxoppend.makenextstate([right])

    crowbar.makenextstate([left])

    return start