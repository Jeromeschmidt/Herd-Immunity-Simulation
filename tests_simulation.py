from simulation import Simulation
from virus import Virus
from person import Person
import unittest

#UNIT TESTS
class TestSimulation(unittest.TestCase):

    # reference for test virus and population
    # virus_name = "Ebola"
    # repro_num = 0.25
    # mortality_rate = 0.70
    # pop_size = 100000
    # vacc_percentage = 0.90
    # initial_infected = 10
    #
    # virus = Virus(virus_name, repro_num, mortality_rate)
    # sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    def test_create_population(self):
        virus_name = "Ebola"
        repro_num = 0.25
        mortality_rate = 0.70
        pop_size = 100000
        vacc_percentage = 0.90
        initial_infected = 10

        virus = Virus(virus_name, repro_num, mortality_rate)
        sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

        assert sim.population == []
        sim._create_population(initial_infected)
        assert sim.population != []

    def test_simulation_should_continue(self):
        virus_name = "Ebola"
        repro_num = 0.25
        mortality_rate = 0.70
        pop_size = 100000
        vacc_percentage = 0.90
        initial_infected = 10

        virus = Virus(virus_name, repro_num, mortality_rate)
        sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

        assert sim.pop_size != sim.total_dead, True
        sim.total_dead = sim.pop_size
        assert sim.pop_size == sim.total_dead, False
    #
    # def test_run(self):
    #     pass
    #
    def test_time_step(self):
        virus_name = "HIV"
        repro_num = 0.50
        mortality_rate = 0.90
        pop_size = 100000
        vacc_percentage = 0.90
        initial_infected = 10

        virus = Virus(virus_name, repro_num, mortality_rate)
        sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

        person1 = Person(1, False, virus)
        person2 = Person(2, False)
        sim.interaction(person1, person2)
        sim._infect_newly_infected()
        assert person1.infection is virus
        assert person2.infection is sim.virus

    #
    def test_interaction(self):
        virus_name = "Ebola"
        repro_rate = 0.99
        mortality_rate = 0.70
        pop_size = 100000
        vacc_percentage = 0.90
        initial_infected = 10

        virus = Virus(virus_name, repro_rate, mortality_rate)
        sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

        person1 = Person(1, False, virus)
        person2 = Person(2, False)

        assert person1.infection is virus
        assert person2.infection is None
        sim.interaction(person1, person2)
        sim._infect_newly_infected()
        assert person1.infection is virus
        assert person2.infection is sim.virus

    #
    def test_infect_newly_infected(self):
        virus_name = "Ebola"
        repro_num = 0.25
        mortality_rate = 0.70
        pop_size = 100000
        vacc_percentage = 0.90
        initial_infected = 10

        virus = Virus(virus_name, repro_num, mortality_rate)
        sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

        person1 = Person(1, False)
        person2 = Person(2, False)
        sim.newly_infected.append(person1)
        sim.newly_infected.append(person2)

        assert person1.infection is None
        assert person2.infection is None
        assert sim.newly_infected != []
        sim._infect_newly_infected()
        assert sim.newly_infected == []
        assert person1.infection is sim.virus
        assert person2.infection is sim.virus


if __name__ == '__main__':
    unittest.main()
