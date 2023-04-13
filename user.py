class User():
    def __init__(self,name,type):
         self.name=name
         self.first_name=[]
         self.type=type
         self.date_birth=[]
         self.rank=0
    def discribe_user(self):
      print(f" user {self.name}, type {self.type}")