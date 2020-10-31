class Car(object):

    def __init__(self, model, color, company, speed_limit, milage):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating...")

    def change_gear(self):
        gear = 0
        gear = int (input("enter the gear you want to change to: "))
        if gear >= 1 and gear <=6:
            print("gear changed to ", gear)
        else:
            print("Enter a number between 1 to 6")

tesla = Car("F1", "red", "tesla", 70, 10)

tesla.start()
tesla.change_gear()