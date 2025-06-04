class ContactManager():
    _contacts: dict[str, list[str]]
    def __init__(self)-> None:
        self._contacts = {}
    
    def create_contact(self, name: str, phone_numbers: list[str])-> dict[str,list[str]] | str:
        if name not in self._contacts:
            self._contacts[name] = phone_numbers
            return {name: phone_numbers}
        else:
            return "Errore il contatto esiste già"

    def add_phone_number(self, contact_name: str, phone_number: str)-> dict[str, list[str]] | str:
        if contact_name in self._contacts:
            if phone_number not in self._contacts[contact_name]:
                self._contacts[contact_name].append(phone_number)
                return {contact_name : self._contacts[contact_name]}
            else:
                return "Errore il numero di telefono esiste già"
        else:
            return "Errore il contatto non esiste"

    def remove_phone_number(self, contact_name: str, phone_number: str)-> dict[str, list[str]] | str:
        if contact_name in self._contacts:
            if phone_number in self._contacts[contact_name]:
                self._contacts[contact_name].remove(phone_number)
                return {contact_name: self._contacts[contact_name]}
            else:
                return "Il numero di telefono non esiste"
        else:
            return "Il contatto non esiste"
    
    def update_phone_number(self, contact_name: str, old_phone_number: str,
                             new_phone_number: str)-> dict[str, list[str]] | str:
        if contact_name in self._contacts:
            if old_phone_number in self._contacts[contact_name]:
                self.remove_phone_number(contact_name, old_phone_number)
                self.add_phone_number(contact_name, new_phone_number)
                return {contact_name: self._contacts[contact_name]}
            else:
                return "Errore il numero di telefono non esite"
        else:
            return "Errore il contatto non esiste"
    

    def list_contacts(self)-> list[str]:
        return list(self._contacts.keys())
    
    def list_phone_numbers(self, contact_name: str)-> list[str] | str:
        if contact_name in self._contacts:
            return self._contacts[contact_name]
        else:
            return "Errore il contatto non esiste"
    
    def search_contact_by_phone_number(self, phone_number: str)-> list[str] | str:
        out_list: list = []
        for k,v in self._contacts.items():
            for elem in v:
                if elem == phone_number:
                    out_list.append(k)
                    break
        if out_list:
            return out_list
        else:
            return "Nessun contatto trovato con questo numero di telefono."


cm = ContactManager()

# 1. Creo un nuovo contatto
print(cm.create_contact("Alice", ["123", "456"]))

# 2. Provo a creare Alice di nuovo
print(cm.create_contact("Alice", ["999"]))

# 3. Aggiungo un numero ad Alice
print(cm.add_phone_number("Alice", "789"))

# 4. Aggiungo un numero già esistente
print(cm.add_phone_number("Alice", "123"))

# 5. Aggiungo numero a contatto inesistente
print(cm.add_phone_number("Bob", "111"))

# 6. Rimuovo un numero esistente
print(cm.remove_phone_number("Alice", "456"))

# 7. Rimuovo numero inesistente
print(cm.remove_phone_number("Alice", "000"))

# 8. Aggiorno numero esistente
print(cm.update_phone_number("Alice", "789", "999"))

# 9. Aggiorno numero inesistente
print(cm.update_phone_number("Alice", "000", "111"))

# 10. Lista contatti
print(cm.list_contacts())

# 11. Lista numeri di Alice
print(cm.list_phone_numbers("Alice"))

# 12. Lista numeri di contatto inesistente
print(cm.list_phone_numbers("Bob"))

# 13. Ricerca per numero esistente
print(cm.search_contact_by_phone_number("123"))

# 14. Ricerca per numero inesistente
print(cm.search_contact_by_phone_number("000"))
 