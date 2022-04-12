import unittest
from avl_skeleton import AVLTreeList


"""
IN ORDER TO USE THE TEST TOU NEED TO MAKE THE FOLLOWING:
1. IMPLEMENT APPEND METHOD IN AVLTreeList THIS WAY:
def append(self, val):
        self.insert(self.length(), val)
2. YOU NEED TO HAVE FPOINTERS TO FIRST AND LAST ELEMENT
"""


class testAVLList(unittest.TestCase):

    emptyList = AVLTreeList()
    twentyTree = AVLTreeList()
    twentylist = []

    for i in range(20):
        twentylist.append(i)
        twentyTree.append(i)

    def in_order(self, tree, node, func):
        if node.isRealNode():
            self.in_order(tree, node.getLeft(), func)
            func(node, tree)
            self.in_order(tree, node.getRight(), func)

    def compare_with_list_by_in_order(self, tree, lst):
        def rec(node, cnt, lst):
            if node.isRealNode():
                rec(node.getLeft(), cnt, lst)
                self.assertEqual(node.getValue(), lst[cnt[0]])
                cnt[0] += 1
                rec(node.getRight(), cnt, lst)

        cnt = [0]
        rec(tree.getRoot(), cnt, lst)

    def compare_with_list_by_retrieve(self, tree, lst):
        for i in range(max(len(lst), tree.length())):
            self.assertEqual(tree.retrieve(i), lst[i])

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

    ###TESTING INSERTION###

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
            self.compare_with_list_by_in_order(T2, L2)
            self.compare_with_list_by_retrieve(T2, L2)

    def test_insert_at_end_small(self):
        T1 = AVLTreeList()
        L1 = []

        for i in range(3):
            T1.append(i)
            L1.append(i)
            self.compare_with_list_by_in_order(T1, L1)
            self.compare_with_list_by_retrieve(T1, L1)

        for j in range(10, 20):
            T3 = AVLTreeList()
            L3 = []
            for i in range(j):
                T3.insert(T3.length(), i)
                L3.insert(len(L3), i)
                self.compare_with_list_by_retrieve(T3, L3)
                self.compare_with_list_by_in_order(T3, L3)

    def test_insert_at_end_big(self):
        T3 = AVLTreeList()
        L3 = []
        for i in range(100):
            T3.insert(T3.length(), i)
            L3.insert(len(L3), i)
        self.compare_with_list_by_retrieve(T3, L3)
        self.compare_with_list_by_in_order(T3, L3)

    def test_insert_at_the_middle_small(self):
        for j in range(10, 20):
            T = AVLTreeList()
            L = []

            for i in range(j):
                T.insert(i//2, i)
                L.insert(i//2, i)
                self.compare_with_list_by_retrieve(T, L)
                self.compare_with_list_by_in_order(T, L)

    def test_insert_at_the_middle_big(self):
        T4 = AVLTreeList()
        L4 = []

        for i in range(100):
            T4.insert(i//2, i)
            L4.insert(i//2, i)
            self.compare_with_list_by_retrieve(T4, L4)
            self.compare_with_list_by_in_order(T4, L4)

    def test_insert_alternately(self):
        T5 = AVLTreeList()
        L5 = []

        for i in range(100):
            if i % 5 == 0:
                T5.insert(0, i)
                L5.insert(0, i)
            elif i % 5 == 1:
                T5.insert(len(L5), i)
                L5.insert(len(L5), i)
            elif i % 5 == 2:
                T5.insert(i//2, i)
                L5.insert(i//2, i)
            elif i % 5 == 3:
                T5.insert(i//3, i)
                L5.insert(i//3, i)
            else:
                T5.insert(i//7, i)
                L5.insert(i//7, i)
            if i % 10 == 0:
                self.compare_with_list_by_retrieve(T5, L5)
                self.compare_with_list_by_in_order(T5, L5)

    ### TESTING DELETION ### (assuming insertion works perfectly)#
    def test_deleting_not_existing(self):
        self.assertEqual(self.emptyList.delete(0), -1)
        self.assertEqual(self.twentyTree.delete(-1), -1)
        self.assertEqual(self.twentyTree.delete(30), -1)

    def test_delete_list_with_only_one_element(self):
        T = AVLTreeList()
        T.insert(0, 1)
        T.delete(0)
        self.assertIsNone(T.getRoot())
        self.assertIsNone(T.firstItem)
        self.assertIsNone(T.lastItem)

    def test_delete_from_list_with_two_elements(self):
        T1 = AVLTreeList()
        for i in range(2):
            T1.append(i)
        T1.delete(0)

        self.assertEqual(T1.getRoot().getValue(), 1)
        T1.delete(0)
        self.assertIsNone(T1.getRoot())

        T1 = AVLTreeList()
        for i in range(2):
            T1.append(i)
        T1.delete(1)
        self.assertEqual(T1.getRoot().getValue(), 0)
        T1.delete(0)
        self.assertIsNone(T1.getRoot())

        T1 = AVLTreeList()
        for i in range(2):
            T1.append(0)

        T1.delete(0)
        self.assertEqual(T1.getRoot().getValue(), 0)
        T1.delete(0)
        self.assertIsNone(T1.getRoot())

    def test_delete_from_start_small(self):
        for j in range(10, 20):
            T = AVLTreeList()
            L = []
            for i in range(j):
                T.append(i)
                L.append(i)

            while not T.empty():
                self.compare_with_list_by_in_order(T, L)
                self.compare_with_list_by_retrieve(T, L)
                T.delete(0)
                L.pop(0)

        self.assertEqual(len(L), 0)

    def test_delete_from_start_big(self):
        T = AVLTreeList()
        L = []
        for i in range(100):
            T.append(i)
            L.append(i)

        while not T.empty():
            self.compare_with_list_by_in_order(T, L)
            self.compare_with_list_by_retrieve(T, L)
            T.delete(0)
            L.pop(0)

        self.assertEqual(len(L), 0)

    def test_delete_from_end_small(self):
        for j in range(10, 20):
            T = AVLTreeList()
            L = []
            for i in range(j):
                T.append(i)
                L.append(i)

            while not T.empty():
                self.compare_with_list_by_in_order(T, L)
                self.compare_with_list_by_retrieve(T, L)
                T.delete(T.length()-1)
                L.pop(len(L)-1)

            self.assertEqual(len(L), 0)

    def test_delete_from_end_big(self):
        T = AVLTreeList()
        L = []
        for i in range(100):
            T.append(i)
            L.append(i)

        while not T.empty():
            self.compare_with_list_by_in_order(T, L)
            self.compare_with_list_by_retrieve(T, L)
            T.delete(T.length()-1)
            L.pop(len(L)-1)

        self.assertEqual(len(L), 0)

    def test_delete_from_middle_small(self):
        for j in range(10, 20):
            T = AVLTreeList()
            L = []
            for i in range(j):
                T.append(i)
                L.append(i)

            while not T.empty():
                self.compare_with_list_by_in_order(T, L)
                self.compare_with_list_by_retrieve(T, L)
                T.delete(T.length()//2)
                L.pop(len(L)//2)

            self.assertEqual(len(L), 0)

    def test_delete_from_middle_big(self):
        T = AVLTreeList()
        L = []

        for i in range(100):
            T.append(i)
            L.append(i)

        while not T.empty():
            self.compare_with_list_by_in_order(T, L)
            self.compare_with_list_by_retrieve(T, L)
            T.delete(T.length()//2)
            L.pop(len(L)//2)

        self.assertEqual(len(L), 0)

    def test_delete_altenatly(self):
        T = AVLTreeList()
        L = []
        for i in range(100):
            T.append(i)
            L.append(i)
        cnt = 0
        while not T.empty():
            self.compare_with_list_by_in_order(T, L)
            self.compare_with_list_by_retrieve(T, L)
            if cnt % 4 == 0:
                T.delete(T.length()//2)
                L.pop(len(L)//2)
            elif cnt % 4 == 1:
                T.delete(0)
                L.pop(0)
            elif cnt % 4 == 2:
                T.delete(T.length()-1)
                L.pop(len(L)-1)
            else:
                T.delete(T.length()//4)
                L.pop(len(L)//4)
            cnt += 1

        self.assertEqual(len(L), 0)

    ### TESTING INSERTION AND DELETION TOGETHER###

    def test_delete_and_insert_equal_number_of_times_small(self):
        cnt = 1
        T = AVLTreeList()
        for i in range(10):
            T.append(i)

        for i in range(100):
            if cnt % 2 == 0:
                T.insert(cnt % T.length(), i+10)
            else:
                T.delete(cnt % T.length())
            cnt += 17

    def test_delete_and_insert_equal_number_of_times_big(self):
        cnt = 1
        T = AVLTreeList()
        for i in range(100):
            T.append(i)

        for i in range(1000):
            if cnt % 2 == 0:
                T.insert(cnt % T.length(), i+10)
            else:
                T.delete(cnt % T.length())
            cnt += 17

    def test_delete_and_insert_with_more_insertions_small(self):
        T = AVLTreeList()
        T.append(40)
        for i in range(30):
            if (i % 3 != 2):
                T.insert((i*17) % T.length(), i)
            else:
                T.delete((i*17) % T.length())

    def test_delete_and_insert_with_more_insertions_big(self):
        T = AVLTreeList()
        T.append(40)
        for i in range(150):
            if (i % 3 != 2):
                T.insert((i*17) % T.length(), i)
            else:
                T.delete((i*17) % T.length())

    def test_delete_and_insert_altenatly_small(self):
        T = AVLTreeList()
        L = []

        for i in range(20):
            if i % 3 == 0:
                T.insert(T.length()//2, i)
                L.insert(len(L)//2, i)
            elif i % 3 == 1:
                T.insert(0, i)
                L.insert(0, i)
            else:
                T.delete(T.length()//2)
                L.pop(len(L)//2)
            self.compare_with_list_by_in_order(T, L)
            self.compare_with_list_by_retrieve(T, L)

    ### TESTING FAMILTY ### (testing that node == node.getchild.gerparent)#

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
            if i % 5 == 0:
                T5.insert(0, i)
            elif i % 5 == 1:
                T5.insert(T5.length(), i)
            elif i % 5 == 2:
                T5.insert(i//2, i)
            elif i % 5 == 3:
                T5.insert(i//3, i)
            else:
                T5.insert(i//7, i)
            self.in_order(T5, T5.getRoot(), self.check_family)

    def test_family_after_deletion_alternatly(self):
        T = AVLTreeList()

        for i in range(100):
            T.insert(0, i)

        for i in range(99):
            if i % 5 == 0:
                T.delete(0)
            elif i % 5 == 1:
                T.delete(T.length()-1)
            elif i % 5 == 2:
                T.delete((T.length()-1)//2)
            elif i % 5 == 3:
                T.delete((T.length()-1)//3)
            else:
                T.delete((T.length()-1)//7)
            self.in_order(T, T.getRoot(), self.check_family)

    def test_family_after_deleting_and_inserting_small(self):
        T = AVLTreeList()

        for i in range(20):
            if i % 3 == 0:
                T.insert(T.length()//2, i)
            elif i % 3 == 1:
                T.insert(0, i)
            else:
                T.delete(T.length()//2)
            self.in_order(T, T.getRoot(), self.check_family)

    def test_family_after_deleting_and_inserting_big(self):
        T = AVLTreeList()

        for i in range(500):
            if i % 3 == 0:
                T.insert(T.length()//2, i)
            elif i % 3 == 1:
                T.insert(0, i)
            else:
                T.delete(T.length()//2)
            self.in_order(T, T.getRoot(), self.check_family)

    ###TESTING SIZE###

    def check_size(self, node, tree):
        self.assertEqual(node.getSize(), node.getLeft(
        ).getSize() + node.getRight().getSize() + 1)

    def test_size_after_insertion_at_start(self):
        T2 = AVLTreeList()

        for i in range(50):
            T2.insert(0, i)
            self.in_order(T2, T2.getRoot(), self.check_size)

    def test_size_after_deletion_from_start(self):
        T = AVLTreeList()
        for i in range(50):
            T.insert(0, i)

        for i in range(49):
            T.delete(0)
            self.in_order(T, T.getRoot(), self.check_size)

    def test_size_after_insertion_at_end(self):
        T3 = AVLTreeList()

        for i in range(50):
            T3.insert(T3.length(), i)
            self.in_order(T3, T3.getRoot(), self.check_size)

    def test_size_after_deletion_from_end(self):
        T3 = AVLTreeList()

        for i in range(50):
            T3.insert(T3.length(), i)

        for i in range(49):
            T3.delete(T3.length()-1)
            self.in_order(T3, T3.getRoot(), self.check_size)

    def test_size_after_insertion_at_middle(self):
        T4 = AVLTreeList()

        for i in range(50):
            T4.insert(i//2, i)
            self.in_order(T4, T4.getRoot(), self.check_size)

    def test_size_after_deletion_from_middle(self):
        T3 = AVLTreeList()

        for i in range(50):
            T3.insert(0, i)

        for i in range(49):
            T3.delete(i//2)
            self.in_order(T3, T3.getRoot(), self.check_size)

    def test_size_after_insertion_alternatly(self):
        T5 = AVLTreeList()

        for i in range(200):
            if i % 5 == 0:
                T5.insert(0, i)
            elif i % 5 == 1:
                T5.insert(T5.length(), i)
            elif i % 5 == 2:
                T5.insert(i//2, i)
            elif i % 5 == 3:
                T5.insert(i//3, i)
            else:
                T5.insert(i//7, i)
            self.in_order(T5, T5.getRoot(), self.check_size)

    def test_size_after_deletion_alternatly(self):
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
            self.in_order(T, T.getRoot(), self.check_size)

    def test_size_after_deleting_and_inserting_small(self):
        T = AVLTreeList()

        for i in range(20):
            if i % 3 == 0:
                T.insert(T.length()//2, i)
            elif i % 3 == 1:
                T.insert(0, i)
            else:
                T.delete(T.length()//2)
            self.in_order(T, T.getRoot(), self.check_size)

    def test_size_after_deleting_and_inserting_big(self):
        T = AVLTreeList()

        for i in range(500):
            if i % 3 == 0:
                T.insert(T.length()//2, i)
            elif i % 3 == 1:
                T.insert(0, i)
            else:
                T.delete(T.length()//2)
            self.in_order(T, T.getRoot(), self.check_size)
