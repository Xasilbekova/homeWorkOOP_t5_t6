class Time:
    def __init__(self, hour, minute, second) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_time(self):
        print(f"Time: {self.hour:02d}:{self.minute:02d}:{self.second:02d}")

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def next_second(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def previous_second(self):
        self.second -= 1
        if self.second == -1:
            self.second = 59
            self.minute -= 1
            if self.minute == -1:
                self.minute = 59
                self.hour -= 1
                if self.hour == -1:
                    self.hour = 23

hour = int(input("Soatni kiriting (0-23): "))
minute = int(input("Daqiqani kiriting (0-59): "))
second = int(input("Sekundni kiriting (0-59): "))

time = Time(hour, minute, second)

print("\nOld time:")
time.get_time()

new_hour = int(input("\nYangi soatni kiriting (0-23): "))
new_minute = int(input("Yangi daqiqani kiriting (0-59): "))
new_second = int(input("Yangi sekundni kiriting (0-59): "))

time.set_time(new_hour, new_minute, new_second)

print("\nNew Time:")
time.get_time()

print("\nNext second:")
time.next_second()
time.get_time()

print("\nPrevious second:")
time.previous_second()
time.get_time()
