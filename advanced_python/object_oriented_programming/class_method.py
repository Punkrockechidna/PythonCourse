# When to use what https://www.makeuseof.com/tag/python-instance-static-class-methods/

class PlayerCharacter:
    # class object attribute (static not dynamic) doesn't change
    membership = True

    # constructor method/instantiate/init
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            # self allows you to have a reference to something that hasn't been created yet IE player1
            self.name = name  # attribute/property
            self.age = age

    def shout(self):
        print(f'My name is {self.name}!')

    @classmethod  # not used too often
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod  # also not used often, doesn't care about class attributes(class state) (NO access to cls)
    def adding_things2(num1, num2):
        return num1 + num2


# player1 = PlayerCharacter('Cindy', 40)
player3 = PlayerCharacter.adding_things(2, 3)
print(player3)
print(player3.name)
print(player3.age)
