from avl_skeleton import AVLTreeList
import random as random

L = AVLTreeList()


for i in range(5):
    L.insert(i, i)
L.printt()

L.delete(3)
L.printt()
L.delete(3)
L.printt()
