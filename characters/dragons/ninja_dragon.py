from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.4
    blocks_path = False
    is_container = False
    implemented = True  # Change to True to view in the GUI

    # END 2.4

    def action(self, colony):
        # BEGIN 2.4
        "*** YOUR CODE HERE ***"
        terminator = [t for t in self.place.terminators]
        
        for t in terminator:
                t.reduce_armor(self.damage)

