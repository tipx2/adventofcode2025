import re
import heapq

with open("day10/input10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def add_clicks(joltage, button):
    return tuple(joltage[i] + (1 if i in button else 0) for i in range(len(joltage)))

def distance(current_joltage, target_joltage):
    return sum([abs(current_joltage[i]-target_joltage[i]) for i in range(len(current_joltage))])

total = 0
for line in lines:

    buttons = tuple(tuple(int(z) for z in x.strip("()").split(",")) for x in re.findall("\([,\d]+\)", line))
    target_joltage = tuple(int(x) for x in re.search("\{[,\d]+\}", line).group().strip("{}").split(","))

    initial_joltage = tuple([0] * len(target_joltage))
    queue = [(0, initial_joltage)]

    heapq.heapify(queue)

    visited = set()
    while queue:
        print(queue)
        clicks, current_joltage = heapq.heappop(queue)
        if current_joltage == target_joltage:
            print(clicks)
            total += clicks
            break
        else:
            for b in buttons:
                new = add_clicks(current_joltage, b)
                if any(target_joltage[i] < new[i] for i in range(len(new))):
                  continue
                if new not in visited:
                    visited.add(new)
                    queue.append((clicks + 1, new))
print(total)