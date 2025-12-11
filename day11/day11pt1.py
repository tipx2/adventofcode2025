with open("day11/input11.txt") as f:
    lines = [x.strip() for x in f.readlines()]

adj = {}
for line in lines:
    key, values = line.split(": ")
    adj[key] = values.split(" ")

queue = ["you"]

paths = 0

while queue:
    current = queue.pop(0)
    if current == "out":
        paths += 1
        continue
   
    for a in adj[current]:
        queue.append(a)

    #print(queue)
print(paths)