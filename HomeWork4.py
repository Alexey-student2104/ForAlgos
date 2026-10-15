import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(
            self._height(node.left),
            self._height(node.right)
        )

    def _balance_factor(self, node):
        return self._height(node.right) - self._height(node.left)

    def _rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node

        self._update_height(node)
        self._update_height(right)

        return right

    def _rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node

        self._update_height(node)
        self._update_height(left)

        return left

    def _balance(self, node):
        self._update_height(node)
        factor = self._balance_factor(node)

        if factor == 2:
            if self._balance_factor(node.right) < 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        if factor == -2:
            if self._balance_factor(node.left) > 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        return node

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        return self._balance(node)

    def add(self, key):
        self.root = self._insert(self.root, key)

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._find_min(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return self._balance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def exists(self, key):
        node = self.root

        while node is not None:
            if key == node.key:
                return True
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return False

    def next_val(self, key):
        node = self.root
        result = None

        while node is not None:
            if node.key >= key:
                result = node.key
                node = node.left
            else:
                node = node.right

        return result

    def prev_val(self, key):
        node = self.root
        result = None

        while node is not None:
            if node.key <= key:
                result = node.key
                node = node.right
            else:
                node = node.left

        return result

    def get_root(self):
        return self.root.key if self.root is not None else "Empty"

    def get_height(self):
        return self._height(self.root)

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

    tree = AVLTree()
    output = []

    for _ in range(q):
        parts = input().split()

        if not parts:
            continue

        command = parts[0]

        if command == "add":
            tree.add(int(parts[1]))
        elif command == "del":
            tree.delete(int(parts[1]))
        elif command == "exists":
            output.append(
                "YES" if tree.exists(int(parts[1])) else "NO"
            )
        elif command == "next":
            result = tree.next_val(int(parts[1]))
            output.append(str(result) if result is not None else "None")
        elif command == "prev":
            result = tree.prev_val(int(parts[1]))
            output.append(str(result) if result is not None else "None")
        elif command == "root":
            output.append(str(tree.get_root()))
        elif command == "height":
            output.append(str(tree.get_height()))
        elif command == "print":
            output.append(tree.print_tree())

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()