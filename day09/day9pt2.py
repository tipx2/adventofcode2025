with open("day09/example.txt") as f:
  lines = [x.strip() for x in f.readlines()]

red_tiles = [(int(x), int(y)) for x,y in [z.split(",") for z in lines]]
green_tiles = set()

for i in range(len(red_tiles)):
  target = red_tiles[i+1] if i != len(red_tiles)-1 else red_tiles[0]
  initial = red_tiles[i]
  
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


def debug_draw():
  for y in range(15):
    for x in range(15):
      if (x,y) in red_tiles:
        print("#", end="")
      elif (x,y) in green_tiles:
        print("X", end="")
      else:
        print(".", end="")
    print()

# debug_draw()

for l in red_tiles:
  green_tiles.add(l)

def valid(x1,y1,x2,y2):
  for x in range(min(x1, x2), max(x1, x2) + 1):
    if (x,y1) in green_tiles and (x+1,y1) not in green_tiles and (x-1,y1) not in green_tiles:
      return False
    if (x,y2) in green_tiles and (x+1,y2) not in green_tiles and (x-1,y2) not in green_tiles:
      return False

  for y in range(min(y1, y2), max(y1, y2) + 1):
    if (x1,y) in green_tiles and (x1,y+1) not in green_tiles and (x1,y-1) not in green_tiles:
      return False
    if (x2,y) in green_tiles and (x2,y+1) not in green_tiles and (x2,y-1) not in green_tiles:
      return False
    
  return True

largest = 0

for i in range(len(red_tiles)):
  for j in range(i+1, len(red_tiles)):
    x1,y1 = red_tiles[i]
    x2,y2 = red_tiles[j]

    if not valid(x1,y1,x2,y2):
      continue

    area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
    if area > largest:
      largest = area
      print(x1,y1,x2,y2, area)

print(largest)