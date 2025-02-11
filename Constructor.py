"""class Computer:
    def __init__(self):
        print("In Computer class")

comp1 = Computer()
comp2 = Computer()"""


class Computer:
    def __init__(self,brand,ram,rom):
       self.brand = brand
       self.ram = ram
       self.rom = rom

    def info(self):
        print(self.brand,self.ram,self.rom)

comp1 = Computer('Dell','16gb','1Tb')
comp2 = Computer('Hp','8gb','512gb')
comp1.brand = 'lenovo'

comp1.info()
comp2.info()

