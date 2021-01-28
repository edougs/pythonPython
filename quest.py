# choose your own adventure
import random

def Adventure_control():
    print("""Hello Arthur King of the Britons!

Who art on a quest to seek the grail...
    """)
    Bridge()
    print("back home")

def Bridge():
    print("""You come upon a bridge. It is the Bridge of Death!
and look -- it's the old man from scene 24!

He will ask you fiv- I mean three questions...""")
    Trivia()
    next_input = Direction("LR")
    if next_input.lower() =="l":
        dead("You are apprehended by the police!")
    elif next_input.lower() =="r":
        print("You went right?")

def Trivia():
    trivia_count = 0
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
        print("Do you go (L)eft or (R)ight?")
    elif way == "UD":
        print("Do you go (U)p or (D)own?")
    elif way == "IO":
        print("Do you go (I)n or (O)ut?")
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
