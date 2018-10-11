import random, sys
random.seed(42)
from person import Person
from logger import Logger

class Simulation(object):
    '''
    Main class that will run the herd immunity simulation program.  Expects initialization
    parameters passed as command line arguments when file is run.
    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    _____Attributes______
    logger: Logger object.  The helper object that will be responsible for writing
    all logs to the simulation.
    '''

    def __init__(self, population_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.vacc_percentage = vacc_percentage
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.total_dead = 0
        self.total_healed = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.newly_infected = []
        self._create_population(initial_infected)
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus_name, population_size, vacc_percentage, initial_infected)
        # TODO: Create a Logger object and bind it to self.logger.  You should use this
        # logger object to log all events of any importance during the simulation.  Don't forget
        # to call these logger methods in the corresponding parts of the simulation!
        self.logger = Logger(self.file_name)
        self.logger.write_metadata(population_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num)



    def _create_population(self, initial_infected):
        self.population = []
        infected_count = 0
        while len(self.population) != self.population_size:
            if infected_count !=  initial_infected:
                person = Person(self.next_person_id, False, True)
                self.population.append(person)
                self.next_person_id += 1
                infected_count += 1
            else:
                just_your_luck = random.uniform(0,1)
                if just_your_luck < self.vacc_percentage:
                    person = Person(self.next_person_id, True)
                    self.population.append(person)
                    self.next_person_id += 1
                else:
                    person = Person(self.next_person_id, False)
                    self.population.append(person)
                    self.next_person_id += 1
        self.current_infected += infected_count
        self.total_infected += infected_count
        return self.population

    def _simulation_should_continue(self):
        if self.population_size == 0 or self.current_infected == 0:
            return False
        else:
            return True

    def run(self):
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
            should_continue = self._simulation_should_continue()
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        interactions = 0
        total_interactions = 0
        for person in self.population:
            if person.infected is True:
                while interactions <= 100:
                    random_person = random.choice(self.population)
                    while random_person.is_alive is False:
                        assert random_person.is_alive == False
                        random_person = random.choice(self.population)
                    else:
                        assert random_person.is_alive == True
                        self.interaction(person, random_person)
                        interactions += 1
                        total_interactions += 1
                else:
                    did_survive = person.did_survive_infection(self.mortality_rate)
                    if person.is_alive is True:
                        assert person.is_alive == True
                        assert person.is_vaccinated == True
                        assert person.infected == False
                        self.current_infected -= 1
                        self.total_healed += 1
                        interactions = 0

                    else:
                        assert person.is_alive == False
                        assert person.infected == False
                        self.total_dead += 1
                        self.population_size -= 1
                        self.current_infected -= 1
                        interactions = 0
        self.logger.log_infection_survival(person, did_survive)
        self._infect_newly_infected()

    def interaction(self, person, random_person): # 9/10 almost completed
        if random_person.is_vaccinated is True:
            assert random_person.is_vaccinated == True
            pass
        elif random_person.infected is True:
            assert random_person.infected == True
            pass
        else:
            are_you_lucky = random.random()
            if are_you_lucky > self.basic_repro_num:
                self.logger.log_interaction(person, random_person, False, True)
            else:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(person, random_person, True, False)
        # TODO: Remember to call self.logger.log_interaction() during this method!

    def _infect_newly_infected(self):
        for person in self.population:
            if person._id in self.newly_infected:
                person.infected = True
                self.total_infected += 1
                self.current_infected += 1
        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected)
    simulation.run()

    print('The total amount dead: {}'.format(simulation.total_dead))
    print('Total population: {}'.format(simulation.population_size))
    print('The total amount healed: {}'.format(simulation.total_healed))
    print('Total amount of people infected: {}'.format(simulation.total_infected))
