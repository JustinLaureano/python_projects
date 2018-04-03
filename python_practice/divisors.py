"""
Create a program that asks the user for a number and then prints out a list
of all the divisors of that number.
"""


# number = int(input('enter a positive number: '))
# print([num for num in range(1, number) if number % num == 0])


contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["Javascript", "Gaming", "Foxes"]
    }
]


def lookup_profile(first_name, prop):
    for contact in contacts:
        if contact["firstName"] == first_name:
            if prop in contact:
                print(contact["firstName"], contact[prop])
            else:
                print("no prop with that name")
        else:
            print("Not in list")


lookup_profile("Sherlock", "number")
