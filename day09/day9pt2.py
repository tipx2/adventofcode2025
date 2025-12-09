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


def debug_draw(x1,y1,x2,y2):
  for y in range(10):
    for x in range(15):
      if (x,y) == (x1,y1) or (x,y) == (x2,y2):
        print("@", end="")
      elif (x,y) in red_tiles:
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
  flippedx1 = False
  flippedx2 = False
  for x in range(min(x1, x2)+1, max(x1, x2)):
    if ((x,y1) in green_tiles) != ((x-1,y1) in green_tiles):
      if flippedx1:
        return False
      else:
        flippedx1 = True
    
    if ((x,y2) in green_tiles) != ((x-1,y2) in green_tiles):
      if flippedx2:
        return False
      else:
        flippedx2 = True
  
  flippedy1 = False
  flippedy2 = False
  for y in range(min(y1, y2)+1, max(y1, y2)):
    if ((x1,y) in green_tiles) != ((x1,y-1) in green_tiles):
      if flippedy1:
        return False
      else:
        flippedy1 = True
    
    if ((x2,y) in green_tiles) != ((x2,y-1) in green_tiles):
      if flippedy2:
        return False
      else:
        flippedy2 = True

  return True

largest = 0

for i in range(len(red_tiles)):
  for j in range(i+1, len(red_tiles)):
    x1,y1 = red_tiles[i]
    x2,y2 = red_tiles[j]

    area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
    if area > largest:
      if valid(x1,y1,x2,y2):
        debug_draw(x1,y1,x2,y2)
        print(x1,y1,x2,y2)
        largest = area

print(largest)