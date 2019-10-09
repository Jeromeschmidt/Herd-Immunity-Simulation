from simulation import Simulation
from virus import Virus
from logger import Logger
# from logger import Logger
import unittest
import os

#UNIT TESTS
class TestLogger(unittest.TestCase):

    def test_write_metadata():
        virus_name = "HIV"
        repro_num = 0.50
        mortality_rate = 0.90
        pop_size = 100000
        vacc_percentage = 0.90
        initial_infected = 10

        virus = Virus(virus_name, repro_num, mortality_rate)
        sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)
        log = Logger(sim)
                     
        assert os.path.exists(f'simulations/{log.name}.txt')

    def test_log_interaction():
        pass
    def test_log_infection_survival():
        pass
    def test_log_time_step():
        pass
