with open("day05/input5.txt") as f:
  ranges, ids = f.read().split("\n\n")
  
  events = []
  for a,b in [z.split("-") for z in ranges.split("\n")]:
    events.append((int(a), "start"))
    events.append((int(b)+1, "end"))

events = sorted(events, key=lambda x: x[0])

total = 0
currently_open = 0
earliest_opening = 0

for e in events:
  if e[1] == "start":
    currently_open += 1
    if currently_open == 1:
      earliest_opening = e[0]
  elif e[1] == "end":
    currently_open -= 1
    if currently_open == 0:
      total += e[0] - earliest_opening

print(total)
  
