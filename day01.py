# Advent of Code 2023 - day 1

def get_parts_sum(lines):
    parts_sum = 0
    for line in lines:
        numbers = [x for x in [*line] if x.isdecimal()]
        parts_sum += int(''.join((numbers[0], numbers[-1])))
    return parts_sum

with open('input01.txt') as f:
    lines = f.read().split()

print(get_parts_sum(lines))

# Part 2
numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven':7,
    'eight': 8,
    'nine': 9,
}

new_lines = []

for line in lines:
    new_line = line
    for number in numbers:
        new_line = new_line.replace(number, number + str(numbers[number]) + number)
    new_lines.append(new_line)

print(get_parts_sum(new_lines))
