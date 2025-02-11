"""#A class can have noof objects but a object has only one class
class Computer:
    #pass is used 
    def info(self):
        print("Dell 15gb 1Tb")
        
comp1 = Computer()#creation of object

comp1.info()#short way
Computer.info(comp1)#conventional way"""

class Computer:
    def info(self,brand,ram,rom):
        print(brand,ram,rom)

comp1 = Computer()
comp2 = Computer()

comp1.info('Dell','16gb','1Tb')
comp2.info('Hp','8gb','512gb')
