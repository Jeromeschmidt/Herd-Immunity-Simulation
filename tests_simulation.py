from simulation import Simulation
from virus import Virus
import unittest

#UNIT TESTS
class TestSimulation(unittest.TestCase):

    virus_name = "Ebola"
    repro_num = 0.25
    mortality_rate = 0.70
    pop_size = 100000
    vacc_percentage = 0.90
    initial_infected = 10

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    def test_create_population(self):
        assert sim.population == None
        simulation._create_population(initial_infected)
        assert sim.population != None

    def _simulation_should_continue(self):
        pass

    def run(self):
        pass

    def time_step(self):
        pass

    def interaction(self):
        pass

    def _infect_newly_infected(test):
        pass

if __name__ == '__main__':
    unittest.main()
