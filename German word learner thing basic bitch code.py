#kai hemmings
#project started 16/06/2020
#title - i need mental support

import random


the_gate_to_hell = """
---------------------------------------
would you like begin this shitty thing?
yes
no
Option:"""

such_awesome_thing = """
ya fukkin know that word hmmm you retard
1 - yes
2 - no
Option:"""

global Auschwitz
global Schindlers_list
global Boris_list

def piece_of_shit_word_thing():
    while True:
        
        global Auschwitz
        Auschwitz = int(input("choose number (over 40 dipshit)"))
        
        if Auschwitz < 1:
            print ("DID YOU FUCKING READ THE THING ABOVE YOU PIECE OF SHIT")

        else:
            return Auschwitz

def hitler_was_right():

    global Schindlers_list
    global Boris_list
    global Insults

    with open('Schindlers_List.txt') as Schindlers_list:
        Schindlers_list = Schindlers_list.read().splitlines()
        lines = []
        for line in Schindlers_list:
            lines.append(line)
        
    with open('Slaves_List.txt') as Boris_list:
        Boris_list = Boris_list.read().splitlines()
        lines = []
        for line in Boris_list:
            lines.append(line)

    with open('Insults.txt') as Insults:
        Insults = Insults.read().splitlines()
        lines = []
        for line in Insults:
            lines.append(line)

    return Schindlers_list
    return Boris_list
    return Insults
    

def so_you_have_chosen_death():

    global Auschwitz
    global Schindlers_list
    global Boris_list
    global Insults

    while True:

        while Auschwitz != 0:

            part1 = len (Schindlers_list) - 1
            part2 = random.randint(0, part1)
            word = str(Schindlers_list[part2])
            answer = str(Boris_list[part2])
            #print (part1, part2)
            #print (word, answer)   debug thingy


            print ()
            print ("on this long list we have", Auschwitz,"jew(s) left")
            print (word)
            the_chamber = int(input(such_awesome_thing))

            if the_chamber == 1:
                shooting_range = input("WhAT iS ThE ENglIsH TrAnsLaTIOn MoTHeR fUCkEr:")

                if shooting_range == answer:
                    print ()
                    print ("hooray you dumb autistic fuck nugget you got it right")
                    Auschwitz = Auschwitz - 1

                elif shooting_range != answer:
                    print ()
                    print ("you dumb piece of shit can't you get one fucking thing done in your life just off yourself now so you don't become a total disapointment later")
                    print ("also the english word was",answer,"dipshit")
                    Auschwitz = Auschwitz + 0
                
            elif the_chamber == 2:
                print ("fuck me you are dummb it is",answer)
                numberjacks = len(Insults) - 1
                dumbdumb = random.randint(0, numberjacks)
                print (Insults[dumbdumb])

            else:
                print ('wrong thing you daft cunt get it right')

        if Auschwitz == 0:
            fuck_outta_here()

def fuck_outta_here():
    while True:
        gas_gas_gas = input("""
---------------------------------
well you gonna do this shit again
yes
no
Option:""")
        if gas_gas_gas == "yes":
            confirm = input('are you sure????')
            if confirm == 'yes':
                fight_screen()
            else:
                fuck_outta_here()
        elif gas_gas_gas == "no":
            for i in range(0, 3):
                print ('quitting...')
                quit ()

def fight_screen():
    while True:
        option = input (the_gate_to_hell)
        if option == "yes":
            piece_of_shit_word_thing()
            hitler_was_right()
            so_you_have_chosen_death()
            
        elif option == "no":
            for i in range(0, 3):
                print ('quitting...')
                quit ()

while True:
    fight_screen()
