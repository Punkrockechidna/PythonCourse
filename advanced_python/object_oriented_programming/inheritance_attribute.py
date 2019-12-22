# This can use super
# super does not need to pass self, it uses class above the current one
class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self,email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)
