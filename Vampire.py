from Warrior import Warrior

class Vampire(Warrior):
    def __init__(self, name, health, attack, vampirism, sprite, x, y):
        super().__init__(name, health, attack, sprite, x, y)
        self.vampirism = vampirism

    def set_vampirism(self, vampirism):
        self.vampirism = vampirism 
    
    def get_vampirism(self):
        return self.vampirism
