class manusia: #template
    #class variable (static)
    jumlah = 0

    def __init__(self, InputName, InputLocation, InputAge, InputHeight):
        #instance variable
        self.name = InputName
        self.location = InputLocation
        self.age = InputAge
        self.Height = InputHeight
        manusia.jumlah += 1
        print("Penambahan manusia " + InputName)

manusia1 = manusia("Homo Sapiens", "Jawa", 63, 170)
print(manusia.jumlah)
manusia2 = manusia("Erectus", "Kalimantan", 80, 190)
print(manusia.jumlah)
manusia3 = manusia("Megantropus", "Sumatra", 100, 220)
print(manusia.jumlah)

