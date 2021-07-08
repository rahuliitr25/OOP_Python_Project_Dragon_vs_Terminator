from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    min_range = None
    max_range = None

    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        
        minRange = self.min_range
        maxRange = self.max_range
        
        curPlace = self.place
        places = []
        
        while curPlace != skynet:
            places.append(random_or_none(curPlace.terminators))
            curPlace = curPlace.entrance
        
        no_of_places = len(places)
        
        
        if maxRange != None and minRange  == None:
            for i in range(min(maxRange+1,no_of_places)):
                if places[i] != None:
                    return places[i]
        
        if minRange != None and maxRange == None:
            for i in range(minRange, no_of_places):
                if places[i] != None:
                    return places[i]
        
        if minRange != None and minRange == maxRange and minRange < no_of_places:
            return places[minRange]
            
        
        if minRange == None and maxRange == None:
            for i in places:
                if i != None:
                    return i
            
        return None
        
        # END 1.3 and 2.1

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
