# Advent of Code 2023 - day 5
with open('input5.txt') as f:
    lines = f.read().split('\n')

groups = [[]]

for line in lines:
    if line == "":
        groups.append([])
    else:
        groups[-1].append(line)

initial_seeds = [*map(int, groups.pop(0)[0].split(": ")[1].split(" "))]
seeds = initial_seeds.copy()

stripped_groups = []

for group in groups:
    group.pop(0)
    stripped_groups.append([])
    for line in group:
        line = [int(line.split()[i]) for i in [1,0,2]]
        stripped_groups[-1].append(line)
    # for part 2
    stripped_groups[-1].sort()

for i in range(len(stripped_groups)):
    for j in range(len(seeds)):
        seed = seeds[j]
        group = stripped_groups[i]
        found = False
        for line in group:
            if seed in range(line[0], line[0] + line[2]):
                found = True
                seeds[j] = seed + line[1] - line[0]

print(min(seeds))

# Part 2
seed_pairs = []
for i in range(0, len(initial_seeds)-1, 2):
    seed_pairs.append((initial_seeds[i], initial_seeds[i]+initial_seeds[i+1]-1))

def eval(low, high, mapping):
    result = []
    for line in mapping:
        source_low, dest, range_length = line
        source_high = source_low + range_length - 1
        if low < source_low:
            if high < source_low:
                result.append((low, high))
                return result
            result.append((low, source_low-1))
            low = source_low
        if low > source_high:
            continue
        if high <= source_high:
            result.append((low - source_low + dest, high - source_low + dest))
            return result
        result.append((low - source_low + dest, source_high - source_low + dest))
        low = source_high + 1
    result.append((low, high))
    return result

def find_min(pair, map_level):
    mapping = stripped_groups[map_level]
    low, high = pair
    ranges = eval(low, high, mapping)
    if map_level == len(stripped_groups) - 1:
        return ranges[0][0]
    return min([find_min(pair, map_level+1) for pair in ranges])

mins = [find_min(pair, 0) for pair in seed_pairs]

print(min(mins))
