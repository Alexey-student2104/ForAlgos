import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root

        while True:
            if key == current.key:
                return

            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

    def exists(self, key):
        current = self.root

        while current is not None:
            if current.key == key:
                return True

            if key < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, key):
        parent = None
        current = self.root

        while current is not None and current.key != key:
            parent = current

            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is not None and current.right is not None:
            successor_parent = current
            successor = current.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current.key = successor.key
            parent = successor_parent
            current = successor

        child = current.left if current.left is not None else current.right

        if parent is None:
            self.root = child
        elif parent.left is current:
            parent.left = child
        else:
            parent.right = child

    def height(self):
        if self.root is None:
            return 0

        result = 0
        stack = [(self.root, 1)]

        while stack:
            node, depth = stack.pop()
            result = max(result, depth)

            if node.left is not None:
                stack.append((node.left, depth + 1))

            if node.right is not None:
                stack.append((node.right, depth + 1))

        return result

    def print_tree(self):
        if self.root is None:
            return "Empty"

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
    q = int(input())
    tree = BST()
    output = []

    for _ in range(q):
        command = input().split()

        if not command:
            continue

        operation = command[0]

        if operation == "add":
            tree.add(int(command[1]))
        elif operation == "del":
            tree.delete(int(command[1]))
        elif operation == "exists":
            output.append("YES" if tree.exists(int(command[1])) else "NO")
        elif operation == "height":
            output.append(str(tree.height()))
        elif operation == "print":
            output.append(tree.print_tree())

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
