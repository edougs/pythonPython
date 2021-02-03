# choose your own adventure
import random

def Adventure_control():
    print("""Hello Arthur King of the Britons!

Who art on a quest to seek the grail...
    """)
    Cave()
    #Bridge()
    print("back home")

def Cave():
    fight_rabbit_dict = {1:'Send Sir Bors',
                         2:'Attack!',
                         3:'Call for the Holy Hand Grenade',
                         4:'Run Away!',
                         5:'Call Brother Maynard'}
    grenade_instructions = '''First shalt thou take out the Holy Pin.
Then shalt thou count to three, no more, no less. Three shall be the number
thou shalt count, and the number of the counting shall be three. Four shalt
thou not count, neither count thou two, excepting that thou then proceed to
three. Five is right out. Once the number three, being the third number, be
reached, then lobbest thou thy Holy Hand Grenade of Antioch towards thy foe,
who, being naughty in my sight, shall snuff it.'''

    print('''You approach a rock-encircled clearing beyond which
is the mouth of a smokey cave. You spot an ordinary looking rabbit.

What will you do?''')
    try_again = True
    atlist = [1,2,3,4,5]
    while try_again:
        attack_choice = Attack(fight_rabbit_dict,atlist)
        if attack_choice == '1':
            print('The rabbit lunges for his neck!'
                  '\nIn an instant Sir Bors is dead...Now what?')
            atlist.remove(1)
        elif attack_choice == '2':
            print("Half your men are quickly dispatched! The rabbit made"
            "\nshort work of them. Color me impressed, but you probably "
            "\nshouldn't do that again.")
            atlist.remove(2)
        elif attack_choice == '3':
            print('You prepare to lob thou holy hand grenade at the rabbit.')
            if 5 in atlist:
                print('You pull the pin and count to 5! BOOM!')
                dead('Maybe you should consult the Book of Armaments first?')
            else:
                print('You count to 3, with some assistance, and throw the gren'
                'ade! A loud \nexplosion rocks the cave entrance. The rabbit is'
                ' destroyed! \nNearby, some police are startled from their '
                'investigation and look \ntoward the source of the noise.'
                '\n\n Success! The way is clear.')
                try_again = False
        elif attack_choice == '4':
            print('How brave! But the answers you seek are in that cave. '
            '\nSo...')
            atlist.remove(4)

        elif attack_choice == '5':
            print(grenade_instructions)
            atlist.remove(5)
        else:
            dead("Well that didn't help anything.")
    print('You move past the carnage to the entrance of the cave')
    next_input = Direction('IO')
    if next_input.upper() == 'O':
        dead('You are apprehended by the police!')
    elif next_input.upper() == 'I':
        #TO DO: in the cave is the writing in aramaic. and the beast
        print('You head in to the cave.')
    else:
        print('what is life?')



def Attack(attack_list, attack_range):
    for i in attack_range:
        print(f'{i}: {attack_list[i]}')
    attack_choice = input('>')
    return attack_choice

def Bridge():
    print('''You come upon a bridge. It is the Bridge of Death!
and look -- it's the old man from scene 24!

He will ask you fiv- I mean three questions...''')
    Trivia()
    next_input = Direction("LR")
    if next_input.upper() =="L":
        dead("You are apprehended by the police!")
    elif next_input.upper() =="R":
        #TO DO: from bridge is the lake and a castle where they are taunted
        print("You went right?")
    else:
        print('How did i get to this bridge?')

def Trivia():
    print("what is your name?")
    name = input('>')
    correct_answer = True
    print("what is your quest?")
    quest = input('>')
    if "grail" in quest:
        print("Very good.")
        correct_answer = True
    else:
        correct_answer = False

    if correct_answer:
        random_question = random.randrange(1,4)

    # print(random_question)
    if random_question == 1:
        print("What... is your favorite color?")
        ans = input('>')
        if "wait" in ans or "no" in ans:
            correct_answer = False
        else:
            print("Right. Off you go!")
            correct_answer = True
    elif random_question == 2:
        print("What... is the airspeed velocity of an unladen swallow?")
        ans= input('>')
        if "african" in ans.lower() or "european" in ans.lower():
            print("I don't know that! Arghhhhhhhh")
            correct_answer = True
    elif random_question == 3:
        print("What... is the capital of Assyria?")
        capital = input('>')
        if "ashur" in capital.lower() or "assur" in capital.lower():
            print("Right. Off you go!")
            correct_answer = True
        else:
            correct_answer = False
    else:
        print("You stare at each other...you both wonder how you got here.")
        correct_answer = False

    if correct_answer:
        print("You make your way over the bridge.")
    else:
        dead("You are cast into the Gorge of Eternal Peril.")

def Direction(way):
    if way == "LR":
        x='(L)eft'
        y='(R)ight'
    elif way == "UD":
        x='(U)p'
        y='(D)own'
    elif way == "IO":
        x='(I)n'
        y='(O)ut'
    print(f"Do you go {x} or {y}?")
    return input('>')

def dead(reason):
    random_condolence=['Rotten luck!','Ahh too bad!','We can''t all win.'
    ,'Well, you tried.']
    i = random.randrange(1,4)
    print(f"{reason} {random_condolence[i]} Do you want to try again? [Y/N]")
    ans = input('>')
    if ans.lower() =="y":
        Adventure_control()
    else:
        quit()



Adventure_control()
