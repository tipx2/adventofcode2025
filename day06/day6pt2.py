import math
with open("day06/input6.txt") as f:
  lines = [x.strip("\n") for x in f.readlines()]

eqns = []

operations_line = lines[-1]
del lines[-1]

i = 1

while i < len(operations_line):
  current_op = operations_line[i-1]
  start_pos = i-1
  while i < len(operations_line) and operations_line[i] not in "*+":
    i += 1

  eqn = []
  for x in range(i-1, start_pos-1, -1):
    s = ""
    for line in lines:
      s += line[x]
    eqn.append(s)
  eqn.append(current_op)
  eqns.append(eqn)
  i+=1

total = 0
for eqn in eqns:
  if eqn[-1] == "+":
    total += sum([int(x) for x in eqn[0:-1] if x.strip() != ""])
  elif eqn[-1] == "*":
    total += math.prod([int(x) for x in eqn[0:-1] if x.strip() != ""])
print(total)