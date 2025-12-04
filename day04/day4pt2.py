with open("day04/input4.txt") as f:
  lines = [x.strip() for x in f.readlines()]

rolls = set()

for x in range(len(lines)):
  for y in range(len(lines)):
    if lines[x][y] == "@":
      rolls.add((x, y))

def get_accessible():
  accessible = set()
  for x,y in rolls:
    surrounding = 0
    for offsetx, offsety in [(x-1,y), (x+1, y), (x+1, y+1), (x-1, y-1), (x, y+1), (x, y-1), (x-1, y+1), (x+1, y-1)]:
      if (offsetx, offsety) in rolls:
        surrounding += 1
    
    if surrounding < 4:
      accessible.add((x,y))
  return accessible

removed = 0
while accessible := get_accessible():
  rolls = rolls - accessible
  removed += len(accessible)


print(removed)