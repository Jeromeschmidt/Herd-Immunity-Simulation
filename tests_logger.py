from simulation import Simulation
from virus import Virus
from logger import Logger
import unittest
import os

#UNIT TESTS
class TestLogger(unittest.TestCase):
    def test__init__(self):
        self.log = Logger('test.txt')
        assert self.log.file_name == 'test.txt'

    def test_write_metadata(self):
        file_name = 'test.txt'
        assert self.log.file_name == file_name
        
    def test_log_interaction(self):
        pass
    def test_log_infection_survival(self):
        pass
    def test_log_time_step(self):
        pass
