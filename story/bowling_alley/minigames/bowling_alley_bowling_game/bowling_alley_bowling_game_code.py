from random import randint
from time import sleep
timeing_one = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
timeing_one_key = [0,1,3,6,8,10,8,6,3,1,0,0,0,0,0]
timeing_two = ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "]
timeing_two_key = ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "]
g1 = ["   ","   ","   ","   ","   ","   ","   "]
g2 = ["   ","   ","   ","   ","   ","   ","   "]
l = ["   ","   ","   ","   ","   ","   "]
m = ["   ","   ","   ","   "]
h = ["   ","   ","   ","   ","   "]
a = ["   ","   ","   ","   ","   ","   ","   "]
def screen():
    return f'''
    |-----|-----|-----|-----|-----|-----|
    |     | ({g2[6]}: L L L L L :{g1[6]}) | {timeing_one[0]} 00
    |     | ({g2[5]}:{l[5]}L L L   :{g1[5]}) | {timeing_one[1]} 01
    |     | ({g2[4]}:{l[4]}  L{h[4]}  :{g1[4]}) | {timeing_one[2]} 03
    |     | ({g2[3]}:{l[3]} {m[3]}{h[3]} :{g1[3]}) | {timeing_one[3]} 06
    |     | ({g2[2]}:{l[2]} {m[2]}{h[2]} :{g1[2]}) | {timeing_one[4]} 08
    |     | ({g2[1]}:{l[1]} {m[1]} {h[1]}:{g1[1]}) | {timeing_one[5]} 10!
    |     | ({g2[0]}:{l[0]} {m[0]} {h[0]}:{g1[0]}) | {timeing_one[6]} 08
    |     | (   :{a[4]} {a[5]} {a[6]}:   ) | {timeing_one[7]} 06
    |     | (   : {a[1]}{a[2]}{a[3]} :   ) | {timeing_one[8]} 03
    |     | (   :    {a[0]}    :   ) | {timeing_one[9]} 01
    |     |_ _ _ _ _ _ _ _ _ _ _ _| {timeing_one[10]} 00
    |     |         ____          | {timeing_one[11]} 00
    |     |        / '' \         | {timeing_one[12]} 00
    |     |       |   '  |        | {timeing_one[13]} 00
    |     |        \____/         | {timeing_one[14]} 00
    |-----------------------------------|
    | {timeing_two[0]} {timeing_two[1]} {timeing_two[2]} {timeing_two[3]} {timeing_two[4]} {timeing_two[5]}  {timeing_two[6]} {timeing_two[7]} {timeing_two[8]} {timeing_two[9]} {timeing_two[10]} |
    |-00-01-03-06-08-10!-08-06-03-01-00-|
    |          B O W L I N G            |
    |-----------------------------------|
    '''
def timeing_one_start():
    for i in range(len(timeing_one)):
        timeing_one[i] = "[=]"
        print(screen())
        sleep(0.2)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        timeing_one[i] = "   "








def print_as(indec):
    a[indec] = "(+)"
    print(screen())
    sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    a[indec] = "   "

def lowscore():
    print_as(0)
    print_as(1)
    print_as(4)
    for thing in range(len(l)):
        l[thing] = "(+)"
        print(screen())
        sleep(0.5)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        l[thing] = "   "

def medscore():
    print_as(0)
    print_as(2)
    print_as(5)
    for thing in range(len(m)):
        m[thing] = "(+)"
        print(screen())
        sleep(0.5)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        m[thing] = "   "

def highscore():
    print_as(0)
    print_as(3)
    print_as(6)
    for thing in range(len(h)):
        h[thing] = "(+)"
        print(screen())
        sleep(0.5)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        h[thing] = "   "

def guter():
    ran = randint(1,2)
    if ran == 1:
        print_as(0)
        print_as(3)
        print_as(6)
        for thing in range(len(g1)):
            g1[thing] = "(+)"
            print(screen())
            sleep(0.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            g1[thing] = "   "
    else:
        print_as(0)
        print_as(1)
        print_as(4)
        for thing in range(len(g2)):
            g2[thing] = "(+)"
            print(screen())
            sleep(0.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            g2[thing] = "   "