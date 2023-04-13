from user import User as U
class Admin(U):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.priveleges=['ban','delete']
    def show_priveleges(self):
     print(f"{self.priveleges}")
Anton=Admin('Anton_228','admin')
Anton.show_priveleges()