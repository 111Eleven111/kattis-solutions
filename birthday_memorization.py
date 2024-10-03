"""
KATTIS: Birthday Memorization
https://open.kattis.com/problems/fodelsedagsmemorisering

Krarkl wants to learn the birthdays of all his 
friends, so he knows whom to congratulate each day. 
Unfortunately collisions sometimes arise, meaning 
several friends may have the same birthday. This may 
confuse Krarkl, so he decided to only remember the 
birthday of the friend he likes the most in case of 
a collision. Given a list of birthdays for each of his 
friends and how much Krarkl likes each friend, print what 
friends Krarkl will remember the birthday for.

Input, first line: N lines
Remaining N lines: <name like_amount birthdaydate>

Output, first line: K amount of friends Krarkl
Remaining K lines: name of friends Krarkl will remember
"""

sample_input = """10
Oden 78 03/12
Tor 132 14/05
Freja 10000 14/05
Loke 512 12/10
Hel 14 04/05
Fjorgynn 532 13/05
Hildegun 500 13/05
Vindsval 17 03/12
Snotra 20 04/05
Kvaser 420 03/12"""

data = sample_input
data_list = data.split("\n"); data_list.pop(0)
my_dict = {}

# Read data from input
for friend in data_list:
    friend = friend.split() # Creates friend data as [name, bond, date]
    
    # In case of conflicting birthday, keep name with largest bond value
    if friend[2] in my_dict:
        if int(friend[1]) > int(my_dict[friend[2]][1]):
            my_dict[friend[2]] = friend
    else:
        my_dict[friend[2]] = friend # Add name with new date

# Print answer in requested format
print(len(my_dict))
to_print = []
for key, value in my_dict.items():
    to_print.append(value[0])

to_print.sort()
for name in to_print:
    print(name)