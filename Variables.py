class Computer:
    brand = 'dell'#class variable
    def __init__(self,ram,rom):
        self.ram = ram #instance variable
        self.rom = rom #instance variable
    def info(self):
        print(self.brand,self.ram,self.rom)

comp1 = Computer('16gb','1tb')
comp2 = Computer('8gb','512gb')


print(comp1.ram,comp2.ram)
comp1.ram = '64gb' #changing instance variable
print(comp1.ram,comp2.ram)

print(Computer.brand,comp1.brand,comp2.brand)
Computer.brand = 'dell-laptop'
print(Computer.brand,comp1.brand,comp2.brand)

