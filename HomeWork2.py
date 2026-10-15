import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root

        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    current.left.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    current.right.parent = current
                    return
                current = current.right

    def find(self, key):
        current = self.root

        while current is not None:
            if current.key == key:
                return current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    def rotate_left(self, key):
        a = self.find(key)

        if a is None or a.right is None:
            return

        b = a.right
        parent = a.parent

        a.right = b.left
        if b.left is not None:
            b.left.parent = a

        b.left = a
        a.parent = b

        b.parent = parent

        if parent is None:
            self.root = b
        elif parent.left is a:
            parent.left = b
        else:
            parent.right = b

    def rotate_right(self, key):
        a = self.find(key)

        if a is None or a.left is None:
            return

        b = a.left
        parent = a.parent

        a.left = b.right
        if b.right is not None:
            b.right.parent = a

        b.right = a
        a.parent = b

        b.parent = parent

        if parent is None:
            self.root = b
        elif parent.left is a:
            parent.left = b
        else:
            parent.right = b

    def preorder(self):
        if self.root is None:
            return ""

        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(str(node.key))

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return " ".join(result)


def main():
    input = sys.stdin.readline

    n = int(input())
    keys = list(map(int, input().split()))
    m = int(input())

    tree = BST()

    for key in keys:
        tree.add(key)

    output = []

    for _ in range(m):
        command, key = input().split()
        key = int(key)

        if command == "left":
            tree.rotate_left(key)
        else:
            tree.rotate_right(key)

        output.append(tree.preorder())

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
