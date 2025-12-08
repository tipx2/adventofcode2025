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


circuits = set()
for (coord1, coord2), distance in sorted(distances.items(), key=lambda x: x[1]):
  circuits.add(coord1)
  circuits.add(coord2)

  if all(b in circuits for b in boxes):
    print(coord1[0] * coord2[0])
    break
