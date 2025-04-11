from Es7 import User, Privileges, Admin

# Creiamo un'istanza di User
user1 = User("Mario", "Rossi", "mrossi", "mrossi@example.com")

# Creiamo un'istanza di Privileges con una lista di privilegi
privileges1 = Privileges(["can add post", "can delete post", "can ban user"])

# Creiamo un'istanza di Admin, passando l'oggetto User e l'oggetto Privileges
admin1 = Admin(user1, privileges1)

# Mostriamo le informazioni sull'utente e i privilegi
print(admin1.describe_admin())