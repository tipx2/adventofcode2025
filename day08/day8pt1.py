import math
from collections import Counter

with open("day08/input8.txt") as f:
  lines = [x.strip() for x in f.readlines()]

def distance(coord1, coord2):
  return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 + (coord1[2] - coord2[2]) ** 2

distances = {}

boxes = [(int(x), int(y), int(z)) for x,y,z in [w.split(",") for w in lines]]

for b1 in boxes:
  for b2 in boxes:
    if b1 == b2 or (b1, b2) in distances or (b2, b1) in distances:
      continue
    distances[(b1, b2)] = distance(b1,b2)

circuits = {}
circuit_counter = 0
for (coord1, coord2), distance in sorted(distances.items(), key=lambda x: x[1])[:1000]:
  for original in (circuits[coord1] if coord1 in circuits else None, circuits[coord2] if coord2 in circuits else None):
    for key in circuits.keys():
      if circuits[key] == original:
        circuits[key] = circuit_counter

  circuits[coord1] = circuit_counter
  circuits[coord2] = circuit_counter

  circuit_counter += 1

print(math.prod(sorted(Counter(circuits.values()).values(), reverse=True)[:3]))