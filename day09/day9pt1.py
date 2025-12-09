with open("day09/input9.txt") as f:
  lines = [x.strip() for x in f.readlines()]

tiles = [(int(x), int(y)) for x,y in [z.split(",") for z in lines]]

largest = 0

for l1 in tiles:
  for l2 in tiles:
    area = abs(l1[0] - l2[0] + 1) * abs(l1[1] - l2[1] + 1)
    if area > largest:
      largest = area
print(largest)