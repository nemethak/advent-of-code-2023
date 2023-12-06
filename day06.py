import math

with open('input06.txt') as f:
    lines = f.read().split('\n')

times = [*map(int, lines[0].split()[1:])]
distances = [*map(int, lines[1].split()[1:])]

values = []

for i in range(len(times)):
    goal = distances[i]
    time = times[i]
    value = 0
    for j in range(1, time + 1):
        if j * (time - j) > goal:
            value += 1
    values.append(value)

print(math.prod(values))

# Part 2

time = int(('').join(lines[0].split()[1:]))
distance = int(('').join(lines[1].split()[1:]))

min_time = 0
max_time = 0

for i in range(1, time + 1):
    if i * (time - i) > distance:
        min_time = i
        break

for i in range(time, 0, -1):
    if i * (time - i) > distance:
        max_time = i
        break
    
print(max_time - min_time + 1)
