# Advent of Code 2023 - day 2

cubes = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

possible = []
minimums = []

with open('input02.txt') as f:
    lines = f.read().split('\n')

for line in lines:
    game_id = int(line.split(':')[0].split()[1])
    rounds = line.split(':')[1].split(';')
    poss = True
    # part 2
    mins = {
        'red':1,
        'green':1,
        'blue':1
    }
    for round in rounds:
        pulls = round.split(',')
        for pull in pulls:
            values = pull.strip().split()
            # part 2
            mins[values[1]]= max(int(values[0]),mins[values[1]])
            for value in values:
                color = values[1]
                if int(values[0]) > cubes[color]:
                    poss = False
    # part 2
    minimums.append(mins['red'] * mins['blue'] * mins['green'])
    if poss == True:
        possible.append(game_id)

print(sum(possible))

# Part 2
print(sum(minimums))
