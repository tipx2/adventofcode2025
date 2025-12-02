import math
with open("day02/input2.txt") as f:
  lines = f.read().strip().split(",")

total = 0

for r in lines:
  low,high = r.split("-")
  for x in range(int(low), int(high)+1):
    str_x = str(x)
    len_str_x = len(str_x)

    for z in range(1, (len_str_x//2) + 1):
      if str_x == str_x[:z] * (len_str_x//z):
        #print(x)
        total += x
        break

print()
print(total)