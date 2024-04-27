class SPOM:
    def __init__(self, amount_of_electrolyzers, num_of_dupes = None):
        self.amount_of_electrolyzers = amount_of_electrolyzers
        self.num_of_dupes = num_of_dupes
    def rate_of_water(self) -> " grams / sec of water":
        return self.amount_of_electrolyzers * 1000
    def oxygen_production(self) -> " grams / sec of oxygen":
        return 888 * self.amount_of_electrolyzers
    def hydrogen_production(self) -> " grams / sec of hydrogen":
        return 112 * self.amount_of_electrolyzers
    def oxygen_pump_amount(self) ->  " gas pumps":
        return self.oxygen_production() / 500
    def hydrogen_pump_amount(self) ->  " gas pumps":
        return self.hydrogen_production() / 500
    def amount_of_dupes(self) -> " dupes":
        return self.oxygen_production() / 100
    def amount_of_dupes_reverse(self):
        if self.num_of_dupes == None:
            return "you haven't enterned a desired number of dupes."
        else:
            return f"you will need {(100 * self.num_of_dupes) / 888} electrolyzers to sustain {self.num_of_dupes} dupes."
    def hydrogen_generator_amount(self) -> " hydrogen generators":
        return self.hydrogen_production() / 100
    def min_amount_of_generators(self) -> " hydrogen generators":
        return self.energy_demand() / 800
    def energy_production(self) -> " watts":
        return self.hydrogen_generator_amount() * 800
    def energy_demand(self) -> " watts":
        return (self.amount_of_electrolyzers * 120) + (int(self.oxygen_pump_amount() + self.hydrogen_pump_amount()) * 240)
    def excess_energy(self) -> " watts":
        return self.energy_production() - self.energy_demand()
    def dupe_lavatory_water_production(self) -> " grams / sec of water":
        return (6700 / 600) * self.num_of_dupes
    def dupe_lavatory_water_production_reverse(self) -> " dupes":
        return self.rate_of_water() / (6700 / 600)
    def water_to_oxygen(self) -> " grams / sec of oxygen":
        return 888 * (self.dupe_lavatory_water_production() / 1000)
    def water_deficiency(self) -> " grams / sec of water":
        return SPOM((100 * self.num_of_dupes) / 888).rate_of_water() - self.dupe_lavatory_water_production()

spom_machine = SPOM(amount_of_electrolyzers = 1, num_of_dupes = 90)
print(f"you need {str(spom_machine.rate_of_water()) + spom_machine.rate_of_water.__annotations__['return']}.")
print(f"you will produce {str(spom_machine.oxygen_production()) + spom_machine.oxygen_production.__annotations__['return']} and {str(spom_machine.hydrogen_production()) + spom_machine.hydrogen_production.__annotations__['return']}.")
print(f"you will need {str(spom_machine.oxygen_pump_amount()) + spom_machine.oxygen_pump_amount.__annotations__['return']} for the oxygen and {str(spom_machine.hydrogen_pump_amount()) + spom_machine.hydrogen_pump_amount.__annotations__['return']} for the hydrogen.")
print(f"you can sustain {str(spom_machine.amount_of_dupes()) + spom_machine.amount_of_dupes.__annotations__['return']} with {spom_machine.amount_of_electrolyzers} electrolyzers.")
print(f"you can power {str(spom_machine.hydrogen_generator_amount()) + spom_machine.hydrogen_generator_amount.__annotations__['return']} with a minimum amount of {str(spom_machine.min_amount_of_generators()) + spom_machine.min_amount_of_generators.__annotations__['return']}.")
print(f"you will produce {str(spom_machine.energy_production()) + spom_machine.energy_production.__annotations__['return']} , {str(spom_machine.energy_demand()) + spom_machine.energy_demand.__annotations__['return']} of which will be consumed by the SPOM , leaving you with {str(spom_machine.excess_energy()) + spom_machine.excess_energy.__annotations__['return']}.")
print(spom_machine.amount_of_dupes_reverse())
print(f"you will produce {str(spom_machine.dupe_lavatory_water_production()) + spom_machine.dupe_lavatory_water_production.__annotations__['return']} with {spom_machine.num_of_dupes} dupes.")
print(f"you will produce {str(spom_machine.water_to_oxygen()) + spom_machine.water_to_oxygen.__annotations__['return']} with {spom_machine.num_of_dupes} dupes.")
print(f"you will need {str(spom_machine.dupe_lavatory_water_production_reverse()) + spom_machine.dupe_lavatory_water_production_reverse.__annotations__['return']} to sustain {spom_machine.amount_of_electrolyzers} electrolyzers.")
print(f"the deficiency of water is {str(spom_machine.water_deficiency()) + spom_machine.water_deficiency.__annotations__['return']}.")
print("")

class FOOD:
    def __init__(self,type_of_food,num_of_dupes = None,amount_of_Sleet_Wheat_Grain = 0, amount_of_Pincha_Peppernut = 0, num_of_Pincha_Pepperplant = 0, num_of_Sleet_Wheat = 0):
        self.num_of_Sleet_Wheat = num_of_Sleet_Wheat
        self.num_of_Pincha_Pepperplant = num_of_Pincha_Pepperplant
        self.num_of_dupes = num_of_dupes
        self.type_of_food = type_of_food
        self.amount_of_Sleet_Wheat_Grain = amount_of_Sleet_Wheat_Grain
        self.amount_of_Pincha_Peppernut = amount_of_Pincha_Peppernut
        self.function_allocation = {"Pepper Bread":(self.Pepper_Bread, self.Pepper_Bread_calories, self.rate_of_Pincha_Peppernut, self.rate_of_Sleet_Wheat_Grain, self.rate_of_Pepper_Bread, self.amount_of_dupes_Pepper_Bread, self.amount_of_Pepper_Bread_plants_reverse)}
    def Pepper_Bread(self) -> " Pepper Bread":
        return min(self.amount_of_Sleet_Wheat_Grain / 10, self.amount_of_Pincha_Peppernut)
    def Pepper_Bread_calories(self, num) -> " kcal":
        return num * 4000
    def rate_of_Pincha_Peppernut(self) -> " KG of Pincha Peppernut / cycle":
        return (4 / 8) * self.num_of_Pincha_Pepperplant
    def rate_of_Sleet_Wheat_Grain(self) -> " KG of Sleet Wheat Grain / cycle":
        return self.num_of_Sleet_Wheat
    def rate_of_Pepper_Bread(self) -> " KG of Pepper Bread / cycle":
        return min(self.rate_of_Sleet_Wheat_Grain() / 10, self.rate_of_Pincha_Peppernut())
    def amount_of_dupes_Pepper_Bread(self) -> " dupes":
        return self.Pepper_Bread_calories(self.rate_of_Pepper_Bread()) / 1000
    def amount_of_Pepper_Bread_plants_reverse(self) -> (" Pincha Pepperplant"," Sleet Wheat"):
        return ((self.num_of_dupes*1000*2/4000),(self.num_of_dupes*1000*2*10/4000))
    def getter(self):
        return self.function_allocation[self.type_of_food]
def f(x):return x*10
x = 10
farm = FOOD("Pepper Bread",num_of_dupes=4, num_of_Pincha_Pepperplant=x, num_of_Sleet_Wheat=f(x))
print(f"you're producing {str(farm.getter()[2]()) + farm.getter()[2].__annotations__['return']}")
print(f"you're producing {str(farm.rate_of_Sleet_Wheat_Grain()) + farm.rate_of_Sleet_Wheat_Grain.__annotations__['return']}")
print(f"you're producing {str(farm.rate_of_Pepper_Bread()) + farm.rate_of_Pepper_Bread.__annotations__['return']} or {str(farm.Pepper_Bread_calories(farm.rate_of_Pepper_Bread())) + farm.Pepper_Bread_calories.__annotations__['return']} / cycle")
print(f"you can sustain {str(farm.amount_of_dupes_Pepper_Bread()) + farm.amount_of_dupes_Pepper_Bread.__annotations__['return']}")
print(f"you need to plant {str(farm.amount_of_Pepper_Bread_plants_reverse()[0])+farm.amount_of_Pepper_Bread_plants_reverse.__annotations__['return'][0]} and {str(farm.amount_of_Pepper_Bread_plants_reverse()[1])+farm.amount_of_Pepper_Bread_plants_reverse.__annotations__['return'][1]} to sustain {farm.num_of_dupes} dupes with {farm.type_of_food}")
print("")

class cooler:
    def __init__(self, temperature_type, desired_temperature):
        self.temperature_type = temperature_type
        self.desired_temperature = desired_temperature
        self.myDict = {"before cooling": self.sensor_before_cooling, "after cooling": self.sensor_after_cooling}
    def sensor_after_cooling(self):
        return self.desired_temperature + 7
    def sensor_before_cooling(self):
        return self.desired_temperature - 7
    def sensor_temperature(self) -> " °C":
        return self.myDict[self.temperature_type]()
    
thermo_aquatuner = cooler("after cooling", 20)
print(f"set your sensor to above {str(thermo_aquatuner.sensor_temperature()) + thermo_aquatuner.sensor_temperature.__annotations__['return']}")