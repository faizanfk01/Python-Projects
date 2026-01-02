class Car:
    def __init__(self, brand, color, model, year):
        self.brand = brand
        self.color = color
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if self.is_running:
            print(f"\nYour {self.brand} {self.model} is already running!")

        else:
            self.is_running = True
            print(f"\nYour {self.brand} {self.model} starts. Vroom Vroom!")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"\nYour {self.brand} {self.model} engine is turned off!")

        else:
            print(f"\nYour {self.brand} {self.model} engine is already Off!")

    def drive(self, distance):
        if self.is_running:
            print(f"\nYour {self.brand} {self.model} is driving {distance} km")

        else:
            print(f"\nStart your {self.brand} {self.model} first")

    def __str__(self):
        return f"\nYour car is a {self.year} {self.brand} {self.model} in {self.color} color."

my_car = Car("Toyota", "Blue", "Corolla", 2022)

def main():
    while True:
        print("\n1. Start\n2. Stop\n3. Check Distance\n4. Check your car model\n5. Exit")
        choice = int(input("Choose 1-5: "))

        if choice == 1:
            my_car.start()

        elif choice == 2:
            my_car.stop()

        elif choice == 3:
            my_car.drive(600)

        elif choice == 4:
            print(my_car)

        elif choice == 5:
            print(f"\nBubyeeee! Your {my_car.brand} {my_car.model}\n")
            break

        else:
            print("Please choose between 1-5")

main()