from simulation import Simulation
from person import Person
import pytest, random


def setup_simulation():
    pop_size = 100000
    vacc_percentage = 0.90
    virus_name = 'Zombies'
    mortality_rate = 0.70
    basic_repro_num = 0.25
    initial_infected = 10
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected)
    return simulation

def test_create_population():
    simulation = setup_simulation()
    assert simulation.population_size == 100000
    assert len(simulation.population) == 100000
    assert len(simulation.population) == simulation.population_size
    assert simulation.vacc_percentage == 0.90
    vaccinated = 0
    not_vaccinated_and_not_infected = 0
    infected_count = 0
    for person in simulation.population:
        if person.is_vaccinated is True and person.infected is False:
            vaccinated += 1
        else:
            if person.infected is True and person.is_vaccinated is False:
                infected_count += 1
            elif person.is_vaccinated is False and person.infected is False:
                not_vaccinated_and_not_infected += 1
    assert vaccinated == 89914
    assert not_vaccinated_and_not_infected == 10076
    assert infected_count == 10
    assert simulation.total_infected == 10
    assert simulation.current_infected == 10
    assert vaccinated + not_vaccinated_and_not_infected + infected_count == 100000
    assert simulation.virus_name == 'Zombies'
    assert simulation.mortality_rate == 0.70
    assert simulation.basic_repro_num == 0.25
    assert simulation.next_person_id == 100000

def test_interaction():
    simulation = setup_simulation()
    person = simulation.population[0]
    random_person = simulation.population[2522]
    simulation.interaction(person, random_person)
    assert len(simulation.newly_infected) == 1
