import random

class Person(object):
    '''
    Person objects will populate the simulation.
    '''

    def __init__(self, _id, is_vaccinated, infected=False):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected

    def did_survive_infection(self, mortality_rate):
        if self.infected:
            assert self.infected == True
            but_did_you_die = random.random()
            if but_did_you_die <= mortality_rate:
                assert self.is_vaccinated == False
                self.is_alive = False
                assert self.is_alive == False
                self.infected = False
                assert self.infected == False
                return False
            else:
                self.is_vaccinated = True
                self.infected = False
                return True
