class Date:
    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        if self.day >= 1 and self.day < 10:
            print(f"Sana: 0{self.day}")
        elif self.day >= 10 and self.day <= 31:
            print(f"Sana: {self.day}")
        else:
            print("Bunday sana mavjud emas!")

    def get_month(self):
        if self.month >= 1 and self.month < 10:
            print(f"Oy: 0{self.month}")
        elif self.month >= 10 and self.month <= 12:
            print(f"Oy: {self.month}")
        else:
            print("Bunday oy mavjud emas!")

    def get_year(self):
        if self.year >= 1900 and self.year <= 9999:
            print(f"Yil: {self.year}")
        else:
            print("Bunday yil mavjud emas!")

    def get_date(self):
        if self.day >= 1 and self.day < 10 and self.month >= 1 and self.month < 10 and self.year >= 1900 and self.year <= 9999:
            print(f"Hozirgi vaqt: 0{self.day}/0{self.month}/{self.year}")
        elif self.day >= 10 and self.day <= 31 and self.month >= 10 and self.month <= 12 and self.year >= 1900 and self.year <= 9999:
            print(f"Hozirgi vaqt: {self.day}/{self.month}/{self.year}")

    def set_day(self, new_day):
        self.day = new_day
        if new_day >= 1 and new_day < 10:
            print(f"Sana: 0{new_day}")
        elif new_day >= 10 and new_day <= 31:
            print(f"Sana: {new_day}")
        else:
            print("Bunday sana mavjud emas!")

    def set_month(self, new_month):
        self.month = new_month
        if new_month >= 1 and new_month < 10:
            print(f"Oy: 0{new_month}")
        elif new_month >= 10 and new_month <= 12:
            print(f"Oy: {new_month}")
        else:
            print("Bunday oy mavjud emas!")

    def set_year(self, new_year):
        self.year = new_year
        if new_year >= 1900 and new_year <= 9999:
            print(f"Yil: {new_year}")
        else:
            print("Bunday yil mavjud emas!")

    def set_date(self, new_day, new_month, new_year):
        self.day = new_day
        self.month = new_month
        self.year = new_year
        if new_day >= 1 and new_day < 10 and new_month >= 1 and new_month < 10 and new_year >= 1900 and new_year <= 9999:
            print(f"Hozirgi vaqt: 0{new_day}/0{new_month}/{new_year}")
        elif new_day >= 10 and new_day <= 31 and new_month >= 10 and new_month <= 12 and new_year >= 1900 and new_year <= 9999:
            print(f"Hozirgi vaqt: {new_day}/{new_month}/{new_year}")

    def toString(self, new_day, new_month, new_year):
        if new_day >= 1 and new_day < 10 and new_month >= 1 and new_month < 10 and new_year >= 1900 and new_year <= 9999:
            print(f"Yangi vaqt strTypeda: 0{str(new_day)}/0{str(new_month)}/{str(new_year)}")
        elif new_day >= 10 and new_day <= 31 and new_month >= 10 and new_month <= 12 and new_year >= 1900 and new_year <= 9999:
            print(f"Yangi vaqt strTypeda: {str(new_day)}/{str(new_month)}/{str(new_year)}")

input_day = int(input("Sana ni kiriting (1-31): "))
input_month = int(input("Oy ni kiriting (1-12): "))
input_year = int(input("Yil ni kiriting (1900-9999): "))

date = Date(input_day, input_month, input_year)

print("Before:")
date.get_day()
date.get_month()
date.get_year()
date.get_date()

print("\nAfter:")
new_day = int(input("Yangi sana ni kiriting (1-31): "))
date.set_day(new_day)

new_month = int(input("Yangi oy ni kiriting (1-12): "))
date.set_month(new_month)

new_year = int(input("Yangi yil ni kiriting (1900-9999): "))
date.set_year(new_year)

date.set_date(new_day, new_month, new_year)
date.toString(new_day, new_month, new_year)
