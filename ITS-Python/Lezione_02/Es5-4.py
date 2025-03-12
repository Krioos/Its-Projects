from random import choice

alien_colour:str = choice(["verde", "rosso", "giallo"])

if alien_colour == "verde":
    print(f"Alieno {alien_colour}! 5 punti")
else:
    print(f"Alieno {alien_colour}! 10 punti ")