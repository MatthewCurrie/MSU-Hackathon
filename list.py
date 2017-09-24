
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

Final = [None]*5

Prompt = "Are they a West SEC Division School"

if answer == True:
    Final[0] = "west"

    Prompt = "Is one of their school colors Crimson?"
    if answer == True:
        Final[1] = "crimson"
        #more here later

    elif answer == False:
        Prompt = "Is one of their school colors Red?"
        if answer == True:
            Final[1] = "red"
        elif answer == False:
            Prompt = "Is one of their school colors Orange?"
            if


elif answer == False:
    Final[0] = "east"
else:
    Final[0] = None

Prompt = "Is one of their school colors Red?"
if answer == True:
    Final[1] = "red"
    Prompt = "Is one of their school colors White?"
    if answer == True:
        Final
else:
    Final[1] = None



