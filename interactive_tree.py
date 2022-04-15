from avl_skeleton import AVLTreeList


def interactive_tree():
    T = AVLTreeList()
    while True:
        choice = input("choose an operation you want to do with your AVLTreeList from the following: \n \
            empty(), retrieve(i), insert(i,val) delete(i),\n\
            first(), last(), listToArray(), length(),\n\
            split(i), concat, search(val) .\n\
            if you want to exit enter 'exit'\n\
            enter your choice here:  ")
        if choice == "exit":
            print("bye bye")
            break
        elif choice == "empty()":
            if T.empty():
                print("your AVLTreeList is empty")
            else:
                print("your AVLTreeList is not empty")
        elif choice[:8] == "retrieve":
            print("the value in index " +
                  str(choice[9:-1]) + " is: " + str(T.retrieve(int(choice[9:-1]))))
        elif choice[:6] == "insert":
            lst = choice.split(",")
            index = int(lst[0][7:])
            val = lst[1][:-1]
            T.insert(index, val)
            print("if '" + str(index) + "' was a valid index, the " +
                  str(index) + "'th item in the list is now '" + val+"'")

        elif choice[:6] == "delete":
            index = int(choice[7:-1])
            T.delete(index)
            print("if '" + str(index) + "' was a valid index, the " +
                  str(index) + "'th item in the list had been deleted")
        elif choice == "first()":
            print("the first item in the list is: " + str(T.first()))
        elif choice == "last()":
            print("the last item in the list is: " + str(T.last()))
        elif choice == "listToArray()":
            print("your list as an array: ")
            print(T.listToArray())
        elif choice == "length()":
            print("the length of your list is: " + str(T.length()))
        elif choice[:5] == "split":
            index = int(choice[6:-1])
            res = T.split(index)
            T1 = res[0]
            val = res[1]
            T2 = res[2]
            ans = input(
                "if you want to print the tree representing the first list enter 'yes'\n\
                    enter your choice here:  ")
            if ans == "yes":
                T1.printt()
                print(T1.listToArray())
            ans = input("if you want to print the value of the " +
                        str(index) + "'th index enter 'yes'\n\
                            enter your choice here:  ")
            if ans == "yes":
                print(val)
            ans = input(
                "if you want to print the tree representing the second list enter 'yes'\n\
                enter your choice here:  ")
            if ans == "yes":
                T2.printt()
                print(T2.listToArray())
            while True:
                ans = input(
                    "enter '1' if you want to keep working with the first list \n\
                    enter '2' if you want to keep working with the second list \n\
                    enter 'exit' if you want to exit\n\
                    enter your choice here:  ")
                if ans == "1":
                    T = T1
                    break
                elif ans == "2":
                    T = T2
                    break
                elif ans == "exit":
                    print("bye bye")
                    return
                else:
                    print("please enter a valid input")
        elif choice == "concat":
            lst = input(
                "enter a sequence of values you want to create a new AVLTreeList that will be concatenated to \n\
                your tree in the following format: \n\
                val1,val2,val3,....,valn\n\
                enter your sequence here: \n").split(",")
            L = AVLTreeList()
            for val in lst:
                L.insert(L.length(), val)
            print("the avlTreeList that had been concatenated to your list is: ")
            L.printt()
            print(L.listToArray())
            T.concat(L)
        elif choice[:6] == "search":
            val = choice[7:-1]
            index = T.search(val)
            if index == -1:
                print(val + " is not in your list")
            else:
                print(val + " is in the " + str(index) +
                      "'th index in your list")
        else:
            print("please enter a valid input")
        ans = input(
            "enter 'yes' if you want to print your AVLTreeList\n\
            enter your choice here:  ")
        if ans == "yes":
            T.printt()
            print(T.listToArray())


interactive_tree()
