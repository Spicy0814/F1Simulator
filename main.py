import random
import time
import sys

year = 2021
gp_total_2021 = 21
gp_current = 15
rank = 0
lap = 1

test = ""

class team:
    def __init__(self, team, color, power, budget_year):
        self.team = team
        self.color = color
        self.power = power
        self.budget_year = budget_year

mercedes = team("Mercedes","Turquoise", 95, 145000000)
redbull = team("Redbull","Dark-blue", 95, 145000000)
mclaren = team("McLaren","Orange", 95, 145000000)
ferrari = team("Ferrari","Red", 95, 145000000)
alpine = team("Apline","Light-blue", 95, 145000000)
alphatauri = team("AlphaTauri","Gray", 95, 145000000)
aston_martin = team("Aston Martin","Dark-Green", 95, 145000000)
williams = team("Williams","Blue", 95, 145000000)
alfa_romeo = team("Alfa Romeo","Dark-red", 95, 145000000)
haas = team("Haas","White", 95, 145000000)


class driver:
    def __init__(self, rank, name, age, number, nickname, wins, podiums, gp_entered, team ):
        self.rank = rank
        self.name = name
        self.age = age
        self.number = number
        self.nickname = nickname
        self.wins = wins
        self.podiums = podiums
        self.gp_entered = gp_entered
        self.team = team


Ham = driver(1, "Lewis Hamilton", 36, 44, "HAM", 100, 176, 281, mercedes)
Ver = driver(2, "Max Verstappen", 24, 33, "VER", 17, 53, 134, redbull)
Bot = driver(3, "Valtteri Bottas", 32, 77, "BOT", 9, 64, 171, mercedes)
Nor = driver(4, "Lando Norris", 21, 4, "NOR", 0, 5, 53, mclaren)
Per = driver(5, "Sergio Pérez", 31, 11, "PER", 2, 12, 207, redbull)
Sai = driver(6, "Carlos Saints", 27, 55, "SAI", 0, 5, 134, ferrari)
Lec = driver(7, "Charles Leclerc", 23, 16, "LEC", 2, 13, 73, ferrari)
Ric = driver(8, "Daniel Riccardo", 32, 3, "RIC", 8, 32, 203, mclaren)
Gas = driver(9, "Pierre Gasly", 25, 10, "GAS", 1, 3, 79, alphatauri)
Alo = driver(10, "Fernando Alonso", 40, 14, "ALO", 32, 97, 329, alpine)
Oco = driver(11, "Esteban Ocon", 25, 31, "OCO", 1, 2, 82, alpine)
Vet = driver(12, "Sebastian Vettel", 34, 5, "VET", 53, 122, 273, aston_martin)
Str = driver(13, "Lance Stroll", 22, 18, "STR", 0, 3, 93, aston_martin)
Tsu = driver(14, "Yuki Tsunoda", 21, 22, "TSU", 0, 0, 15, alphatauri)
Rus = driver(15, "George Russel", 36, 63, "RUS", 0, 1, 53, williams)
Lat = driver(16, "Nicholas Latifi", 26, 6, "LAT", 0, 0, 32, williams)
Räi = driver(17, "Kimi Räikönen", 41, 7, "RÄI", 21, 103, 345, alfa_romeo)
Gio = driver(18, "Antonio Giovinazzi", 27, 99, "GIO", 0, 0, 55, alfa_romeo)
Msc = driver(19, "Mick Schumacher", 22, 47, "MSC", 0, 0, 15,haas)
Maz = driver(20, "Nikita Mazepin", 22, 9, "MAZ", 0, 0, 15, haas)

class location:
    def __init__(self, location, location_name, ammount_of_laps, circut_name):
        self.location = location
        self.location_name = location_name
        self.ammount_of_laps = ammount_of_laps
        self.circut_name = circut_name

Bahrain = location("Bahrain", "Bahrainian", 57, "Bahrain International Circuit")
Italy = location("Italy", "Italian", 53, "Autodromo Nazionale di Monza")
Portugal = location("Portugal", "Portugeese", 66, "Algarve International Circuit")
Spain = location("Spain", "Spanish", 66, "	Circuit de Barcelona-Catalunya")
Monaco = location("Monaco", "Monaco", 78, "	Circuit de Monaco")
Azerbajan = location("Azerbajan", "Azerbaijan", 51, "Baku City Circuit")
France = location("France", "French", 53, "Circuit Paul Ricard")
Austria_1 = location("Austria", "Steiermark", 71, "Red Bull Ring")
Austria_2 = location("Austria", "Austrian", 71, "Red Bull Ring")
England = location("England", "British", 52, "	Silverstone Circuit")
Hungary = location("Hungary", "Hungarian", 70, "Hungaroring")
Belgium = location("Belgium", "Belgian", 44, "Circuit de Spa-Francorchamps")
Netherlands = location("Netherlands", "Dutch", 72, "Zandvoort")
Russia = location("Russia", "Russian", 53, "Sochi Autodrom")
Turkey = location("Turkey", "Turkish", 58, "Intercity Istanbul Park")
United_states = location("United States", "United States", 56, "Circuit of the Americas")
Mexico = location("Mexico", "Mexican", 71, "Autodromo Hermanos Rodriguez")
Brazil = location("Brazil", "Brazilian", 71, "Autodromo Jose Carlos Pace")
Saudi_arabia = location("Saudi Arabia", "Saudi Arabian", 50, "Jeddah Street Circuit")
Abu_dhabi = location("Abu Dhabi", "Abu Dhabi", 55, "Yas Marina Circuit")

driver_list = [Ham, Ver, Bot, Nor, Per, Sai, Lec, Ric, Gas, Alo, Oco, Vet, Str, Tsu, Rus, Lat, Räi, Gio, Msc, Maz]
location_list = [Bahrain, Italy, Portugal, Spain, Monaco, Azerbajan, France, Austria_1, Austria_2, England, Hungary, Belgium, Netherlands, Russia, Turkey, United_states, Mexico, Brazil, Saudi_arabia, Abu_dhabi]
incidents = ["crashed with", "Spun off", "engine failiure", ]

def grand_prix_start():

    number_location = random.randrange(0, 19)
    current_location = location_list[number_location]

    input("Press enter to start the race:")
    print("The " + current_location.location_name + " Grand Prix is about to start.")
    time.sleep(2)

    print("⚫ ⚫ ⚫ ⚫ ⚫", end="")

    for x in range (0,6):
        b = "🔴 " * x
        print (b, end="\r")
        time.sleep(1)

    time.sleep(2)

    print("⚫ ⚫ ⚫ ⚫ ⚫")

    time.sleep(1)
    print("And we are off... Hopefully this will be a great race here in " + current_location.location + ".")


def print_ranking():
    global rank
    race_end = False

    while race_end == False:
        rank += 1
        amount_drivers = len(driver_list)

        if amount_drivers > 0:
            number_driver = random.randrange(0, amount_drivers)
            current_driver = driver_list[number_driver]
            print(rank, current_driver.nickname)
            driver_list.pop(number_driver)

        else:
            race_end = True
            exit()


def lap():
    lap_incident_chance = random.randrange(0, 100)
    if lap_incident_chance <= 10:
        pass


grand_prix_start()
print_ranking()
