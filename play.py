from avl_skeleton import AVLTreeList

T = AVLTreeList()

for i in range(10):
    T.append(i)

L = T.split(5)

L[0].printt()
print(L[1])
L[2].printt()
