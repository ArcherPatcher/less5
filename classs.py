class Reustarant():
   def __init__(self,name,type):
      self.name=name
      self.type=type
      self.number_served=0
   def describe(self): 
    print(f"{self.name}, kitchen is a:{self.type}")
   def open_rest(self):
    print(f"{self.name} is open")
   def read_numbers(self):
    print(f"n today:{self.number_served}")
   def set_number_served(self,num):
    self.number_served=num
   def inc_num(self,num):
    self.number_served+=  num