from simulation import Simulation
from virus import Virus
from person import Person
from logger import Logger
import unittest
import os

#UNIT TESTS
class TestLogger(unittest.TestCase):
    def test__init__(self):
        log = Logger('test.txt')
        assert log.file_name == 'test.txt'

    def test_write_metadata(self):
        log = Logger('test.txt')
        open('simulations/test.txt', 'w').close()
        assert os.path.getsize('simulations/test.txt') == 0
        log.write_metadata(10, 1, "virus_name", 0.1, 0.1)
        assert os.path.getsize('simulations/test.txt') != 0

    def test_log_interaction(self):
        log = Logger('test.txt')
        virus = Virus("test", 0.1, 0.1)
        person = Person(1, False, virus)
        random_person = Person(2, False)
        temp = os.path.getsize('simulations/test.txt')
        log.log_interaction(person, random_person, random_person_sick=False, random_person_vacc=False, did_infect=True)
        assert os.path.getsize('simulations/test.txt') > temp

    def test_log_infection_survival(self):
        log = Logger('test.txt')
        virus = Virus("test", 0.1, 0.1)
        person = Person(1, False, virus)
        temp = os.path.getsize('simulations/test.txt')
        log.log_infection_survival(person, True)
        assert os.path.getsize('simulations/test.txt') > temp

    def test_log_time_step(self):
        log = Logger('test.txt')
        temp = os.path.getsize('simulations/test.txt')
        log.log_time_step(1, 5, 20, 50, 100)
        assert os.path.getsize('simulations/test.txt') > temp

if __name__ == '__main__':
    unittest.main()
