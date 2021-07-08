from .dragon import Dragon
from utils import random_or_none
from ..fighter import Fighter

class BodyguardDragon(Dragon):
    """BodyguardDragon provides protection to other Dragons."""

    name = 'Bodyguard'
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 4
    is_container = True
    # BEGIN 3.2
    implemented = True  # Change to True to view in the GUI

    def __init__(self, armor=2):
        Dragon.__init__(self, armor)
        self.contained_dragon = None  # The Dragon hidden in this bodyguard

    def can_contain(self, other):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***" 
        if self.is_container and self.contained_dragon == None and not other.is_container:
            return True
        
        return False
       
    def contain_dragon(self, dragon):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        if self.can_contain(dragon):
            self.contained_dragon = dragon
        # END 3.2

    def action(self, colony):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        if self.contained_dragon != None:
            self.contained_dragon.action(colony)
            
        # END 3.2
