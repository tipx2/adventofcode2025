import re
from functools import cache
with open("day10/example.txt") as f:
  lines = [x.strip() for x in f.readlines()]

def switch(current, button):
  current = list(current)
  for b in button:
    if b in current:
      current.remove(b)
    else:
      current.append(b)
  return tuple(sorted(current))

@cache
def dp(current, target, buttons):
  if current == target:
    return 0
  else:
    cheapest = 99999999999
    for b in buttons:
      result = 1 + dp(switch(current, b), target, buttons)
      cheapest = min(cheapest, result)
    return cheapest

for line in lines:
  target_string = re.search("\[.+\]", line).group().strip("[]")
  target_lights = []
  for i in range(len(target_string)):
    if target_string[i] == "#":
      target_lights.append(i)
  buttons = tuple(tuple(int(z) for z in x.strip("()").split(",")) for x in re.findall("\([,\d]+\)", line))
  joltage = [int(x) for x in re.search("\{[,\d]+\}", line).group().strip("{}").split(",")]
  print(dp(tuple(), tuple(target_lights), buttons))

