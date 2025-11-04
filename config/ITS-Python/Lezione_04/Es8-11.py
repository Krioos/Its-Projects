def send_messages(lista):
    sent_messages = []
    working_list = lista.copy()
    for elem in working_list:
        print(elem)
        sent_messages.append(elem)

    return sent_messages





lista  = [
    "riga 1",
    "Riga 2",
    "Riga 3",
    "Riga 4",
    "Riga 5"
]

messages = send_messages(lista)
print("%s,\n%s" %(lista, messages ))