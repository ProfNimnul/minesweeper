import random
from array import array

x = input("x=")
y = input("y=")

print(x, y)
baseX = int(x) + 1
baseY = int(y) + 1
t = [0 for i in range(0, baseX)]
cells = array('I', t)

print(cells[2])
random.seed()
for i in range(0, baseX):
    for j in range(0, baseY):
        cells[i][j] = 0
# mine = random.randint(0, 1)
