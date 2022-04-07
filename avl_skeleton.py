# username - complete info
# id1      - 206484750
# name1    - Guy Reuveni
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0  # Guy added it.

    """returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

    def getLeft(self):
        return self.left

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

    def getRight(self):
        return self.right

    """returns the parent

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

    def getParent(self):
        return self.parent

    """return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""

    def getValue(self):
        return self.value

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

    def getHeight(self):
        return self.height

    """returns the size

	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""

    def getSize(self):  # Guy added it
        return self.size

    """returns the balnce factor

	@rtype: int
	@returns: the balance factor of self
	"""

    # Guy added it. noe sure what to return if the node is virtual.
    def getBf(self):
        return self.left.getHeight() - self.right.getHeight()

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def setLeft(self, node):
        self.left = node

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def setRight(self, node):
        self.right = node

    """sets parent

	@type node: AVLNode
	@param node: a node
	"""

    def setParent(self, node):
        self.parent = node

    """sets value

	@type value: str
	@param value: data
	"""

    def setValue(self, value):
        self.value = value

    """sets the height of the node

	@type h: int
	@param h: the height
	"""

    def setHeight(self, h):
        self.height = h

    """sets the size of the node

	@type size: int
	@param size: the size
	"""

    def setSize(self, size):  # Guy added this method
        self.size = size

    """given that self is an AVL criminal with BF = +2 and its left son has BF = +1,
    fixes the Bf of self. furthermore, updating the height and size fields of the nodes involved
	"""

    def rightRotation(self):  # not handling the root problem yet
        B = self
        parent = B.getParent()
        A = B.getLeft()
        if parent.getLeft() == B:
            parent.setLeft(A)
        else:
            parent.setRight(A)
        A.setParent(parent)
        B.setParent(A)
        B.setLeft(A.getRight())
        A.setRight(B)
        B.getLeft().setParent(B)

        # fixing height field off A and B, the only nodes whose height was changed
        A.setHeight(1 + max(A.left.getHeight() + A.right.getHeight()))
        B.setHeight(1 + max(B.left.getHeight() + B.right.getHeight()))

        # fixing size field off A and B, the only nodes whose size was changed
        A.setSize(B.size)
        B.setSize(1 + B.left.getSize() + B.right.getSize())

    """returns whether self is not a virtual node

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def isRealNode(self):
        if self.height == -1:
            return False
        return True


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):

    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        self.first = None
        self.last = None
        # we should consider adding a length field - Guy thinks that maybe we can be stasfied with the fact that we have a pointer to the root and root's size is the length of the list

    """returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""

    def empty(self):  # better to be implented after we understand how we enter the first element to the list
        return None

    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

    def retrieve(self, i):
        return None

    """inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, i, val):
        return -1

    """deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    # not handling mikrey kastze yet.
    def delete(self, i):
        if i >= self.length():
            return -1

        nodeToBeDeleted = self.treeSelect(i+1)

        if nodeToBeDeleted.getSize() == 1:  # the node is a leaf
            numOfBalancingOpps = deleteLeaf(nodeTobeDeleted)
            return numOfBalancingOpps

        elif not nodeToBeDeleted.getLeft().isRealNode():  # the node has only right child
            numOfBalancingOpps = deleteNodeWithRightChildOnly(nodeToBeDeleted)
            return numOfBalancingOpps

        elif not nodeToBeDeleted.getRight().isRealNode():  # the node has only left child
            numOfBalancingOpps = deleteNodeWithLeftChildOnly(nodeToBeDeleted)
            return numOfBalancingOpps

        else:  # the node has two children
            successor = self.getSuccessorOf(nodeToBeDeleted)
            if successor.size == 1:
                numOfBalancingOpps = deleteLeaf(successor)
            else:
                numOfBalancingOpps = deleteNodeWithRightChildOnly(successor)
            parent = nodeToBeDeleted.getParent()
            leftChild = nodeToBeDeleted.getLeft()
            rightChild = nodeToBeDeleted.getRight()
            if parent.getLeft() == nodeToBeDeleted:
                parent.setLeft(successor)
            else:
                parent.setRight(successor)
            successor.setParent(parent)
            leftChild.setParent(successor)
            successor.setLeft(leftChild)
            rightChild.setParent(successor)
            successor.setRight(rightChild)
            return numOfBalancingOpps

        return -1

        def deleteLeaf(nodeToBeDeleted):
            parent = nodeToBeDeleted.getParent()
            if parent.getLeft() == nodeToBeDeleted:
                parent.setLeft(nodeToBeDeleted.getLeft())
            else:
                parent.setRight(nodeToBeDeleted.getRight())
            nodeToBeDeleted.setParent(None)
            numOfBalancingOpps = fixTreeAfterDeletion(parent)
            return numOfBalancingOpps

        def deleteNodeWithRightChildOnly(nodeToBeDeleted):
            parent = nodeToBeDeleted.getParent()
            child = nodeToBeDeleted.getRight()
            child.setParent(parent)
            if parent.getLeft() == nodeToBeDeleted:
                parent.setLeft(child)
            else:
                parent.setRight(child)
            nodeToBeDeleted.setParent(None)
            nodeToBeDeleted.setRight(None)
            numOfBalancingOpps = fixTreeAfterDeletion(parent)
            return numOfBalancingOpps

        def deleteNodeWithLeftChildOnly(nodeToBeDeleted):
            parent = nodeToBeDeleted.getParent()
            child = nodeToBeDeleted.getLeft()
            child.setParent(parent)
            if parent.getLeft() == nodeToBeDeleted:
                parent.setLeft(child)
            else:
                parent.setRight(child)
            nodeToBeDeleted.setParent(None)
            nodeToBeDeleted.setLeft(None)
            numOfBalancingOpps = fixTreeAfterDeletion(parent)
            return numOfBalancingOpps

        def fixTreeAfterDeletion(node):
            numOfBalancingOpps = 0
            doneWithFixingHeight = False
            while True:
                node.setSize(node.getSize() - 1)
                if not doneWithFixingHeight:
                    BF = node.getBf()
                    heightBefore = node.getHeight()
                    heightAfter = 1 + \
                        max(node.getLeft().getHeight(),
                            node.getRight().getHeight())
                    if abs(Bf) < 2 and heightAfter == heightBefore:
                        doneWithFixingHeight = True

                    elif abs(BF) < 2 and heightAfter != heightBefore:
                        node.setHeight(heightAfter)
                        numOfBalancingOpps += 1
                    else:  # abs(BF) = 2
                        if heightAfter != heightBefore:
                            node.setHeight(heightAfter)
                            numOfBalancingOpps += 1
                        if BF == 2:
                            BFL = node.getLeft().getBf()
                            if BFL == 1 or BFL == 0:
                                node.rightRotation()
                                numOfBalancingOpps += 1
                            elif BFL == - 1:
                                node.leftRotatation()
                                node.rightRotation()
                                numOfBalancingOpps += 2
                        else:  # BF = -2
                            BFR = node.getRight().getBf()
                            if BFR == -1 or BFR == 0:
                                node.leftRotatation()
                                numOfBalancingOpps += 1
                            elif BFR == 1:
                                node.rightRotation()
                                node.leftRotatation()
                                numOfBalancingOpps += 2

                node = node.getParent()

                if node == self.getRoot():
                    break

            return numOfBalancingOpps
    """returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""

    def first(self):
        return self.first.getValue()

    """returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""

    def last(self):
        return self.last.getValue()

    """returns an array representing list

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

    def listToArray(self):
        return None

    """returns the size of the list

	@rtype: int
	@returns: the size of the list
	"""

    def length(self):
        if self.empty():
            return 0
        return getRoot(self).getSize()

    """splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""

    def split(self, i):
        return None

    """concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

    def concat(self, lst):
        return None

    """searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""

    def search(self, val):
        return None

    """returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""

    def getRoot(self):
        return self.root

    # service methods
    """returns the i'th smallest node in the tree

    @type i: int
    @pre: 1 <= i <= self.length()
    @param i: a position in the tree
    @rtype: AVLNode
    @returns: the i'th smallest node in the tree
    @complexity: O(logi)
    """

    def treeSelect(self, i):
        if i == 1:
            return self.first
        if i == self.length():
            return self.last

        curr = self.findSmallestSubTreeOfSize(i)
        r = curr.getLeft().getSize() + 1
        while (i != r):
            if i < r:               # the node is in the left tree so we need to loof for the i'th smallest node in the left tree
                curr = curr.getLeft()

            # the node is in the right tree so we need to look for the (i-r)'th smallest node in the right tree
            else:
                curr = curr.getRight()
                i = i - r
            r = curr.getLeft().getSize() + 1
        return curr

    """returns the smallest node in the tree whose subtree of size >= k

    @type k: int
    @pre: 1 <= k <= self.length()
    @rtype: AVLNode
    @returns: the smallest node off size >= k
    @complexity: O(logk)
    """

    def findSmallestSubTreeOfSize(self, k):
        curr = self.first
        while (curr.getSize() < k):
            curr = curr.getParent()
        return curr

    """returns the successor of a given node

    @type node: AVLNode
	@rtype: AVLNode
	@returns: the successor of a given node. if the node is the Maximum returns None
    complexity: O(logn)
	"""

    def getSuccessorOf(self, node):
        if self.last == node:
            return None

        if node.getRight().isRealNode():
            curr = node.getRight()
            while curr.isRealNode():
                curr = curr.getLeft()
            return curr

        curr = node.getParent()
        while curr.isRealNode and curr.getRight() == node:
            node = curr
            curr = curr.getParent()
        return curr

    # """increases by 1 the size of all the node which are in the path from node to the root

        # @rtype: int
        # @returns: the size of the list
        # """

    # def increaseSizeByOneAllTheWayUpFrom(self, node):
    #     while True:
    #         node.setSize(node.getSize() + 1)
    #         if node == self.getRoot():
    #             break
