class user:
    
    def __init__(self, name):
        print('я создался')
        self.username = name
        
    def sayname(self):
        print('меня зовут', self.username)

alex = user('alex')

alex.sayname()