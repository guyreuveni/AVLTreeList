from avl_skeleton import AVLTreeList
import random


def count_insertions():
    for i in range(1, 11):
        cnt = 0

        T = AVLTreeList()
        for j in range(1000*(2**i)):
            index = random.randint(0, T.length())
            add = T.insert(index, 17)
            cnt = cnt + add

        print("for i = " + str(i) + " : " + str(cnt))


def count_deletions():
    for i in range(1, 11):
        cnt = 0

        T = AVLTreeList()
        for j in range(1000*(2**i)):
            index = random.randint(0, T.length())
            T.insert(index, 17)

        for j in range(1000*(2**i)):
            index = random.randint(0, T.length()-1)
            add = T.delete(index)
            cnt = cnt + add

        print("for i = " + str(i) + " : " + str(cnt))


def count_deletetion_and_insertions():
    for i in range(1, 11):
        cnt = 0

        T = AVLTreeList()
        for j in range((1000*(2**i))//2):
            index = random.randint(0, T.length())
            T.insert(index, 17)

        for j in range((1000*(2**i))//2):
            if j % 2 == 0:
                index = random.randint(0, T.length())
                add = T.insert(index, 17)
                cnt = cnt + add
            else:
                index = random.randint(0, T.length()-1)
                add = T.delete(index)
                cnt = cnt + add

        print("for i = " + str(i) + " : " + str(cnt))


def count_joins():
    for i in range(1, 11):
        random_tree = AVLTreeList()
        max_tree = AVLTreeList()

        for j in range(1000*(2**i)):
            index = random.randint(0, random_tree.length())
            random_tree.insert(index, 17)
            max_tree.insert(index, 17)

        h = max_tree.getRoot().getRight().getHeight()
        res_split_random = random_tree.split(
            random.randint(0, random_tree.length()))
        res_split_max = max_tree.split(
            max_tree.getRoot().getLeft().getSize()-1)

        print("for i = " + str(i))
        avg_cost_random = res_split_random[4]
        print("the averege cost of join operation in random index split is :" +
              str(avg_cost_random))
        max_cost_random = res_split_random[3]
        print("the max cost of join operation in random index split is :" +
              str(max_cost_random))
        print("the right tree height is :" + str(h))

        avg_cost_max = res_split_max[4]
        print("the averege cost of join operation in max left index split is :" + str(avg_cost_max))
        max_cost_max = res_split_max[3]
        print("the max cost of join operation in max left index split is :" + str(max_cost_max))
        print("")


count_deletetion_and_insertions()
