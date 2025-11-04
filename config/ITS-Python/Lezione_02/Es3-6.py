guests = ["Raffaello", "Ichigo", "Bob Dole", "Leonardo da Vinci", "Trump"]
for elem in guests:
    print(F"Hy {elem} welcome to the party!")

print("Oh no it seems Raffaelo will not be able to come to the party")
guests.remove("Raffaello")



print("Snoop is now coming to the party")
guests.append("Snoop")
for elem in guests:
    print(f"Hy {elem} welcome to the party!")

print("Hey guys I've just found a bigger table, three new guests can join now!")
guests.insert(0, "M&M")
guests.insert(int(len(guests)//2), "Pol Pot")
guests.append("Stalin")

for elem in guests:
    print(f"Hy {elem} welcome to the party!")