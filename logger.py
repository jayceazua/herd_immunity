class Logger(object):
    '''
    Utility class responsible for logging all interactions of note during the
    simulation.
    '''

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = None

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        # TODO: Finish this method.  The simulation class should use this method
        # immediately upon creation, to log the specific parameters of the simulation
        # as the first line of the file.  This line of metadata should be tab-delimited
        # (each item separated by a '\t' character).
        # NOTE: Since this is the first method called, it will create the text file
        # that we will store all logs in.  Be sure to use 'w' mode when you open the file.
        # For all other methods, we'll want to use the 'a' mode to append our new log to the end,
        # since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        # basic_repro_num):
        # - Writes the first line of a logfile, which will contain metadata on the
        #     parameters for the simulation.
        file = open(self.file_name, 'w')
        file.write("population size:{}\nvaccine percentage:{}\nvirus name:{}\nmortality rate:{}\nbasic reproduction number:{}\n".format(str(pop_size), str(vacc_percentage), str(virus_name), str(mortality_rate), str(basic_repro_num)))
        file.close()

    def log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
        # TODO: Finish this method.  The Simulation object should use this method to
        # log every interaction a sick individual has during each time step.  This method
        # should accomplish this by using the information from person1 (the infected person),
        # person2 (the person randomly chosen for the interaction), and the optional
        # keyword arguments passed into the method.  See documentation for more info
        # on the format of the logs that this method should write.
        # NOTE:  You'll need to think
        # about how the booleans passed (or not passed) represent
        # all the possible edge cases!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        # - Expects person1 and person2 as person objects.
        # - Expects did_infect, person2_vacc, and person2_sick as Booleans, if passed.
        # - Between the values passed with did_infect, person2_vacc, and person2_sick, this method
        #     should be able to determine exactly what happened in the interaction and create a String
        #     saying so.
        # - The format of the log should be "{person1.ID} infects {person2.ID}", or, for other edge
        #     cases, "{person1.ID} didn't infect {person2.ID} because {'vaccinated' or 'already sick'}"
        # - Appends the interaction to logfile.
        file = open(self.file_name, 'a')
        if did_infect == True:
            file.write("\n{} infects {}\n".format(person1._id, person2._id))
        elif did_infect == False:
            file.write("\n{} didn't infect {} because is already vaccinated or already sick.\n".format(person1._id, person2._id))
        file.close()

    def log_infection_survival(self, person, did_die_from_infection):
        # TODO: Finish this method.  The Simulation object should use this method to log
        # the results of every call of a Person object's .resolve_infection() method.
        # If the person survives, did_die_from_infection should be False.  Otherwise,
        # did_die_from_infection should be True.  See the documentation for more details
        # on the format of the log.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

        # - Expects person as Person object.
        # - Expects bool for did_die_from_infection, with True denoting they died from
        #     their infection and False denoting they survived and became immune.
        # - The format of the log should be "{person.ID} died from infection" or
        #     "{person.ID} survived infection."
        # - Appends the results of the infection to the logfile.
        file = open(self.file_name, 'a')
        if did_die_from_infection == False:
            file.write("{} survived infection\n".format(person._id))
        else:
            file.write("{} died from infection\n".format(person._id))


    def log_time_step(self, time_step_number):
        # TODO: Finish this method.  This method should log when a time step ends, and a
        # new one begins.  See the documentation for more information on the format of the log.
        # NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time
        # step, it also logs a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.  You may want to create a helper class
        # to compute these statistics for you, as a Logger's job is just to write logs!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

        # - Expects time_step_number as an Int.
        # - This method should write a log telling us when one time step ends, and
        #     the next time step begins.  The format of this log should be:
        #         "Time step {time_step_number} ended, beginning {time_step_number + 1}..."
        # - STRETCH CHALLENGE DETAILS:
        #     - If you choose to extend this method, the format of the summary statistics logged
        #         are up to you.  At minimum, it should contain:
        #             - The number of people that were infected during this specific time step.
        #             - The number of people that died on this specific time step.
        #             - The total number of people infected in the population, including the newly
        #                 infected
        #             - The total number of dead, including those that died during this time step.
        file = open(self.file_name, 'a')
        new_time_step_counter = time_step_number + 1
        file.write("Time step {} ended, beginning time step {}\n\n".format(time_step_number, new_time_step_counter))
        file.close()
