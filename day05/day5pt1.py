with open("day05/input5.txt") as f:
  ranges, ids = f.read().split("\n\n")
  ranges = [(int(x), int(y)) for x,y in [z.split("-") for z in ranges.split("\n")]]
  ids = [int(x) for x in ids.strip().split("\n")]

fresh = 0
for i in ids:
  for r in ranges:
    if r[0] <= i <= r[1]:
      fresh += 1
      break
print(fresh)