from functools import cache
with open("day07/example.txt") as f:
  lines = [x.strip() for x in f.readlines()]

splitters = set()
initial = None

lowest_i = len(lines)

for i in range(len(lines)):
  for j in range(len(lines[0])):
    if lines[i][j] == "S":
      initial = (i,j)
    elif lines[i][j] == "^":
      splitters.add((i,j))

@cache
def split_laser(i, j):
  if i >= lowest_i:
    return 0
  if (i, j) in splitters:
    return 1 + split_laser(i, j + 1) + split_laser(i, j - 1)
  return split_laser(i + 1, j)

print(1 + split_laser(initial[0], initial[1]))
