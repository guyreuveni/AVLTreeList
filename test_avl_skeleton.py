import unittest
from avl_skeleton import AVLTreeList


class testAVLList(unittest.TestCase):

    emptyList = AVLTreeList()
    twentyTree = AVLTreeList()
    twentylist = []

    for i in range(20):
        twentylist.append(i)
        twentyTree.insert(twentyTree.length(), i)

    def in_order(self, tree, node, func):
        if node.isRealNode():
            self.in_order(tree, node.getLeft(), func)
            func(node, tree)
            self.in_order(tree, node.getRight(), func)

    def test_empty(self):
        self.assertTrue(self.emptyList.empty())
        self.assertFalse(self.twentyTree.empty())

    def test_retrieve_basic(self):
        self.assertIsNone(self.emptyList.retrieve(0))
        self.assertIsNone(self.emptyList.retrieve(59))
        self.assertIsNone(self.twentyTree.retrieve(30))
        self.assertIsNone(self.twentyTree.retrieve(-1))
        for i in range(20):
            self.assertEqual(self.twentylist[i], self.twentyTree.retrieve(i))

    def test_insertBasic(self):
        T1 = AVLTreeList()
        T1.insert(0, 1)
        self.assertEqual(T1.getRoot().getValue(), 1)

    def test_insert_at_start(self):
        # inserts at start
        T2 = AVLTreeList()
        L2 = []

        for i in range(50):
            T2.insert(0, i)
            L2.insert(0, i)

        for i in range(50):
            self.assertEqual(T2.retrieve(i), L2[i])

    def test_insert_at_end(self):
        # inserts at end
        T3 = AVLTreeList()
        L3 = []

        for i in range(50):
            T3.insert(T3.length(), i)
            L3.insert(len(L3), i)

        for i in range(50):
            self.assertEqual(T3.retrieve(i), L3[i])

    def test_insert_at_the_middle(self):

        # inserts in the middle
        T4 = AVLTreeList()
        L4 = []

        for i in range(50):
            T4.insert(i//2, i)
            L4.insert(i//2, i)

        for i in range(len(L4)):
            self.assertEqual(T4.retrieve(i), L4[i])

    def test_insert_alternately(self):
        # inserts alternately
        T5 = AVLTreeList()
        L5 = []

        for i in range(200):
            if i//5 == 0:
                T5.insert(0, i)
                L5.insert(0, i)
            elif i//5 == 1:
                T5.insert(len(L5), i)
                L5.insert(len(L5), i)
            elif i//5 == 2:
                T5.insert(i//2, i)
                L5.insert(i//2, i)
            elif i//5 == 3:
                T5.insert(i//3, i)
                L5.insert(i//3, i)
            else:
                T5.insert(i//7, i)
                L5.insert(i//7, i)
        for i in range(len(L5)):
            self.assertEqual(T5.retrieve(i), L5[i])

    def check_family(self, node, tree):
        self.assertEqual(node, node.getLeft().getParent())
        self.assertEqual(node, node.getRight().getParent())

    def test_family_basic(self):
        self.in_order(self.twentyTree, self.twentyTree.getRoot(),
                      self.check_family)

        self.assertIsNone(self.twentyTree.getRoot().getParent())

    def test_family_after_insertion_at_start(self):
        T2 = AVLTreeList()

        for i in range(50):
            T2.insert(0, i)
            self.in_order(T2, T2.getRoot(), self.check_family)

    def test_family_after_deletion_from_start(self):
        T = AVLTreeList()
        for i in range(50):
            T.insert(0, i)

        for i in range(49):
            T.delete(0)
            self.in_order(T, T.getRoot(), self.check_family)

    def test_family_after_insertion_at_end(self):
        T3 = AVLTreeList()

        for i in range(50):
            T3.insert(T3.length(), i)
            self.in_order(T3, T3.getRoot(), self.check_family)

    def test_family_after_deletion_from_end(self):
        T3 = AVLTreeList()

        for i in range(50):
            T3.insert(T3.length(), i)

        for i in range(49):
            T3.delete(T3.length()-1)
            self.in_order(T3, T3.getRoot(), self.check_family)

    def test_family_after_insertion_at_middle(self):
        T4 = AVLTreeList()

        for i in range(50):
            T4.insert(i//2, i)
            self.in_order(T4, T4.getRoot(), self.check_family)

    def test_family_after_deletion_from_middle(self):
        T3 = AVLTreeList()

        for i in range(50):
            T3.insert(0, i)

        for i in range(49):
            T3.delete(i//2)
            self.in_order(T3, T3.getRoot(), self.check_family)

    def test_family_after_insertion_alternatly(self):
        T5 = AVLTreeList()

        for i in range(200):
            if i//5 == 0:
                T5.insert(0, i)
            elif i//5 == 1:
                T5.insert(T5.length(), i)
            elif i//5 == 2:
                T5.insert(i//2, i)
            elif i//5 == 3:
                T5.insert(i//3, i)
            else:
                T5.insert(i//7, i)
            self.in_order(T5, T5.getRoot(), self.check_family)

    def test_family_after_deletion_alternatly(self):
        T = AVLTreeList()

        for i in range(100):
            T.insert(0, i)

        for i in range(99):
            if i//5 == 0:
                T.delete(0)
            elif i//5 == 1:
                T.delete(T.length()-1)
            elif i//5 == 2:
                T.delete((T.length()-1)//2)
            elif i//5 == 3:
                T.delete((T.length()-1)//3)
            else:
                T.delete((T.length()-1)//7)
            self.in_order(T, T.getRoot(), self.check_family)
