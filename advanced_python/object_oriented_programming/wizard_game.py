# oop
# Classes should be singular

class PlayerCharacter:
    # class object attribute (static not dynamic) doesn't change
    membership = True

    # constructor method/instantiate/init
    def __init__(self, name,age):
        if (PlayerCharacter.membership):
            # self allows you to have a reference to something that hasn't been created yet IE player1
            self.name = name  # attribute/property
            self.age = age

    def shout(self):
        print(f'My name is {self.name}!')


player1 = PlayerCharacter('Cindy', 40)

print(player1.shout())

# shows blueprint
# help(player1)
