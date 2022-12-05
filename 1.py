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

# +
import csv
import pprint

data = []

with open('data/1.csv', 'r') as datafile:
    reader = csv.reader(datafile)

    calories = 0

    for row in reader:
        if row == []:
            data.append(calories)
            calories = 0
        else:
            calories = calories + int(row[0])

print(data)

max_cal = max(data)
max_index = data.index(max_cal)

print(f'Maximum calories is {max_cal} with the {max_index} elf')

data.sort(reverse=True)
print(data)

top_3 = data[0] + data[1] + data[2]
print(f'Total of top 3 is {top_3}')

