ex = [1, 1, 1, 1, 1, 1]
ex2 = [[1], [1], [1], [1]]
ex3 = [2, 2, 1, 2, 2, 2]


def length(l):
    if l == []:
        return 0
    else:
        return 1 + length(l[1:])


def suma(l):
    if l == []:
        return 0
    else:
        x = l.pop(0)
        return x + suma(l)


def concat(l):
    if l == []:
        return []
    else:
        x = l.pop(0)
        return x + concat(l)


def ani(c, l):
    if l == []:
        return False
    else:
        x = l.pop(0)
        return c(x) or ani(c, l)


def condition(i):
    return i == 1


print(ani(condition, ex3))


class Node():
    def __init__(self, left, right, val):
        self.value = val
        self.left = left
        self.right = right


def sizeT(node: Node):
    if node.value == 0:
        return 0
    else:
        return 1 + sizeT(node.left) + sizeT(node.right)


exTree = Node(1, 0, 2)

print(sizeT(exTree))
