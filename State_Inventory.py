from gameloop import gameloopfunction
class State():
    def __init__(self,text="",asciimap="",options="",statesout=[],code=0,workingitem="",usedtext="",nextstateafteritemuse=None,used=False,item="",itemdes="",itemtaken="",founditem="",itemtooken=False,afterusednextstatetext=""):
        self.text = text
        self.asciimap = asciimap
        self.options = options
        self.statesout = statesout
        self.code = code

        self.workingitem = workingitem
        self.usedtext = usedtext
        self.used = used
        self.nextstateafteritemuse = nextstateafteritemuse
        self.afterusednextstatetext = afterusednextstatetext

        self.item = item
        self.itemdes = itemdes
        self.itemtaken = itemtaken
        self.founditem = founditem
        self.itemtooken = itemtooken

        if self.text == "win":
            gameloopfunction()


    def makenextstate(self,temp):
        self.statesout = temp
    def defineitem(self,name,des,taken,found):
        self.item = name
        self.itemdes = des
        self.itemtaken = taken
        self.founditem = found
    def useitemsetup(self,workingitem,usedtext,nextstateafteritemuse=None,afterusednextstatetext=""):
        self.workingitem = workingitem
        self.usedtext = usedtext
        self.nextstateafteritemuse = nextstateafteritemuse
        self.afterusednextstatetext = afterusednextstatetext

    def printtext(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(self.asciimap+"\n\n")
        if self.item == "":
            x=0
            if self.used == False:
                print(self.text)
            elif self.used == True:
                x+=1
                print(self.usedtext)
                if self.afterusednextstatetext == None or self.afterusednextstatetext == "":
                    input("[Press enter to continue]")
                else:
                    print(str(x)+". "+str(self.afterusednextstatetext))
                    self.statesout.insert(0,self.nextstateafteritemuse)
            optionstext = ""
            for i in self.options:
                x+=1
                optionstext = optionstext + str(x) + ". " + i + "\n"
            print(optionstext)
            choose = input()
            if choose == "i":
                self.viewinventory()
            else:
                try:
                    self.nextstate(choose)
                except:
                    self.printtext()
        else:
            if self.itemtooken == False:
                choose = input(self.founditem+"\n"+"1. Take "+self.item+"\n")
                if choose == "1":
                    self.itemtooken = True
                    inventory.additem(self.item,self.itemdes)
                    self.nextstate(0)
                elif choose == "i":
                    self.viewinventory()
                else:
                    self.printtext()
            else:
                print(self.itemtaken)
                input("[Press enter to continue]")
                self.statesout[0].printtext()

    def nextstate(self,choose):
        choose = int(choose)-1
        if self.statesout[choose].code == 0:
            self.statesout[choose].printtext()
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(self.statesout[choose].asciimap+"\n\n")
            reponse = input("Enter code or press enter to go back.\n")

            if str(reponse) == str(self.statesout[choose].code):
                self.statesout[choose].statesout[0].printtext()
            else:
                self.printtext()

    def viewinventory(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("INVENTORY\n")
        x = 0
        for i in inventory.lst:
            x+=1
            print(str(x)+". "+i)
        if inventory.lst == {}:
            print("Empty\n")
            input("[Press enter to continue]")
            self.printtext()
        try:
            retrn = str(input("\nPick item\nOr C to cancel.\n"))
            if retrn == "c" or retrn == "C":
                self.printtext()
            theitem=list(inventory.lst)[int(retrn)-1]
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            dowhat = input("1. Examine\n2. Use\n3. Cancel\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if dowhat == "1":
                print(inventory.lst[theitem])
                input("[Press enter to continue]")
            elif dowhat == "2":
                if str(theitem) == self.workingitem:
                    if self.used == False:
                        self.used = True
                        self.nextstateafteritemuse.printtext()
                    else:
                        print("You already did that")
                        input("[Press enter to continue]")
                        self.printtext()
                else:
                    print(self.item)
                    print("The will not work.")
                    input("[Press enter to continue]")
                    self.printtext()
            else:
                self.viewinventory()
            self.viewinventory()
        except:
            self.viewinventory()


class Inventory():
    def __init__(self):
        self.lst = {}

    def additem(self,item,itemdes):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.lst[item]=itemdes
        print(itemdes)
        input("[Press enter to continue]")

inventory = Inventory()