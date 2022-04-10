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


elements = dict()

class Element:
  def __init__(self, id, conn, h, E, p):
    self.id = id
    self.conn = conn
    self.h = h 
    self.E = E
    self.p = p 
    elements[id] = self

  def ab(self):
    n1 = nodes[self.conn[0]]
    n2 = nodes[self.conn[1]]
    n3 = nodes[self.conn[2]]
   #n4 = nodes[self.conn[3]]
    a = n2.x - n1.x
    b = n3.y - n1.y
    return a, b 
    
  def code_vec(self):
    n1 = nodes[self.conn[0]]
    n2 = nodes[self.conn[1]]
    n3 = nodes[self.conn[2]]
    n4 = nodes[self.conn[3]]
    return [n1.dof[0], n2.dof[0], n3.dof[0], n4.dof[0],
            n1.dof[1], n2.dof[1], n3.dof[1], n4.dof[1]]
    
  def stiffness_matrix(self):
     a, b = self.ab()
     a2, b2 = a ** 2, b ** 2
     E, p, h = self.E, self.p, self.h
     c1 = E / (1 - p ** 2)
     c2 = E / (2 + 2 * p)
     k0 = h / (12 * a * b)
     k1 = 2 * (a2 * c2 + b2 * c1)
     k2 = 2 * (a2 * c2 - 2 * b2 * c1)
     k3 = 2 * (2 * a2 * c2 - b2 * c1)
     k4 = 2 * (a2 * c1 + b2 * c2)
     k5 = 2 * (a2 * c1 - 2 * b2 * c2)
     k6 = 2 * (2 * a2 * c1 - b2 * c2)
     k7 = 3 * a * b * (c2 + p * c1)
     k8 = 3 * a * b * (c2 - p * c1)
     return k0 * np.asarray([
         [2 * k1, k2, -k3, -k1, k7, -k8, k8, -k7],
         [k2, 2 * k1, -k1, -k3, k8, -k7, k7, -k8],
         [-k3, -k1, 2 * k1, k2, -k8, k7, -k7, k8],
         [-k1, -k3, k2, 2 * k1, -k7, k8, -k8, k7],
         [k7, k8, -k8, -k7, 2 * k4, k5, -k6, -k4],
         [-k8, -k7, k7, k8, k5, 2 * k4, -k4, -k6],
         [k8, k7, -k7, -k8, -k6, -k4, 2 * k4, k5],
         [-k7, -k8, k8, k7, -k4, -k6, k5, 2 * k4]
        ])

Element(id=1, conn=[1,2,6,7], h=0.01, E=70e6, p=0.3)
Element(id=2, conn=[2,3,7,8], h=0.01, E=70e6, p=0.3)
Element(id=3, conn=[3,4,8,9], h=0.01, E=70e6, p=0.3)
Element(id=4, conn=[4,5,9,10], h=0.01, E=70e6, p=0.3)

Element(id=5, conn=[6,7,11,12], h=0.01, E=70e6, p=0.3)
Element(id=6, conn=[7,8,12,13], h=0.01, E=70e6, p=0.3)
Element(id=7, conn=[8,9,13,14], h=0.01, E=70e6, p=0.3)
Element(id=8, conn=[9,10,14,15], h=0.01, E=70e6, p=0.3)

for id, elm in elements.items():
  print(id, elm.conn, elm.h, elm.E, elm.p, elm.ab(), elm.code_vec())

print(elements[1].stiffness_matrix())
