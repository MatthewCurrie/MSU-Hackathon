from tkinter import *

answer = None
root = Tk()


def yes():
    global answer
    answer = True
    var.set(1)


def no():
    global answer
    answer = False
    var.set(1)


def idk():
    global answer
    answer = True


root.update()
root.resizable(width=False, height=False)

topFrame = Frame(root, height=5, width=60)
topFrame.pack(side=TOP, fill=None, expand=False)

bottomFrame = Frame(root, height=10, width=60)
bottomFrame.pack(side=BOTTOM)


def printing():
    Label(topFrame, text=Prompt, height=5, font=10, width=60).grid(row=0, columnspan=3)


var = IntVar()

button1 = Button(bottomFrame, text="YES", bg="green", fg="white", height=10, width=20, font=10, command=yes)
button2 = Button(bottomFrame, text="NO", bg="red", fg="white", height=10, width=20, font=10, command=no)
button3 = Button(bottomFrame, text="IDK", bg="blue", fg="white", height=10, width=20, font=10, command=idk)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)


Prompt = "Are they a West SEC Division School"
printing()
button1.wait_variable(var)
if answer is True:
    Prompt = "Is one of their school colors Crimson?"
    answer = None
    printing()
    button1.wait_variable(var)
    if answer is True:
        Prompt = "Is their other school color White?"
        answer = None
        printing()
        button1.wait_variable(var)
        if answer is True:
            Prompt = "Is their school mascot an animal?"
            answer = None
            printing()
            button1.wait_variable(var)
            if answer is True:
                Prompt = "Is their school in Alabama?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is it University of Alabama?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "I guessed right!"
                    elif answer is False:
                        Prompt = "You're lying."
                elif answer is False:
                    Prompt = "You're lying."
            elif answer is False:
                Prompt = "You're lying."
        elif answer is False:
            Prompt = "You're lying."
    elif answer is False:
        Prompt = "Is one of their school colors Maroon?"
        answer = None
        printing()
        button1.wait_variable(var)
        if answer is True:
            Prompt = "Is their other school color White?"
            answer = None
            printing()
            button1.wait_variable(var)
            if answer is True:
                Prompt = "Is their school mascot an animal?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is their school in Texas?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is it Texas A&M?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "I guessed right!"
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "So it's Mississippi State?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "I guessed right!"
                        elif answer is False:
                            Prompt = "You're lying."
                elif answer is False:
                    Prompt = "You're lying."
            elif answer is False:
                Prompt = "You're lying."
        elif answer is False:
            Prompt = "Is one of their school colors Red?"
            answer = None
            printing()
            button1.wait_variable(var)
            if answer is True:
                Prompt = "Is their other school color Blue?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is their school mascot an animal?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is their school in Mississippi?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "Is it Ole Miss?"
                            answer = None
                            printing()
                            button1.wait_variable(var)
                            if answer is True:
                                Prompt = "I guessed right!"
                            elif answer is False:
                                Prompt = "You're lying."
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "You're lying."
                elif answer is False:
                    Prompt = "Is their other school color White?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is their school mascot an animal?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "Is their school in Arkansas?"
                            answer = None
                            printing()
                            button1.wait_variable(var)
                            if answer is True:
                                Prompt = "Is it Arkansas State University?"
                                answer = None
                                printing()
                                button1.wait_variable(var)
                                if answer is True:
                                    Prompt = "I guessed right!"
                                elif answer is False:
                                    Prompt = "You're lying."
                            elif answer is False:
                                Prompt = "You're lying."
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "You're lying."
            elif answer is False:
                Prompt = "Is one of their school colors Orange?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is their other color Blue?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is their mascot an animal?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "Is their school in Alabama?"
                            answer = None
                            printing()
                            button1.wait_variable(var)
                            if answer is True:
                                Prompt = "Is it Auburn?"
                                answer = None
                                printing()
                                button1.wait_variable(var)
                                if answer is True:
                                    Prompt = "I guessed right!"
                                elif answer is False:
                                    Prompt = "You're lying."
                            elif answer is False:
                                Prompt = "You're lying."
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "You're lying."
                elif answer is False:
                    Prompt = "Is one of their school colors Purple?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is their other color Gold?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "Is their mascot an animal?"
                            answer = None
                            printing()
                            button1.wait_variable(var)
                            if answer is True:
                                Prompt = "Are they in Louisiana?"
                                answer = None
                                printing()
                                button1.wait_variable(var)
                                if answer is True:
                                    Prompt = "Is it LSU?"
                                    answer = None
                                    printing()
                                    button1.wait_variable(var)
                                elif answer is False:
                                    Prompt = "You're lying."
                            elif answer is False:
                                Prompt = "You're lying."
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "There are no other primary school colors in SEC West."
elif answer is False:
    Prompt = "Is one of their school colors Orange?"
    answer = None
    printing()
    button1.wait_variable(var)
    if answer is True:
        Prompt = "Is their other school color Blue?"
        answer = None
        printing()
        button1.wait_variable(var)
        if answer is True:
            Prompt = "Is their school mascot a animal?"
            answer = None
            printing()
            button1.wait_variable(var)
            if answer is True:
                Prompt = "Is their school in Florida?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is the school The University of Florida?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "I guessed right!"
                    elif answer is False:
                        Prompt = "You're lying."
                elif answer is False:
                    Prompt = "You're lying."
            elif answer is False:
                Prompt = "You're lying."
        elif answer is False:
            Prompt = "Is their other school color White?"
            answer = None
            printing()
            button1.wait_variable(var)
            if answer is True:
                Prompt = "Is their school mascot a animal?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is their school in Tennessee?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is the school The University of Tennessee?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "I guessed right!"
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "You're lying."
                elif answer is False:
                    Prompt = "You're lying."
    elif answer is False:
        Prompt = "Is one of their school colors Red?"
        answer = None
        printing()
        button1.wait_variable(var)
        if answer is True:
            Prompt = "Is their other school color Black?"
            answer = None
            printing()
            button1.wait_variable(var)
            if answer is True:
                Prompt = "Is their school mascot a animal?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is their school in Georgia?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is the school The University of Georgia?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "I guessed right!"
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "Is their school in South Carolina?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "Is the school The University of South Carolina?"
                            answer = None
                            printing()
                            button1.wait_variable(var)
                            if answer is True:
                                Prompt = "I guessed right!"
                            elif answer is False:
                                Prompt = "You're lying."
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "You're lying."
                elif answer is False:
                    Prompt = "You're lying."
        elif answer is False:
            Prompt = "Is one of their school colors Blue?"
            answer = None
            printing()
            button1.wait_variable(var)
            if answer is True:
                Prompt = "Is their other school color White?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is their school mascot a animal?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is their school in Kentucky?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "Is the school The University of Kentucky?"
                            answer = None
                            printing()
                            button1.wait_variable(var)
                            if answer is True:
                                Prompt = "I guessed right!"
                            elif answer is False:
                                Prompt = "You're lying."
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "You're lying."
            elif answer is False:
                Prompt = "Is one of their school colors Black?"
                answer = None
                printing()
                button1.wait_variable(var)
                if answer is True:
                    Prompt = "Is one of their school colors Gold?"
                    answer = None
                    printing()
                    button1.wait_variable(var)
                    if answer is True:
                        Prompt = "Is their school mascot a animal?"
                        answer = None
                        printing()
                        button1.wait_variable(var)
                        if answer is True:
                            Prompt = "Is their school in Missouri?"
                            answer = None
                            printing()
                            button1.wait_variable(var)
                            if answer is True:
                                Prompt = "Is the school The University of Missouri?"
                                answer = None
                                printing()
                                button1.wait_variable(var)
                                if answer is True:
                                    Prompt = "I guessed right!"
                                elif answer is False:
                                    Prompt = "Please repeat, you have hit a dead end."
                            elif answer is False:
                                Prompt = "Please repeat, you have hit a dead end."
                        elif answer is False:
                            Prompt = "Is their school in Tennessee"
                            answer = None
                            printing()
                            button1.wait_variable(var)
                            if answer is True:
                                Prompt = "Is the school Vanderbilt University?"
                                answer = None
                                printing()
                                button1.wait_variable(var)
                                if answer is True:
                                    Prompt = "I guessed right!"
                                elif answer is False:
                                    Prompt = "You're lying."
                            elif answer is False:
                                Prompt = "You're lying."
                        elif answer is False:
                            Prompt = "You're lying."
                    elif answer is False:
                        Prompt = "You're lying."
                elif answer is False:
                    Prompt = "You're lying."
            elif answer is False:
                Prompt = "You're lying."
        elif answer is False:
            Prompt = "You're lying."
    elif answer is False:
        Prompt = "You're lying."

printing()

root.mainloop()
