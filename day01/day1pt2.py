with open("day01/input1.txt") as f:
  lines = [x.strip() for x in f.readlines()]

arrow = 50

zeroes = 0


for l in lines:
  if l[0] == "R":
    for x in range(int(l[1:])):
      arrow = (arrow + 1) % 100
      if arrow == 0:
        zeroes += 1
  elif l[0] == "L":
    for x in range(int(l[1:])):
      arrow = (arrow - 1) % 100
      if arrow == 0:
        zeroes += 1

print(zeroes)