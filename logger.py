import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name
        self.time_step_numberV = list()
        self.current_infectedV = list()
        self.died_this_time_stepV = list()
        self.total_infectedV = list()
        self.total_deadV = list()

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        with open(f"./simulations/{self.file_name}", "w") as file:
            lines = [f"{pop_size}\n", f"{vacc_percentage}\n", f"{virus_name}\n", f"{mortality_rate}\n", f"{basic_repro_num}\n"]
            file.writelines(lines)


    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        with open(f"./simulations/{self.file_name}", 'a') as file:
            if did_infect and random_person_sick != True:
                file.write(f'{person._id} infects {random_person._id}\n')
            else:
                if random_person_vacc and random_person_sick != True:
                    file.write(f"{person._id} didn't infect {random_person._id} because They're vaccinated\n")
                elif random_person_sick and random_person_vacc != True:
                    file.write(f"{person._id} didn't infect {random_person._id} because They're already sick\n")
                elif random_person_sick and random_person_vacc:
                    file.write(f"{person._id} didn't infect {random_person._id} because They're already sick and already sick\n")

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        with open(f"./simulations/{self.file_name}", "a") as file:
            if person.is_alive:
                file.write(f'{person._id} survived infection')
            else:
                file.write(f'{person._id} died from infection')

    def log_time_step(self, time_step_number, current_infected, died_this_time_step, total_infected, total_dead):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        self.time_step_numberV.append(time_step_number)
        self.current_infectedV.append(current_infected)
        self.died_this_time_stepV.append(died_this_time_step)
        self.total_infectedV.append(total_infected)
        self.total_deadV.append(total_dead)

        with open(f"./simulations/{self.file_name}", 'a') as file:
            lines = [f"Time step {time_step_number} ended, beginning {time_step_number + 1}\n", f' People Infected: {current_infected}', f' People that died this time step far: {died_this_time_step}', f' Total Infected: {total_infected}', f' Total Dead {total_dead}']
            file.writelines(lines)

    def Visualizer(self):
        fig, ax = plt.subplots()
        ax.set(xlabel='time_step_number', ylabel='Statistics', title='Disease Timeline')
        plt.plot(self.time_step_numberV, self.current_infectedV, label='Current Infected')
        plt.plot(self.time_step_numberV, self.died_this_time_stepV, '--', label='Died This Time_Step')
        plt.plot(self.time_step_numberV, self.total_infectedV, '-.', label='Total Infected')
        plt.plot(self.time_step_numberV, self.total_deadV, ':', label='Total_Dead')
        plt.legend(loc='upper left')
        plt.show()
