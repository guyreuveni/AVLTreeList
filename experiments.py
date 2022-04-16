from avl_skeleton import AVLTreeList
from not_avl import TreeList
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


def insert_at_start():
    for i in range(1, 11):
        avl_balance_cnt = 0
        regular_balance_cnt = 0
        avl_depth_cnt = 0
        regular_depth_cnt = 0
        avl = AVLTreeList()
        regular = TreeList()

        n = 1000*i

        for j in range(n):
            avl_add_balnce, avl_add_depth = avl.insert(0, 17)
            avl_balance_cnt += avl_add_balnce
            avl_depth_cnt += avl_add_depth
            reg_add_balnce, reg_add_depth = regular.insert(0, 17)
            regular_balance_cnt += reg_add_balnce
            regular_depth_cnt += reg_add_depth

        avl_avg_balance = avl_balance_cnt/n
        avl_avg_depth = avl_depth_cnt/n

        reg_avg_balance = regular_balance_cnt/n
        reg_avg_depth = regular_depth_cnt/n

        print("for i = " + str(i))
        print("balancig operations avarage for avl is: " + str(avl_avg_balance))
        print("balancig operations avarage for regular is: " + str(reg_avg_balance))
        print("")
        print("avarge depth for avl is: " + str(avl_avg_depth))
        print("avarge depth for regular is: " + str(reg_avg_depth))
        print("")
        print("")


def indices():
    i = 2
    while True:
        for j in range(i):
            if j % 2 == 0:
                yield j
        i = i * 2


def insert_balance_tree():
    for i in range(1, 11):
        avl_balance_cnt = 0
        regular_balance_cnt = 0
        avl_depth_cnt = 0
        regular_depth_cnt = 0
        avl = AVLTreeList()
        regular = TreeList()

        n = 1000*i

        gen = indices()

        cnt = 0

        while cnt < n:
            index = next(gen)
            avl_add_balnce, avl_add_depth = avl.insert(index, 17)
            avl_balance_cnt += avl_add_balnce
            avl_depth_cnt += avl_add_depth
            reg_add_balnce, reg_add_depth = regular.insert(index, 17)
            regular_balance_cnt += reg_add_balnce
            regular_depth_cnt += reg_add_depth
            cnt += 1

        avl_avg_balance = avl_balance_cnt/n
        avl_avg_depth = avl_depth_cnt/n

        reg_avg_balance = regular_balance_cnt/n
        reg_avg_depth = regular_depth_cnt/n

        print("for i = " + str(i))
        print("balancig operations avarage for avl is: " + str(avl_avg_balance))
        print("balancig operations avarage for regular is: " + str(reg_avg_balance))
        print("")
        print("avarge depth for avl is: " + str(avl_avg_depth))
        print("avarge depth for regular is: " + str(reg_avg_depth))
        print("")
        print("")


def insert_random():
    for i in range(1, 11):
        avl_balance_cnt = 0
        regular_balance_cnt = 0
        avl_depth_cnt = 0
        regular_depth_cnt = 0
        avl = AVLTreeList()
        regular = TreeList()

        n = 100000*i

        for j in range(n):
            index = random.randint(0, avl.length())
            avl_add_balnce, avl_add_depth = avl.insert(index, 17)
            avl_balance_cnt += avl_add_balnce
            avl_depth_cnt += avl_add_depth
            reg_add_balnce, reg_add_depth = regular.insert(index, 17)
            regular_balance_cnt += reg_add_balnce
            regular_depth_cnt += reg_add_depth

        avl_avg_balance = avl_balance_cnt/n
        avl_avg_depth = avl_depth_cnt/n

        reg_avg_balance = regular_balance_cnt/n
        reg_avg_depth = regular_depth_cnt/n

        print("for i = " + str(i))
        print("balancig operations avarage for avl is: " + str(avl_avg_balance))
        print("balancig operations avarage for regular is: " + str(reg_avg_balance))
        print("")
        print("avarge depth for avl is: " + str(avl_avg_depth))
        print("avarge depth for regular is: " + str(reg_avg_depth))
        print("")
        print("")


insert_random()
