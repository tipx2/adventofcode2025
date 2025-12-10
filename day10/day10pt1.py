import re
with open("day10/input10.txt") as f:
    lines = [x.strip() for x in f.readlines()]


total = 0
for line in lines:
    target_string = re.search("\[.+\]", line).group().strip("[]")
    target_lights = 0
    for i in range(len(target_string)):
        if target_string[i] == "#":
            target_lights = target_lights | (1<<i)
   
    buttons = []
    for b_str in re.findall("\([,\d]+\)", line):
        button = 0
        for s in b_str.strip("()").split(","):
            button = button | (1<<int(s))
        buttons.append(button)

    # bfs
    queue = [(0, 0)]
    visited = set()
    while queue:
        value, clicks = queue.pop(0)
        if value == target_lights:
            total += clicks
            break
        for b in buttons:
            new = value^b
            if new not in visited:
                visited.add(new)
                queue.append((new, clicks+1))
print(total)