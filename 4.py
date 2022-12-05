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

def in_to_out(i):
    pi = i.split('-')
    p = range(int(pi[0]), int(pi[1])+1)
    p = [x for x in p]
    return p

def one_in_two(p1, p2):
    p12 = [x for x in p2 if x in p1]
    if p12 == p1:
       return True
    else:
        return False

within = 0
lines = 0
with open('data/3.csv', 'r') as fopen:
    reader = csv.reader(fopen)

    for row in reader:
        lines = lines + 1
        p1 = in_to_out(row[0])
        p2 = in_to_out(row[1])

        if one_in_two(p1, p2) or one_in_two(p2,p1):
            within = within + 1

print(within)
print(lines)


# +
def overlap(p1, p2):
    p = [x for x in p1 if x in p2]
    return len(p) > 0

ol = 0
lines = 0
with open('data/3.csv', 'r') as fopen:
    reader = csv.reader(fopen)

    for row in reader:
        lines = lines + 1
        p1 = in_to_out(row[0])
        p2 = in_to_out(row[1])

        if overlap(p1, p2):
            ol = ol + 1

print(ol)
print(lines)

# +
p1 = [1,2,3]
p2 = [2,3]

assert not one_in_two(p1, p2)
assert one_in_two(p2, p1)

p1 = [1,2,3]
p2 = [3]

assert not one_in_two(p1, p2)
assert one_in_two(p2, p1)

p1 = [1,2,3]
p2 = [1]

assert not one_in_two(p1, p2)
assert one_in_two(p2, p1)

p1 = [1,2,3]
p2 = [2]

assert not one_in_two(p1, p2)
assert one_in_two(p2, p1)

p1 = [1,2,3,4,5]
p2 = [2,3,4]

assert not one_in_two(p1, p2)
assert one_in_two(p2, p1)

