from functools import cache
with open("day11/input11.txt") as f:
    lines = [x.strip() for x in f.readlines()]

adj = {}
for line in lines:
    key, values = line.split(": ")
    adj[key] = values.split(" ")

@cache
def dfs(current, end, endbounds):

    if current in endbounds:
        return 0
    elif current == end:
        return 1
    else:
        return sum([dfs(a, end, endbounds) for a in adj[current]])
           

first = dfs("svr", "fft", frozenset(["nno", "idq", "uur", "vpw", "dsj"]))
second = dfs("fft", "dac", frozenset(["vms", "biw", "you"]))
third = dfs("dac", "out", frozenset())

print(first, second, third)
print(first * second * third)