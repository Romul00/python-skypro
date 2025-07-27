class user:
    
    age = 24

    def __init__(self, name):
        print('я создался')
        self.username = name
        
    def sayname(self):
        print('меня зовут', self.username)

    def sayage(self):
        print(self.age)

alex = user('alex')
daun = user ('daun')

alex.sayname()
alex.sayage()
daun.sayname()