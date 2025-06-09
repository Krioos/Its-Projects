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


 