class Myclass:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return self.first_name+' '+self.last_name
myclass=Myclass('Soleman','Hossain')
print(myclass.full_name)
myclass.full_name='New Name'