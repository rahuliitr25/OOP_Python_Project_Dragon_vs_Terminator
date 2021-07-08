from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    food_cost = 6
    
    
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI
    is_container = True
    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        "*** YOUR CODE HERE ***"
        if self.contained_dragon != None:
            self.contained_dragon.action(colony)
        terminators = [t for t in self.place.terminators]
        for t in terminators:
            if t != None:
                t.reduce_armor(self.damage)
            

