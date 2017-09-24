
Alabama = ["west", "crimson", "white", True, "alabama"]
Arkansas= ["west", "red", "white", True, "arkansas"]
Auburn = ["west", "orange", "blue", True, "alabama"]
Florida = ["east", "orange", "blue", True, "florida"]
Georgia = ["east", "red" "black", True, "georgia"]
Kentucky = ["east", "blue", "white", True, "kentucky"]
LSU = ["west", "purple", "gold", True, "louisiana"]
MississippiSt = ["west", "maroon", "white", True, "mississippi"]
OleMiss = ["west", "red", "blue", True, "mississippi"]
Missouri = ["east", "black", "gold", True, "missouri"]
SouthCarolina =["east", "red", "black", True, "south carolina"]
Tennessee = ["east", "orange", "white", True, "tennessee"]
TexasAM = ["west", "maroon", "white", True, "texas"]
Vanderbilt = ["east", "black", "gold", False, "tennessee"]

Prompt = "Are they a West SEC Division School"

if answer == True:
    Prompt = "y"
elif answer == False:
    Prompt = "Is one of their school colors Orange?"

    if answer == True:
        Prompt = "Is their other school color Blue?"

        if answer == True:
            Prompt = "Is their school mascot a animal?"

            if answer == True:
                Prompt = "Is their school in Florida?"

                if answer == True:
                    Prompt = "Is the school The University of Florida?"

                    if answer == True:
                        Prompt = "The computer has guessed correctly."

                    elif answer == False:
                        Prompt = "Please repeat, you have hit a dead end."

                elif answer == False:
                    Prompt = "Please repeat, you have hit a dead end."

            elif answer == False:
                Prompt = "Please repeat, you have hit a dead end."

        elif answer == False:
            Prompt = "Is their other school color White?"

            if answer == True:
                Prompt = "Is their school mascot a animal?"

                if answer == True:
                    Prompt = "Is their school in Tennessee?"

                    if answer == True:
                        Prompt = "Is the school The University of Tennessee?"

                        if answer == True:
                            Prompt = "The computer has guessed correctly."

                        elif answer == False:
                            Prompt = "Please repeat, you have hit a dead end."

                    elif answer == False:
                        Prompt = "Please repeat, you have hit a dead end."

                elif answer == False:
                    Prompt = "Please repeat, you have hit a dead end."

    elif answer == False:
        Prompt = "Is one of their school colors Red?"

        if answer == True:
            Prompt = "Is their other school color Black?"

            if answer == True:
                Prompt = "Is their school mascot a animal?"

                if answer == True:
                    Prompt = "Is their school in Georgia?"

                    if answer == True:
                        Prompt = "Is the school The University of Georgia?"

                        if answer == True:
                            Prompt = "The computer has guessed correctly."

                        elif answer == False:
                            Prompt = "Please repeat, you have hit a dead end."

                    elif answer == False:
                        Prompt = "Is their school in South Carolina?"

                        if answer == True:
                            Prompt = "Is the school The University of South Carolina?"

                            if answer == True:
                                Prompt = "The computer has guessed correctly."

                            elif answer == False:
                                Prompt = "Please repeat, you have hit a dead end."

                        elif answer == False:
                            Prompt = "Please repeat, you have hit a dead end."
                            
                    elif answer == False:
                        Prompt = "Please repeat, you have hit a dead end."

                elif answer == False:
                    Prompt = "Please repeat, you have hit a dead end."
        elif answer == False:
            Prompt = "Is one of their school colors Blue?"

            if answer == True:
                Prompt = "Is their other school color White?"

                if answer == True:
                    Prompt = "Is their school mascot a animal?"

                    if answer == True:
                        Prompt = "Is their school in Kentucky?"

                        if answer == True:
                            Prompt = "Is the school The University of Kentucky?"

                            if answer == True:
                                Prompt = "The computer has guessed correctly."

                            elif answer == False:
                                Prompt = "Please repeat, you have hit a dead end."

                        elif answer == False:
                            Prompt = "Please repeat, you have hit a dead end."

                    elif answer == False:
                        Prompt = "Please repeat, you have hit a dead end."

            elif answer == False:
                Prompt = "Is one of their school colors Black?"

                if answer == True:
                    Prompt = "Is one of their school colors Gold?"
                    
                    if answer == True:
                        Prompt = "Is their school mascot a animal?"

                        if answer == True:
                            Prompt = "Is their school in Missouri?"

                            if answer == True:
                                Prompt = "Is the school The University of Missouri?"

                                if answer == True:
                                    Prompt = "The computer has guessed correctly."

                                elif answer == False:
                                    Prompt = "Please repeat, you have hit a dead end."

                            elif answer == False:
                                Prompt = "Please repeat, you have hit a dead end."

                        elif answer == False:
                            Prompt = "Is their school in Tennessee"

                            if answer == True:
                                Prompt = "Is the school Vanderbilt University?"

                                if answer == True:
                                    Prompt = "The computer has guessed correctly."

                                elif answer == False:
                                    Prompt = "Please repeat, you have hit a dead end."

                            elif answer == False:
                                Prompt = "Please repeat, you have hit a dead end."

                        elif answer == False:
                            Prompt = "Please repeat, you have hit a dead end."

                    elif answer == False:
                        Prompt = "Please repeat, you have hit a dead end."
                        
                elif answer == False:
                    Prompt = "Please repeat, you have hit a dead end."
                    
            elif answer == False:
                Prompt = "Please repeat, you have hit a dead end."

        elif answer == False:
            Prompt = "Please repeat, you have hit a dead end."

    elif answer == False:
        Prompt = "Please repeat, you have hit a dead end."

elif answer == False:
    Prompt = "Please repeat, you have hit a dead end."
