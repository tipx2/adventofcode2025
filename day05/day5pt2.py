from intervaltree import Interval, IntervalTree

with open("day05/input5.txt") as f:
  ranges, ids = f.read().split("\n\n")
  ranges = set((int(x), int(y)) for x,y in [z.split("-") for z in ranges.split("\n")])

total = 0

tree = IntervalTree()
for r in ranges:
  tree[r[0]:r[1]+1] = True

tree.merge_overlaps()

for item in tree:
  total += item.end-item.begin
print(total)