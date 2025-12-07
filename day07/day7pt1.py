with open("day07/input7.txt") as f:
  lines = [x.strip() for x in f.readlines()]

splitters = set()
lasers = []

lowest_i = len(lines)

for i in range(len(lines)):
  for j in range(len(lines[0])):
    if lines[i][j] == "S":
      lasers.append((i,j))
    elif lines[i][j] == "^":
      splitters.add((i,j))

def check_for_end(lasers):
  end = True
  for l in lasers:
    if l[0] > lowest_i:
      end = False
      break
  return end

splits = 0

while check_for_end(lasers):
  for x in range(len(lasers) -1, -1, -1):
    new_laser = (lasers[x][0] +1, lasers[x][1])
    if new_laser in splitters:
      lasers.append((new_laser[0], new_laser[1] + 1))
      lasers.append((new_laser[0], new_laser[1] - 1))
      splits += 1
    else:
      lasers.append(new_laser)
    lasers.remove(lasers[x])

  lasers = list(set(lasers))
print(splits)