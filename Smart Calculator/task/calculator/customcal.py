from collections import defaultdict
import re
import sys


class SmartCalculator:
    dict_saved_variables = defaultdict(str)

    def __init__(self, entry: str):
        self.entry = entry
        self.running()

    def running(self):
        pattern = re.compile(r"[ ]*([A-Za-z]+)[ ]*=[ ]*([A-Za-z\d*]+|\d+)")
        result = pattern.search(self.entry)
        if self.entry == "/help":
            print("The program calculates the sum of numbers")
        elif self.entry == "":
            pass
        elif self.entry == "/exit":
            print("Bye!")
            sys.exit()
        elif self.entry.startswith("/"):
            print("Unknown command")
        elif self.entry.count("=") == 1 and result:
            self.saving_value(result)
        else:
            self.operation()

    def operation(self):
        self.preparing_variables()
        try:
            print(eval(self.entry))
        except SyntaxError:
            print("Invalid expression")
        except NameError:
            print("Unknown variable")

    def preparing_variables(self):
        for key, value in SmartCalculator.dict_saved_variables.items():
            try:
                self.entry = re.sub(key, value, self.entry)
            except KeyError:
                continue
        if "/" in self.entry:
            self.entry = re.sub("/", "//", self.entry)

    @staticmethod
    def saving_value(result):
        variable, assigment = result.groups()
        if assigment.isdigit():
            SmartCalculator.dict_saved_variables[variable] = assigment
        elif not assigment.isdigit() and assigment in SmartCalculator.dict_saved_variables:
            SmartCalculator.dict_saved_variables[variable] = SmartCalculator.dict_saved_variables[assigment]
        elif not assigment.isdigit() and assigment not in SmartCalculator.dict_saved_variables:
            print("Invalid assigment")
        else:
            print("Unknown variable")



