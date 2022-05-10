
from collections import deque

'''
    Class that holds the business logic, performs the data analysis etc...
'''


class AnalyseStream:

    def __init__(self, data: deque) -> None:
        self.data = data

    def get_max_number(self) -> int:
        try:
            return max(self.data)
        except Exception as e:
            print(str(e), str(self.data))

    def get_min_number(self) -> int:
        try:
            return min(self.data)
        except Exception as e:
            print(str(e), str(self.data))

    def get_first_number(self) -> int:
        try:
            return self.data[-1]
        except Exception as e:
            print(str(e), str(self.data))

    def get_last_number(self) -> int:
        try:
            return self.data[0]
        except Exception as e:
            print(str(e), str(self.data))

    def isPrime(self, data: int) -> bool:
        if data < 1:
            return False
        if data in (2, 3):
            return True
        else:
            for i in range(2, int(data/2)+1):
                if (data % i) == 0:
                    return False
                else:
                    return True

    def get_nbre_of_prime_nbre(self) -> int:
        counter = 0

        try:
            for i in self.data:
                if self.isPrime(i):
                    counter += 1
            return counter
        except Exception as e:
            print(str(e), str(self.data))

    def get_nbre_of_even_nbre(self) -> int:
        counter = 0
        try:
            for i in self.data:
                if i % 2 == 0:
                    counter += 1
            return counter
        except Exception as e:
            print(str(e), str(self.data))

    def get_nbre_of_odd_nbre(self) -> int:
        counter = 0
        try:
            for i in self.data:
                if not (i % 2 == 0):
                    counter += 1
            return counter
        except Exception as e:
            print(str(e), str(self.data))


'''
    Class to model the output in order to show structured data to the users
'''


class GenerateOuput:

    def __init__(self, stream_of_data) -> None:
        self.data = stream_of_data
        self.analyse_data = AnalyseStream(self.data)

    '''
        Method that collects the data processed and analysed
        structures the data into a Dict
    '''

    def structure_data(self) -> dict:
        structure = {
            "Max_number": self.analyse_data.get_max_number(),
            "Min_number": self.analyse_data.get_min_number(),
            "First_number": self.analyse_data.get_first_number(),
            "Last_number": self.analyse_data.get_last_number(),
            "Number_of_prime_numbers": self.analyse_data.get_nbre_of_prime_nbre(),
            "Number_of_even_numbers": self.analyse_data.get_nbre_of_even_nbre(),
            "Number_of_odd_numbers": self.analyse_data.get_nbre_of_odd_nbre()
        }
        return structure

    '''
        Prints the data
    '''

    def print_data(self, structured_data: dict):
        # Printing the data processed every minute
        for k, v in structured_data.items():
            print(str(k) + ": " + str(v))
        print()
        print('------------------------')
        print()
