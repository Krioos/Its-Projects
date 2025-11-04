class Date():
    def __init__(self, date_str):
        try:
            day, month, year = date_str.split(".")
        except Exception:
            print("The date is not in the required format")
        else:
            self.year = self.getyear(int(year))
            self.month = self.getmonth(int(month))
            self.day = self.getday(int(day))


    def getday(self, day):
        if day:
            try:
                if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                    if 1 <= day <= 30:
                        return day
                    else:
                        raise ValueError
                elif self.month == 2:
                    if leap:
                        if 1<= day <=29:
                            return day
                        else:
                            raise ValueError
                    else:
                        if 1<= day <= 28:
                            return day
                        else:
                            raise ValueError
                else:
                    if 1 <= day <= 31:
                        return day
                    else:
                        raise ValueError
            except ValueError as e:
                print("The day is not acceptable")
        else:
            print("Day can't be empty")

    def getmonth(self, month):
        if month:
            if 1 <= month <= 12:
                return month
            else:
                print("The month is not acceptable")
                
        else:
            print("Month can't be empty")

    def getyear(self, year):
        global leap
        leap = False
        if year:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                leap = True
            return year
        else:
            print("Year can't be empty")

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

class Database:
    def __init__(self):
        self.dates = []

    def add_date(self, date_str):
        try:
            new_date = Date(date_str)
            if new_date not in self.dates:
                self.dates.append(new_date)
                print(f"Date:\n{new_date}\nsuccesfully added")
            else:
                print(f"Error {new_date} already in the database")
        except Exception:
            pass

    def delete_date(self, date_str):
        try:
            remove = Date(date_str)
            if remove in self.dates:
                self.dates.remove(remove)
                print(f"Date:\n{remove}\nremoved")
            else:
                print(f"Error no date {remove} in the database")
        except Exception:
            pass
    def modify_date(self, old_date_str, new_date_str):
        try:
                old_date = Date(old_date_str)
                if old_date in self.dates:
                    new_date = Date(new_date_str)
                    self.dates[self.dates.index(old_date)] = new_date
                    print(f"Date {old_date} modified to {new_date}.")
                else:
                    print(f"Date {old_date} not found in the database.")
        except Exception:
            pass
    
    def query_date(self,date_str):
        try:
            date_to_query = Date(date_str)
            if date_to_query in self.dates:
                print(f"Date {date_to_query} found in the database.")
            else:
                print(f"Date {date_to_query} not found in the database.")
        except Exception:
            pass
    def list_dates(self):
        # List all dates in the database in sorted order
        try:
            print("Dates in database:")
            for date in self.dates:
                print(date)
        except Exception:
            pass

# Example usage:
db = Database()

# Adding dates
db.add_date("10.05.2023")
db.add_date("01.01.2022")
db.add_date("15.03.2021")
db.add_date(input("Insert a date in dd.mm.yyyy format: "))

# Listing dates
db.list_dates()

# Querying dates
db.query_date("10.05.2023")
db.query_date("25.12.2025")

# Modifying a date
db.modify_date("15.03.2021", "16.03.2021")

# Deleting a date
db.delete_date("01.01.2022")
db.delete_date("01.01.2022")  # Try to delete a non-existing date

# Listing dates after modifications
db.list_dates()