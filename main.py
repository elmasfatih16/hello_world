import numpy as np 

nodes = dict()

class Node: 
  def __init__(self, id, x, y):
    self.id = id
    self.x = x
    self.y = y
    self.rest = [0, 0]
    self.p = [0, 0]
    self.dof = [-1, -1]
    nodes[id] = self
    
  
Node(id=1, x=0, y=0)
Node(id=2, x=3, y=0)
Node(id=3, x=6, y=0)
Node(id=4, x=9, y=0)
Node(id=5, x=12, y=0)
Node(id=6, x=0, y=1)
Node(id=7, x=3, y=1)
Node(id=8, x=6, y=1)
Node(id=9, x=9, y=1)
Node(id=10, x=12, y=1)
Node(id=11, x=0, y=2)
Node(id=12, x=3, y=2)
Node(id=13, x=6, y=2)
Node(id=14, x=9, y=2)
Node(id=15, x=12, y=2)

nodes[1].rest = [1, 1]
nodes[6].rest = [1, 1]
nodes[11].rest = [1, 1]
nodes[15].p = [0, -100]

M = 0
for id, node in nodes.items():
    if node.rest[0] == 0:
      node.dof[0] =M
      M = M + 1

    if node.rest[1] == 0:
      node.dof[1] = M
      M = M + 1

N = M

for id, node in nodes.items():
    if node.rest[0] == 1:
      node.dof[0] =M
      M = M + 1

    if node.rest[1] == 1:
      node.dof[1] = M
      M = M + 1

print("N: ", N)
print("M: ", M)



      

  
for id, node in nodes.items():
  print(id, node.id, node.x, node.y, node.rest, node.p, node.dof)
  


# print(row1.id, row1.x, row1.y, row1.rest)
# print(row2.id, row2.x, row2.y, row2.rest)
# print(row3.id, row3.x, row3.y, row3.rest)
# print(row4.id, row4.x, row4.y, row4.rest)
# print(row5.id, row5.x, row5.y, row5.rest)


