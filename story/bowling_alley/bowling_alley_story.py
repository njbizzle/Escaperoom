from State_Inventory import State
from story.bowling_alley.bowling_alley_maps import asciistart,asciifood_place,asciifood_place_behind_counter,asciibehind_check_in_area_counter,asciicheck_in_area,asciisit_down,asciifood_closet_inside,asciilook_at_seats,asciilook_at_sign

def bowling_alley_story_states():
    start = State("You wake up and your in a some big dark room with high celling and a carpeted floor. As you start to get up the lights flicker on and you seem to be in the check in area for some run down bowling alley. \nYou look to your left and you see the check in counter and behind that a rack of shoes. \nIn front of you there is a big sign that says FOOD, it is flickering and barely works, underneath that you see what looks like a food stand. \nThere are seats every where, probably for the food stand. \n Everything looks really old are rusted but you turn around and there is the door out, but its locked. The lock seems to be the only thing that was new. You cant live in here you got to escape.",asciistart,["Open door","Examine check-in counter.","Go to food stand.","Check out seats."])

    check_in_area = State("The counter is  empty with just some dust. Behind is a huge rack of shoes you can see some finger the lock again looks new. you look more closely and in one of the shoes you see a rolled up piece of paper. You know people check the shoes when the put them back and you can't miss rolled up paper in your shoe so someone must have left it here after the place closed down. Its to fat back to reach but you might be. able to get it if you had a key to the shoe rack.",asciicheck_in_area,["Go behind counter.","Go back."])

    behind_check_in_counter = State("You climb behind the counter and are about to go try and open the rack when you notice a small box.",asciibehind_check_in_area_counter,["Open rack of shoes.","Examine box.","Examine coat.","Go back."])

    small_box_closed = State("It's locked with a keypad.",asciibehind_check_in_area_counter,["Open","Go back."])

    open_small_box = State("",asciibehind_check_in_area_counter,[],[],7632)

    coat_knife = State("",asciibehind_check_in_area_counter)

    rack_of_shoes_outside = State("The paper is sitting in one of the shoes just out of reach, you will need a key to get in.",asciibehind_check_in_area_counter,["Go back."])

    rack_of_shoes = State("You rush in to the shoe rack to grab the paper, and as you bend down you see under the shoe rack, there is tons of stuff and someone must have dropped something important at some point.",asciibehind_check_in_area_counter,["Go get paper.","Examine underneath shoe rack.","Go Back."])

    clue_one = State("You pick up the paper and it reads: 'The sum of all of the digits is 16 and no number is greater than the one left of it.'\n[Clue 2/3. Write this down.]",asciibehind_check_in_area_counter,["Go back."])

    shoe_rack_floor = State("",asciibehind_check_in_area_counter)

    #####

    food_place = State("You walk up to the counter to your right is a way behind and to your left is the big flickering neon sign. You stare at it for a second then you look down at the counter and there is a half eaten hot dog.",asciifood_place,["Inspect hot dog.","Examine sign","Go behind counter.","Go back."])

    look_at_sign = State("Its flickering and has not been well keeped for at least the past 2 or 3 years.",asciifood_place,["Go back."])

    look_at_hot_dog = State("The fist thing that you notice is that the hot dog does not smell horrible, it would be decaying if it was half as old as everything else here. Who ever trapped you here got hungry.",asciifood_place,["Go Back."])

    food_place_behind_counter = State("You walk behind the counter and pause you look around you can't live here, you need to find a way out fast. You see door to some sort of closet as well as some food making machines such as a popcorn popper and a hot dog roller.",asciifood_place_behind_counter,["Open door.","Inspect popcorn maker and hot dog roller.", "Go back."])

    food_machines = State("The popcorn machine is dark, nothing but mold in there. You look at the hotdog roller and feel it, its not hot just a little warm, someone used it recently.",asciifood_place_behind_counter,["Go back."])

    food_closet_outside = State("The door is locked, you will need a key to get in.",asciifood_place_behind_counter,["Go back."])

    food_closet_and_clue_two = State("You walk in and kitchen supplies and rotten food on every shelf, all the food is rotten but the hot dog wasn't. Your thinking is interrupted when you look down and and written on the floor with a spray can are the words:'The first and third digits are the only odd numbers and they add up to 10.'\n[Clue 3/3. Write this down.]'",asciifood_closet_inside,["Go back."])

    #####

    look_at_seats = State("You go to sit down and think, you start to sit when something catches your eye, under the seat there is something, its white witch is wierd because everything else is grey from the years of dust accumulated under the seats.",asciilook_at_seats,["Look under seat.","Sit down.","Go back."])

    look_under_seats = State("You reach under the seat and pull out a crumpled piece of paper, you unfold it and read it, it says: 'The final code is between 6000 - 8000 and every digit is greater than zero'\n[Clue 1/3. Write this down.]",asciilook_at_seats,["Go back."])

    sit_down = State("You decide to sit down and think, as soon as you sit down the cushion starts to rattle. There is something sewn into the cushion, it sounds like a key. You try to pick up the cushion but it to is sewn in to the seat. You look for a zipper with no luck. You'll need something like a pocket knife to cut through that.",asciisit_down,["Go back."])

    cushion_open = State("",asciilook_at_seats)

    #######################

    open_small_box.defineitem("bowling alley key","Again with the sharpie on masking tape it says bowling alley.","You open the box once more and it just empty, what did you expect.","The box clicks open and you reach inside a take out a key, written on the key is bowling alley. It's well protected and probably very important.")

    coat_knife.defineitem("knife","Its just a old pocket knife.","You look in the coat and there is not thing new, just the pocket where you found the knife.","You reach in the pockect and something sharp gives you a small cut on you finger, it's a pocket knife. This should be really useful.")

    shoe_rack_floor.defineitem("food storage key","A normal key with some masking tape on it and in sharpie with food storage written on top of the masking tape.","I dont see anything new under here. Its seems that the only thing of value was the key you took.","You stick you hand in to the discarded pen and pieces of paper, lint and dust. Then suddenly *clink*, it sounds like a key. You bring it out and it is a key. Its labled food storage, I wonder where that is.")

    rack_of_shoes_outside.useitemsetup("shoe rack key","The door is still open and you walk in you see the paper and the bottom of the shoe rack still looks pretty messy.",rack_of_shoes,"Examine shoe rack.")

    food_closet_outside.useitemsetup("food closet key","You walk through the open door to the food closet.",food_closet_and_clue_two,"Walk in to food closet")

    sit_down.useitemsetup("knife","You go to sit down and end up sitting in the pile of cushion fluff from the cushion you cut open.",cushion_open)

    cushion_open.defineitem("shoe rack key","In sharpie on masking tape is written shoe rack key.","If you are reading this something went wrong, tell me. It doesnt count if you reading this in the code.","You tear open the cushion with your knife a reach inside to find a key, its to the shoe rack. Your should make your way over there.")

    win = State()

    #######################

    start.makenextstate([win,check_in_area,food_place,look_at_seats])

    check_in_area.makenextstate([behind_check_in_counter,start])

    behind_check_in_counter.makenextstate([rack_of_shoes_outside,small_box_closed,coat_knife,check_in_area])

    small_box_closed.makenextstate([open_small_box,behind_check_in_counter])

    open_small_box.makenextstate([behind_check_in_counter])

    coat_knife.makenextstate([behind_check_in_counter])

    rack_of_shoes_outside.makenextstate([behind_check_in_counter])

    rack_of_shoes.makenextstate([clue_one,shoe_rack_floor,behind_check_in_counter])

    clue_one.makenextstate([behind_check_in_counter])

    shoe_rack_floor.makenextstate([behind_check_in_counter])

    food_place.makenextstate([look_at_hot_dog,look_at_sign,food_place_behind_counter,start])

    look_at_sign.makenextstate([food_place])

    look_at_hot_dog.makenextstate([food_place])

    food_place_behind_counter.makenextstate([food_closet_outside,food_machines,food_place])

    food_machines.makenextstate([food_place_behind_counter])

    food_closet_outside.makenextstate([food_place_behind_counter])

    food_closet_and_clue_two.makenextstate([food_place_behind_counter])

    look_at_seats.makenextstate([look_under_seats,sit_down,start])

    look_under_seats.makenextstate([look_at_seats])

    sit_down.makenextstate([look_at_seats])

    cushion_open.makenextstate([look_at_seats])

    return start