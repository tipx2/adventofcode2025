with open("day09/input9.txt") as f:
  lines = [x.strip() for x in f.readlines()]

red_tiles = [(int(x), int(y)) for x,y in [z.split(",") for z in lines]]
polygon = []

for i in range(len(red_tiles)):
  target = red_tiles[i+1] if i != len(red_tiles)-1 else red_tiles[0]
  initial = red_tiles[i]
  
  polygon.append(initial)
  
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
    polygon.append(new)
    times += 1
    new = (initial[0] + (delta[0] * times), initial[1] + (delta[1] * times))

def valid(x1,y1,x2,y2):
  for x,y in polygon:
    if min(x1, x2) < x < max(x1, x2) and min(y1, y2) < y < max(y1, y2):
      return False
  return True

def area(c1,c2):
  return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)

all_rects = [(area(red_tiles[x],red_tiles[y]), red_tiles[x],red_tiles[y]) for x in range(len(red_tiles)) for y in range(x+1, len(red_tiles))]
all_rects.sort(reverse=True)

for i, pair in enumerate(all_rects):
  x1,y1 = pair[1]
  x2,y2 = pair[2]
  
  if valid(x1,y1,x2,y2):
    print(pair[0])
    break