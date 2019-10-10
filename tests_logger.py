from simulation import Simulation
from virus import Virus
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
        pass
    def test_log_infection_survival(self):
        pass
    def test_log_time_step(self):
        pass

if __name__ == '__main__':
    unittest.main()
