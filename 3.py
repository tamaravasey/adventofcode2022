# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52
#
# A27
# B28
# C29
# D30
# E31
# F32
#
# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

# +
import csv

overlaps = []
file_length = 0
with open('data/4.csv', 'r') as r_file:
    reader = csv.reader(r_file)

    for row in reader:
        file_length = file_length + 1
        length = len(row[0])
        lon2 = int(length/2)
        r1 = []
        r2 = []
        for num, char in enumerate(row[0]):
            if num < lon2:
                r1.append(char)
            else:
                r2.append(char)

        ruck = [r1, r2]
        # print(row)
        # print(ruck)

        overlap = [x for x in r1 if x in r2]
        overlap = set(overlap)
        for o in overlap:
            overlaps.append(o)

assert file_length == len(overlaps)


def alpha(a):
    b = ord(a) - 96 #lowercase a starts at 97
    if b < 0:
        b = ord(a) - 64 + 26 #uppercase A starts at

    return b

over_num = [alpha(o) for o in overlaps]

print(overlaps)
print(over_num)

print(sum(over_num))

# +
overlaps = []
file_length = 0
badges = []
with open('data/4.csv', 'r') as r_file:
    reader = csv.reader(r_file)
    group = 0
    rucks = []

    for row in reader:

        file_length = file_length + 1

        rucks.append(row[0])

        if group == 2:
            # find
            badge = [x for x in rucks[0] if x in rucks[1] and x in rucks[2]]
            badge = set(badge)
            assert len(badge) == 1

            for b in badge:
                badges.append(alpha(b))
            rucks = []
            group = 0
        else:
            group = group + 1


def alpha(a):
    b = ord(a) - 96 #lowercase a starts at 97
    if b < 0:
        b = ord(a) - 64 + 26 #uppercase A starts at

    return b



print(badges)
print(sum(badges))

