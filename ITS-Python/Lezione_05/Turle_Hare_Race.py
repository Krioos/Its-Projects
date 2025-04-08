import random
import time
def display_race(hare_position, turtle_position):
    track = ['_'] * 70
    if hare_position > 70 or turtle_position > 70:
        return
    else:
        if hare_position == turtle_position:
            track[hare_position - 1] = 'OUCH!!!'
        else:
            track[turtle_position - 1] = 'T'
            track[hare_position - 1] = 'H'
        print(''.join(track))

def turtle_move(position,weather, turtle_stamina):
    move = random.randint(1, 10)
    if 1 <= move <= 4 and turtle_stamina >= 5:  # Passo veloce
        position += 3 if weather == "sunny" else 2
        turtle_stamina = max(0, turtle_stamina - 5)
    elif 5 <= move <= 7 and turtle_stamina >= 10:  # Scivolata
        position -= 6 if weather == "sunny" else 7
        turtle_stamina = max(0, turtle_stamina - 10)
    elif 8 <= move <= 10 and turtle_stamina >= 3 :  # Passo lento
        position += 1 if weather == "sunny" else 0
        turtle_stamina = max(0, turtle_stamina - 3)
    else:
        print("Too few stamina, Turtle can't move")
        turtle_stamina = min(turtle_stamina + 10, 100)
    if position in obstacles:
        print("Turtle hitted an obstacle!")
        position = position + obstacles[position]
    elif position in bonuses:
        print("Turtle got a bonus!")
        position = position + bonuses[position]       
    return max(1, position), turtle_stamina  

def hare_move(position, weather, hare_stamina):
    move = random.randint(1, 10)
    if 1 <= move <= 2:  # Riposo
        hare_stamina = min(hare_stamina +10, 100)
    elif 3 <= move <= 4 and hare_stamina >= 15:  # Grande balzo
        position += 9 if weather == "suny" else 7
        hare_stamina = max(0, hare_stamina - 15)
    elif move == 5 and hare_stamina >= 20:  # Grande scivolata
        position -= 12 if weather == "sunny" else 14
        hare_stamina = max(0, hare_stamina - 20)
    elif 6 <= move <= 8 and hare_stamina >= 5:  # Piccolo balzo
        position += 1 if weather == "sunny" else 0
        hare_stamina = max(0, hare_stamina - 5)
    elif 9 <= move <= 10 and hare_stamina >= 8:  # Piccola scivolata
        position -= 2 if weather == "sunny" else 4
        hare_stamina = max(0, hare_stamina -8)
    else:
        print ("Too few stamina, Hare can't move!")
    if position in obstacles:
        print("Hare hitted an obstacle!")
        position = position + obstacles[position]
    elif position in bonuses:
        print("Hare got a bonus!")
        position = position + bonuses[position] 
    return max(1, position), hare_stamina

obstacles = {15: -3, 30: -5, 45: -7}
bonuses = {10: 5, 25: 3, 50: 10}
hare_position = 1
turtle_position = 1
tick = 0
weather = "sunny"
turtle_stamina = 100
hare_stamina = 100
print("BANG !!!!! AND THEY'RE OFF !!!!!")
    
while hare_position < 70 and turtle_position < 70:
    tick += 1
    if tick % 10 == 0:
        weather = "rainy" if weather == "sunny" else "sunny"
        print(f"weather changed to {weather.upper()}!")
        
    hare_position, hare_stamina = hare_move(hare_position, weather, hare_stamina)
    turtle_position, turtle_stamina = turtle_move(turtle_position, weather, turtle_stamina)
    display_race(hare_position, turtle_position)
        
    if turtle_position >= 70 and hare_position >= 70:
        print("IT'S A TIE.")
        break
    elif turtle_position >= 70:
        print("TORTOISE WINS! || VAY!!!")
        break
    elif hare_position >= 70:
        print("HARE WINS || YUCH!!!")
        break
    time.sleep(0.5)