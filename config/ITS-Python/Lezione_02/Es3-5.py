guests = ["Raffaello", "Ichigo", "Bob Dole", "Leonardo da Vinci", "Trump"]
for elem in guests:
    print(F"Hy {elem} welcome to the party!")

print("Oh no it seems Raffaello will not be able to come to the party")
guests.remove("Raffaello")


print("Snoop is now coming to the party")
guests.append("Snoop")
for elem in guests:
    print(F"Hy {elem} welcome to the party!")
