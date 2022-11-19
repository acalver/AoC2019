import pandas as pd

modules = pd.read_csv('Day1.csv', header = None)
modules = list(modules[0])

fuel = [(module // 3) - 2 for module in modules]
sum(fuel)

########################################
#Part 2

def recursive_fuel(num):
    
    if num // 3 - 2 <= 0:
        return 0
    
    else:
        new_num = (num // 3) - 2
        return new_num + recursive_fuel(new_num)

fuels_fuel = [recursive_fuel(module) for module in modules]
sum(fuels_fuel)
