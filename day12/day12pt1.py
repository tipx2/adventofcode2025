with open("day12/input12.txt") as f:
  lines = f.read().split("\n\n")

blocks = []
for x in range(6):
  str_block = lines[x].split(":")[1].split("\n")[1:]
  block = []
  for i in range(len(str_block)):
    for j in range(len(str_block[0])):
      if str_block[i][j] == "#":
        block.append((i,j))
  blocks.append(block)

boards = [x.split(": ") for x in lines[6].strip().split("\n")]
for i in range(len(boards)):
  boards[i][0] = tuple(int(x) for x in boards[i][0].split("x"))
  boards[i][1] = tuple(int(x) for x in boards[i][1].split(" "))
  boards[i] = tuple(boards[i])

total = 0
unverified = 0
for board in boards:
  (sizex,sizey), counts = board

  # trivial yes case
  if sizex * sizey >= 9 * sum(counts):
    total += 1
    continue

  # trivial no case
  if sizex * sizey < sum([counts[i] * len(blocks[i]) for i in range(len(blocks))]):
    continue

  
  # print("PERFORM SOME KIND OF COMPUTER SCIENCE MAGICK")
  unverified +=1

print(total)
print(unverified)