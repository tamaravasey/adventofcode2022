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

#

# +
They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

# +
import copy

inputs = '''
[P]     [L]         [T]
[L]     [M] [G]     [G]     [S]
[M]     [Q] [W]     [H] [R] [G]
[N]     [F] [M]     [D] [V] [R] [N]
[W]     [G] [Q] [P] [J] [F] [M] [C]
[V] [H] [B] [F] [H] [M] [B] [H] [B]
[B] [Q] [D] [T] [T] [B] [N] [L] [D]
[H] [M] [N] [Z] [M] [C] [M] [P] [P]'''
in_stacks = []

for row in inputs.split('\n'):
    in_box = row.split(' ') # pesky 4 whitespaces for a missing box.
    in_stacks.append(in_box)

blanks = 0
in_stacks_2 = []

for sn, ss in enumerate(in_stacks):
    to_keep = []
    for bn, stack in enumerate(ss):

        if stack == '':

            blanks = blanks + 1
            if blanks == 4:
                to_keep.append('')
                blanks = 0
        else:
            to_keep.append(stack[1])

   # print(to_keep)
    in_stacks_2.append(to_keep)

stacks = []

for idx in range(9):
    stack = []
    stacks.append(stack)

for sn in range(len(in_stacks_2)-1, 0, -1):
    for bn in range(len(in_stacks_2[sn])):
        if in_stacks_2[sn][bn] != '':
            stacks[bn].append(in_stacks_2[sn][bn])

for s in stacks:
    print(s)

stacks_orig = copy.copy(stacks)

# +
import csv

# #inputs = '''
# [P]     [L]         [T]
# [L]     [M] [G]     [G]     [S]
# [M]     [Q] [W]     [H] [R] [G]
# [N]     [F] [M]     [D] [V] [R] [N]
# [W]     [G] [Q] [P] [J] [F] [M] [C]
# [V] [H] [B] [F] [H] [M] [B] [H] [B]
# [B] [Q] [D] [T] [T] [B] [N] [L] [D]
# [H] [M] [N] [Z] [M] [C] [M] [P] [P]'''


# pushed for time, doing it unprogrammatically ;)
# stacks[0] = ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P']
# stacks[1] = ['M', 'Q', 'H']
# stacks[2] = ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L']
# stacks[3] = ['Z', 'T', 'F', 'Q', 'M', 'W', 'G']
# stacks[4] = ['M', 'T', 'H', 'P']
# stacks[5] = ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T']
# stacks[6] = ['M', 'N', 'B', 'F', 'V', 'R']
# stacks[7] = ['P', 'L', 'H', 'M', 'R', 'G', 'S']
# stacks[8] = ['P', 'D', 'B', 'C', 'N']

# read the inputs
with open('data/5.csv', 'r') as instructions:
    reader = csv.reader(instructions, delimiter=' ')

    for row in reader:
        #print(row)
        #eg ['move', '3', 'from', '2', 'to', '6']

        for moves in range(int(row[1])):
            crate = stacks[int(row[3])-1].pop()
            stacks[int(row[5])-1].append(crate)

for stack in stacks:
    print(stack)

message = ''
for stack in stacks:
    message = message + stack[-1]

print(message)

# +
# moving all in order

stacks = copy.copy(stacks_orig)

# read the inputs
with open('data/5.csv', 'r') as instructions:
    reader = csv.reader(instructions, delimiter=' ')

    for row in reader:
        print(row)
        #eg ['move', '3', 'from', '2', 'to', '6']

        moves = int(row[1])
        f = int(row[3]) -1
        t = int(row[5]) -1

        crate = stacks[f][-moves:]
        stacks[f] = stacks[f][0:-1*int(row[1])]

        for c in crate:
            stacks[t].append(c)

for stack in stacks:
    print(stack)

message = ''
for stack in stacks:
    message = message + stack[-1]

print(message)

