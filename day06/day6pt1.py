import re, math
with open("day06/input6.txt") as f:
  lines = [x.strip() for x in f.readlines()]

eqns = {}

for line in lines:
  l = re.sub(" {2,}", " ", line)
  l = l.split(" ")
  for x in range(len(l)):
    if x not in eqns:
      eqns[x] = []
    eqns[x].append(l[x])

total = 0
for eqn in eqns.values():
  if eqn[-1] == "+":
    total += sum([int(x) for x in eqn[0:-1]])
  elif eqn[-1] == "*":
    total += math.prod([int(x) for x in eqn[0:-1]])

print(total)
