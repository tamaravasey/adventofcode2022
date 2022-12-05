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

data = []

with open('data/2.csv', 'r') as datafile:
    reader = csv.reader(datafile)

    total_score = 0
    for row in reader:

        score = 0
        inputs = row[0].split(' ')
        elf = inputs[0]
        me = inputs[1]

         # A for Rock, B for Paper, and C for Scissors.
        #  X for Rock, Y for Paper, and Z for Scissors
        # (1 for Rock, 2 for Paper, and 3 for Scissors)
        # # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

        # AX = 1+3 = 4

        if me == 'X':
            score = 1
        elif me == 'Y':
            score = 2
        elif me == 'Z':
            score = 3
        else:
            print("ERROR")

        if (elf == 'A' and me == 'X') or (elf == 'B' and me == 'Y') or (elf == 'C' and me == 'Z'):
            score = score + 3
        else:
            if elf == 'A':
                if me == 'Y':
                    score = score + 6
                # else I lose and add nothing
            elif elf == 'B':
                if me == 'Z':
                    score = score + 6
            elif elf == 'C':
                if me == 'X':
                    score = score + 6
            else:
                print("ERROR2")
        print(f'{row} = {score}')

        total_score = total_score + score

print(total_score)


# +

data = []

with open('data/2.csv', 'r') as datafile:
    reader = csv.reader(datafile)
    total_score = 0
    for row in reader:
        score = 0
        inputs = row[0].split(' ')
        elf = inputs[0]
        me = inputs[1]

         # A for Rock, B for Paper, and C for Scissors.
        #  X for Rock, Y for Paper, and Z for Scissors
        # (1 for Rock, 2 for Paper, and 3 for Scissors)
        # # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

        # X lose Y draw Z win
        # In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock.
        # This gives you a score of 1 + 3 = 4.
        # In the second round, your opponent will choose Paper (B),
        # and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
        # In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

        if me == 'X': # lose
            score = 0
            if elf == 'A':
                # rock so choose scisors
                score = score + 3
            elif elf == 'B':
                # paper so choose rock
                score = score + 1
            else:
                score = score + 2
        elif me == 'Y': # draw
            score = 3
            if elf == 'A':
                # rock so choose rock
                score = score + 1
            elif elf == 'B':
                score = score + 2
            else:
                score = score + 3
        elif me == 'Z':
            score = 6
            if elf == 'A':
                # rock so choose paper
                score = score + 2
            elif elf == 'B':
                # paper so choose sciss
                score = score + 3
            else:
                score = score + 1
        else:
            print("ERROR")
        total_score = total_score + score

print(total_score)

# -


