#############################---Exercise 3 Start---####################################

'''
    color: string
    model: string
    year: int
    maxSpeed: float (Mi/Hr)
    mileage: float (Mi/gallon)
    currSpeed: float (Mi/Hr)
'''
class Car:
    def __init__(self, color, model, year, maxSpeed, mileage, currSpeed):
        self.color = color
        self.model = model
        self.year = year
        self.maxSpeed = maxSpeed
        self.mileage = mileage
        self.currSpeed = currSpeed

    # x = Miles/hour to increase the current speed
    def accelerate(self, x):

        originalSpeed = self.currSpeed

        if self.currSpeed + x > self.maxSpeed:
            self.currSpeed = self.maxSpeed
        else:
            self.currSpeed += x

        newSpeed = self.currSpeed

        if originalSpeed != newSpeed:
            print("Current speed is now: " + str(self.currSpeed))

    # Decrease current speed by 20%
    def brake(self):

        originalSpeed = self.currSpeed

        self.currSpeed = self.currSpeed * .80
        if self.currSpeed < 1:
            self.currSpeed = 0

        newSpeed = self.currSpeed

        if originalSpeed != newSpeed:
            print("Current speed is now: " + str(self.currSpeed))


''' Initialize my favorite car '''
stingray = Car('Pearl', "Corvette Stringray", 2021, 194, 15, 0)

''' 
    Begin “driving” at 0 mph. Increase the speed by increments of 10 until 
    the maximum speed is reached (but do not exceed the maximum speed).
'''
while stingray.currSpeed != stingray.maxSpeed:
    stingray.accelerate(10)

while stingray.currSpeed != 0:
    stingray.brake()


#######################################################################################
