from Creature import Creature
from Equipment import Equipment

class Hero(Creature):
    """The hero of the game.
        Is a creature. Has an inventory of elements. """

    def __init__(self, name="Hero", hp=10, abbrv="@", strength=2):
        Creature.__init__(self, name, hp, abbrv, strength)
        self._inventory = []
        self.level: int = 0
        self.xp_cap: int = 10
        self.xp: int = 0
        
    def description(self):
        """Description of the hero"""
        return Creature.description(self) +"armure:"+ str(self.armure)+ str(self._inventory) + " exp:%s/%s" % (self.xp, self.xp_cap)

    def fullDescription(self):
        """Complete description of the hero"""
        res = ''
        for e in self.__dict__:
            if e[0] != '_':
                res += '> ' + e + ' : ' + str(self.__dict__[e]) + '\n'
        res += '> INVENTORY : ' + str([x.name for x in self._inventory])
        return res

    def checkEquipment(self, o):
        """Check if o is an Equipment."""
        if not isinstance(o, Equipment):
            raise TypeError('Not a Equipment')

    def take(self, elem):
        """The hero takes adds the equipment to its inventory"""
        self.checkEquipment(elem)
        self._inventory.append(elem)

    def use(self, elem):
        """Use a piece of equipment"""
        if elem is None:
            return
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        if elem.use(self):
            self._inventory.remove(elem)
    
    def earn_xp(self, xp_amount):
        self.xp += xp_amount
        while self.xp >= self.xp_cap:
            self.xp -= self.xp_cap
            self.level_up()
    
    def level_up(self):
        if self.level % 2 == 0:
            self.max_hp += 2
            self.strength += 1
        else:
            self.max_hp += 3
        self.level += 1
        self.hp = self.max_hp
        self.xp_cap += 10 + 5*self.level

    def meet(self, other):
        self.hp -= other.strength
        theGame().addMessage("The " + other.name + " hits the " + self.description())
        if self.hp > 0:
            return False
        return True
