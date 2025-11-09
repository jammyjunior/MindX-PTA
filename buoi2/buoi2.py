class pet:
    def __init__(self, petType, petHair, petAge, petWeight):
        self.petType = petType
        self.petHair = petHair
        self.petAge = petAge
        self.petWeight = petWeight
    
    def show(self):
        return f"""
        Type: {self.petType}
        Hair: {self.petHair}
        Age: {self.petAge} year(s) old
        Weight: {self.petWeight} kg
        """

network = {
    "ana" : pet("Dog", "black", 5, 10).show(),
    "john" : pet("Cat", "blonde", 2, 5).show(),
    "mark" : pet("Parrot", "colorful", 1, 3).show()
}

while True:
    name = input("Who? ").lower()
    print(network.get(name, "404 Not Found!"))
