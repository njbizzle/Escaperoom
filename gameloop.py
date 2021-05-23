from time import sleep

from start_ascii import start_ascii

from story.tutorial.tutorial_story import tutorial_story_states
from story.bowling_alley.bowling_alley_story import bowling_alley_story_states


def gameloopfunction():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(start_ascii())
        input("[Press Enter To Start]")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        startmenu = input('''
        ---------------------
        #                   #
        #    1. START       #
        #                   #
        #    2. CONTINUE    #
        #                   #
        #    3. QUIT        #
        #                   #
        ---------------------
        ''')
        if startmenu == 1:
            tutorial_story_states().printtext()
        elif startmenu == 2:
            pass
        elif startmenu == 3:
            pass

        tutorial_story_states().printtext()
        bowling_alley_story_states().printtext()
