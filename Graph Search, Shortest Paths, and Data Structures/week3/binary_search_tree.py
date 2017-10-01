class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.size = (left.size if left else 0) + \
                    (right.size if right else 0) + 1

    def update_size(self):
        self.size = (self.left.size if self.left else 0) + \
                    (self.right.size if self.right else 0) + 1


# https://en.wikipedia.org/wiki/Binary_search_tree
class BST:
    def __init__(self):
        self.root = None

    def add(self, key, val):

        def _add(cur, k, v):
            if not cur:
                return Node(key, val)

            if k < cur.key:
                cur.left = _add(cur.left, k, v)
            else:
                cur.right = _add(cur.right, k, v)
            cur.update_size()

            return cur
        self.root = _add(self.root, key, val)

    def get(self, key):
        return self._get(self.root, key).val

    def _get(self, cur, k):
        if not cur:
            return None

        if k < cur.key:
            return self._get(cur.left, k)
        elif k > cur.key:
            return self._get(cur.right, k)
        else:
            return cur

    def size(self):
        return self.root.size if self.root else 0

    def min(self):

        def _min(cur):
            if cur.left:
                return _min(cur.left)
            else:
                return cur
        node = _min(self.root)
        return (node.key, node.val) if node else None

    def max(self):
        if not self.root:
            return None
        else:
            node = self._max(self.root)
            return node.key, node.val

    def _max(self, cur):
        if cur.right:
            return self._max(cur.right)
        else:
            return cur

    def predecessor(self, key):

        def _predecessor(cur, valid_nearest_parent):
            if not cur:
                return valid_nearest_parent

            if key == cur.key:
                if cur.left:
                    return self._max(cur.left)
                else:
                    return valid_nearest_parent
            elif key < cur.key:
                return _predecessor(cur.left, valid_nearest_parent=valid_nearest_parent)
            else:
                return _predecessor(cur.right, valid_nearest_parent=cur)
        node = _predecessor(self.root, None)
        return (node.key, node.val) if node else None

    def get_ith(self, i):
        """index starts from 1"""
        def _get_ith(cur, n):
            if not cur:
                return None
            left_size = cur.left.size if cur.left else 0
            if left_size < n - 1:
                return _get_ith(cur.right, n-left_size-1)
            elif left_size == n - 1:
                return cur
            else:
                return _get_ith(cur.left, n)
        node = _get_ith(self.root, i)
        return (node.key, node.val) if node else None

    def rank(self, key):
        """rank starts from 1"""
        def _rank(cur, n):
            if not cur:
                return None

            if key < cur.key:
                return _rank(cur.left, n)
            elif key == cur.key:
                return (cur.left.size if cur.left else 0) + n + 1
            else:
                return _rank(cur.right, (cur.left.size if cur.left else 0) + n + 1)
        return _rank(self.root, 0)

    def delete(self, key):

        def _delete(cur, k):
            if not cur:
                return None

            if k < cur.key:
                cur.left = _delete(cur.left, k)
            elif k > cur.key:
                cur.right = _delete(cur.right, k)
            else:
                if not cur.left:
                    return cur.right
                if not cur.right:
                    return cur.left
                left_max = self._max(cur.left)
                cur.left = _delete(cur.left, left_max.key)
                cur.key, cur.val = left_max.key, left_max.val

            cur.update_size()
            return cur
        _delete(self.root, key)


if __name__ == '__main__':
    #      3
    #    /   \
    #   1     5
    #    \   /
    #     2 4
    bst = BST()
    bst.add(3, 'three')
    bst.add(1, 'one')
    bst.add(2, 'two')
    bst.add(5, 'five')
    bst.add(4, 'four')

    assert bst.root.key == 3 and bst.root.size == 5
    assert bst.root.left.key == 1 and bst.root.left.size == 2
    assert bst.root.left.right.key == 2 and bst.root.left.right.size == 1
    assert bst.root.right.key == 5 and bst.root.right.size == 2
    assert bst.root.right.left.key == 4 and bst.root.right.left.size == 1

    assert bst.get(1) == 'one'
    assert bst.get(2) == 'two'
    assert bst.get(3) == 'three'
    assert bst.get(4) == 'four'
    assert bst.get(5) == 'five'

    assert bst.min() == (1, 'one')
    assert bst.max() == (5, 'five')

    assert bst.predecessor(1) is None
    assert bst.predecessor(2) == (1, 'one')
    assert bst.predecessor(3) == (2, 'two')
    assert bst.predecessor(4) == (3, 'three')
    assert bst.predecessor(5) == (4, 'four')

    assert bst.get_ith(1) == (1, 'one')
    assert bst.get_ith(2) == (2, 'two')
    assert bst.get_ith(3) == (3, 'three')
    assert bst.get_ith(4) == (4, 'four')
    assert bst.get_ith(5) == (5, 'five')

    assert bst.rank(1) == 1
    assert bst.rank(2) == 2
    assert bst.rank(3) == 3
    assert bst.rank(4) == 4
    assert bst.rank(5) == 5

    import copy
    trees = [copy.deepcopy(bst) for _ in range(5)]

    bst = trees[0]
    bst.delete(1)
    assert bst.root.key == 3 and bst.root.size == 4
    assert bst.root.left.key == 2 and bst.root.left.size == 1
    assert bst.root.right.key == 5 and bst.root.right.size == 2
    assert bst.root.right.left.key == 4 and bst.root.right.left.size == 1

    bst = trees[1]
    bst.delete(2)
    assert bst.root.key == 3 and bst.root.size == 4
    assert bst.root.left.key == 1 and bst.root.left.size == 1
    assert bst.root.right.key == 5 and bst.root.right.size == 2
    assert bst.root.right.left.key == 4 and bst.root.right.left.size == 1

    bst = trees[2]
    bst.delete(3)
    assert bst.root.key == 2 and bst.root.size == 4
    assert bst.root.left.key == 1 and bst.root.left.size == 1
    assert bst.root.right.key == 5 and bst.root.right.size == 2
    assert bst.root.right.left.key == 4 and bst.root.right.left.size == 1

    bst = trees[3]
    bst.delete(4)
    assert bst.root.key == 3 and bst.root.size == 4
    assert bst.root.left.key == 1 and bst.root.left.size == 2
    assert bst.root.left.right.key == 2 and bst.root.left.right.size == 1
    assert bst.root.right.key == 5 and bst.root.right.size == 1

    bst = trees[4]
    bst.delete(5)
    assert bst.root.key == 3 and bst.root.size == 4
    assert bst.root.left.key == 1 and bst.root.left.size == 2
    assert bst.root.left.right.key == 2 and bst.root.left.right.size == 1
    assert bst.root.right.key == 4 and bst.root.right.size == 1