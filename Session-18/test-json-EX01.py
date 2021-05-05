import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-EX0.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print()
print("Number of persons in the database: ", len(people))
for character in people:
    termcolor.cprint("Name: ", 'green', end="")
    print(character['Firstname'], character['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(character['age'])

    phoneNumbers = character['phoneNumber']
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])