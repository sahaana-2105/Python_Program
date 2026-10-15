


#oops-Object oriented programming language or system
#class Object Inheritance Polymorphism Encapsulation Abstraction Interface
# class studenttwo:
#     name="unknown"
#     mark=0
#     def display (self):
#         print(self.name," ",self.mark)

# class studentone:
#     name="naveen"
#     age=20
#     dept="cse"
#     def marks(self):
#         print("Maths:90, English:78")

# class studentthree:
#     name="Unknown"
#     mark=0
#     def _init_(self,name,mark0):
#         self.name=name
#         self.mark=mark

#     # def setdetails(self,name,mark):
#     #     self.name=name
#     #     self.mark=mark
#     def printdetails(self):
#         print(self.name," ",self.mark)  


# s1=studentone()
# print(s1.name)
# print(s1.age)
# s1.marks()

# s2=studenttwo()
# s2.name="aravindh"
# S2.marks=345
# s2.display()
# s3=studenttwo()
# s3.name="dharshan"
# s3.mark=456
# s3.display()

# s4=studentthree("Kumar",34)
# #s4.setdetails("jagan",500)
# s4.printdetails()


# #single inheritance ->one parent class one child class
# class Device:
#     def power_on(self):
#         print("Device switched on")
# class Phone(Device):
#     def call(self):
#         print("Making a phone call")
# samsung=Phone()
# samsung.power_on()
# samsung.call()
# print()
# #multilevel inheritance->Grandparent->Parent->Son
# class Device:
#     def power_on(self):
#         print("Device switched on")
# class Computer(Device):
#     def run_program(self):
#         print("Running a Python program")
# class Laptop(Computer):
#     def charge(self):
#         print("Laptop battery charging")
# asus=Laptop()
# asus.power_on()
# asus.run_program()
# asus.charge()
# print()
# #Multiple Inheritance one child class multiple parent
# class Camera:
#     def take_photo(self):
#         print("Taking a photo")
# class MusicPlayer:
#     def play_music(self):
#         print("Playing music")
# class SmartPhone(Camera,MusicPlayer):
#     def call(self):
#         print("Making a phone call")
# mi=SmartPhone()
# mi.call()
# mi.take_photo()
# mi.play_music()

#hierarchial inheritance - one parent class multiple child class
# class Device:
#     def power_on(self):
#         print("Device Switched On")
# class Phone(Device):
#     def call(self):
#         print("Making a phone call")
# class Computer(Device):
#     def run_program(self):
#         print("Running a Python Program")
# samsung=Phone()
# samsung.call()
# samsung.power_on()
# hp=Computer()
# hp.power_on()
# hp.run_program()
#Hybrid Inheritance  - more than one inheritance in single program
#Polymorphism
#method overriding -method overriding means redefining a parent class method child class with the same name&parameters to provide diff behaviour
# class Phone:
#     def camera(self):
#         print("Taking a normal photo")
# class smartphone(Phone):
#     def camera(self):
#         print("Taking a portrait photo")
# samsung=smartphone()
# samsung.camera()
# nokia=Phone()
# nokia.camera()
# #Encapsulation
# class bank:
#     _amount=800
#     def printamount(self):
#         return self._amount
# hdfc=bank()
# print(hdfc.printamount())
# #Abstraction -hiding the internal details and showing only essential features
# from abc import ABC,abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(Payment):
#     def pay(self):
#         print("Payment done using upi")
# class phonepe(Payment):
#     def pay(self):
#         print("Payment done using phonepe")
# payment=UPI()
# payment.pay()
# payment=phonepe()
# payment.pay()

