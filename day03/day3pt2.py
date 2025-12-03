with open("day03/input3.txt") as f:
  lines = [x.strip() for x in f.readlines()]

total = 0

for line in lines:
  nums = [int(x) for x in line]
  
  highest = 0
  pos = 0
  for i in range(len(nums)):
    if nums[i] > highest:
      highest = nums[i]
      pos = i


print()
print(total)