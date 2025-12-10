with open("day03/input3.txt") as f:
    lines = [x.strip() for x in f.readlines()]

total = 0
line_len = len(lines[0])

# find highest number with at least 11 digits after it, then 10, etc.
for line in lines:
    nums = [int(i) for i in line]

    final = 0
    for x in range(12):
        #print(nums)

        highest = 0
        place = 0
        for i in range(len(nums) - 11 + x):
            if nums[i] > highest:
                highest = nums[i]
                place = i
       
        nums = nums[place+1:]
        final += highest * (10 ** (11-x))
    total += final


print(total)