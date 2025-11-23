class HocSinh:
    def __init__(self, name, address, height, weight, grade):
        self.name = name
        self.address = address
        self.height = height
        self.weight = weight
        self.grade = grade

    def changeAddress(self, newAddress):
        self.address = newAddress
    
    def changeHeightAndWeight(self, newHeight, newWeight):
        self.height = newHeight
        self.weight = newWeight

    def info(self):
        return f"""
        Ten = {self.name}
        Dia chi: {self.address}
        Chieu cao: {self.height}
        Can nang: {self.weight}
        Trinh do: {self.grade}
        """

NguyenVanA = HocSinh("Nguyen Van A", "1st, ThisStreet", 170, 60, 10)
NguyenVanA.changeAddress("1st, ThatStreet")
NguyenVanA.changeHeightAndWeight(165, 55)
print(NguyenVanA.info())