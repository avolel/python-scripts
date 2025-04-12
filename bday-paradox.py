import datetime
import random

def getBirthdays(number_of_bdays):
    birthdays = []
    for a in range(number_of_bdays):
        startOfYear = datetime.date(1960,1,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None #All bdays are unique so we return None
    
    #Comparing each birthday to every other birthday
    for a, bdayA in enumerate(birthdays):
        for b, bdayB in enumerate(birthdays[a + 1 :]):
            if(bdayA == bdayB):
                return bdayA #Return the matching birthday

print('''Birthday Paradox
      
      Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
      This programme does a Monte Carlo simulation (that is, repeated random simulations) to explore this concepct.
      
      It's not actually a paradox, it's just a surprising result.
      ''')

#We need a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: #Keep asking until a valid amount is entered
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #Valid amount has been entered
print()

#Generating and displaying the birthdays
print("Here are ", numBDays, "birthdays:")
birthdays = getBirthdays(numBDays)
for i, bday in enumerate(birthdays):
    if i != 0:
        #Display a comma for each birthday after the first birthday
        print(", ", end='')
        monthName = MONTHS[bday.month - 1]
        dateText = "{} {}".format(monthName, bday.day)
        print(dateText, end='')
print()
print()

#Now determine if they are two birthdays that match
match = getMatch(birthdays)

#Display results
print("In this simulation, ", end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print("Multiple people have a birthday on", dateText)
else:
    print("There are no matching birthdays.")
print()

#Run through 100,000 simulations
print("Gererating", numBDays, "random birthdays 100,000 times...")
input("Press Enter to Begin...")

print("Let's run another 100,000 simulations.")
simMatch = 0 #How many simulations had matching bdays
for i in range(100_000):
    #Report on progress every 10,000 simulations
    if i % 10_000 == 0:
        print(i,"Simulation run...")
    birthdays = getBirthdays(numBDays)
    if(getMatch(birthdays) != None):
        simMatch += 1
print("100,000 simulations run.")

#Simulation Results
probability = round(simMatch / 100_000 * 100, 2)
print("Out of 100,000 simulations of", numBDays,"people, there was a")
print("matching birthday in that group", simMatch, "times. This means")
print("that", numBDays,"people have a", probability,"% chance of")
print("having a matching birthday in their group.")
print("That's probably more than you would think!")