with open("day09/input9.txt") as f:
  lines = [x.strip() for x in f.readlines()]

red_tiles = [(int(x), int(y)) for x,y in [z.split(",") for z in lines]]
green_tiles = set()

minx = 999999999
maxx = 0
miny = 999999999
maxy = 0

for i in range(len(red_tiles)):
  target = red_tiles[i+1] if i != len(red_tiles)-1 else red_tiles[0]
  initial = red_tiles[i]
  
  minx = min(minx, initial[0])
  miny = min(miny, initial[1])
  maxx = max(maxx, initial[0])
  maxy = max(maxy, initial[1])
  
  delta = None
  
  if initial[0] < target[0]:
    delta = (1,0)
  elif initial[0] > target[0]:
    delta = (-1,0)
  elif initial[1] < target[1]:
    delta = (0,1)
  elif initial[1] > target[1]:
    delta = (0,-1)
  
  times = 1
  new = (initial[0] + (delta[0] * times), initial[1] + (delta[1] * times))
  while new != target:
    green_tiles.add(new)
    times += 1
    new = (initial[0] + (delta[0] * times), initial[1] + (delta[1] * times))

for l in red_tiles:
  green_tiles.add(l)

print(maxy)
for y in range(miny, maxy+1):
  if y % 1000 == 0:
    print("aryehvalue:", y)
  spout = False
  for x in range(minx,maxx+1):
    if (x,y) in green_tiles and not (x-1,y) in green_tiles:
      spout = not spout
    if spout:
      green_tiles.add((x,y))

def all_green(l1, l2, green_tiles):
  for y in range(min(l1[1], l2[1]), max(l1[1], l2[1])):
    for x in range(min(l1[0], l2[0]), max(l1[0], l2[0])):
      if (x,y) not in green_tiles:
        return False
  return True

largest = 0

for l1 in red_tiles:
  for l2 in red_tiles:
    if not all_green(l1, l2, green_tiles):
      continue
    area = abs(l1[0] - l2[0] + 1) * abs(l1[1] - l2[1] + 1)
    if area > largest:
      largest = area
print(largest)