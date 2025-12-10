import re
import sympy as sym
from itertools import product

with open("day10/input10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

alphabet = list(map(chr, range(97, 123)))

total = 0
for i, line in enumerate(lines):
    print("aryehvalue:",i)

    buttons = tuple(tuple(int(z) for z in x.strip("()").split(",")) for x in re.findall("\([,\d]+\)", line))
    target_joltage = tuple(int(x) for x in re.search("\{[,\d]+\}", line).group().strip("{}").split(","))
    
    symbols = [[] for _ in range(len(target_joltage))]
    eqns = []
    for i, button in enumerate(buttons):
      symbol = sym.Symbol(alphabet[i])
      for b in button:
        symbols[b].append(symbol)
    
    for x in range(len(symbols)):
      eqns.append(sym.Eq(sum(symbols[x]), target_joltage[x]))
    
    result = sym.solve(eqns)
    
    frees = set()
    for r in result.values():
      frees = frees.union(r.free_symbols)
    
    frees = list(frees)
    upper_bounds = []
    for symbol in frees:
      minimum = 999999999999
      for j in buttons[alphabet.index(symbol.name)]:
        minimum = min(target_joltage[j], minimum)
      upper_bounds.append(range(minimum+1))
    
    min_solution = 999999999999
    
    prev = -1
    for combination in product(*upper_bounds):
      if combination and combination[0] != prev:
        print(combination)
        prev = combination[0]
      
      if sum(combination) >= min_solution:
        continue
      
      solved_values = []
      for r in result.values():
        solved_values.append(r.subs({frees[i]:combination[i] for i in range(len(frees))}))
      
      if all([x >= 0 and round(x) == round(x, 5) for x in solved_values]):
        min_solution = min(sum(solved_values) + sum(combination), min_solution)
    
    total += min_solution
    
print(total)