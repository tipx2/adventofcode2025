import math
with open("day02/input2.txt") as f:
  lines = f.read().strip().split(",")

total = 0

def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

def last_n_digits(num, n):
  return num % (10 ** n)

for r in lines:
  low,high = r.split("-")
  low = int(low)
  high = int(high)
  for x in range(low, high+1):
    len_x = len(str(x))
    if len_x % 2 != 0:
      continue
    
    half_len_x = len_x//2
    if first_n_digits(x, half_len_x) == last_n_digits(x, half_len_x):
      # print(x)
      # print(first_n_digits(x, half_len_x), last_n_digits(x, half_len_x))
      # print()
      total += x
    
print(total)