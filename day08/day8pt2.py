import heapq, time

def distance(coord1, coord2):
  return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 + (coord1[2] - coord2[2]) ** 2

start = time.perf_counter()

with open("day08/input8.txt") as f:
  lines = [x.strip() for x in f.readlines()]

distances = []
boxes = [(int(x), int(y), int(z)) for x,y,z in [w.split(",") for w in lines]]
all_boxes = len(boxes)


for b1 in range(all_boxes):
  for b2 in range(b1+1, all_boxes):
    distances.append((distance(boxes[b1],boxes[b2]), (boxes[b1], boxes[b2])))

heapq.heapify(distances)

count = 0
circuits = set()
while distances:
  distance, (coord1, coord2) = heapq.heappop(distances)
  
  if coord1 not in circuits:
    circuits.add(coord1)
    count += 1
  if coord2 not in circuits:
    circuits.add(coord2)
    count += 1

  if count == all_boxes:
    print(coord1[0] * coord2[0])
    break

print(time.perf_counter() - start)