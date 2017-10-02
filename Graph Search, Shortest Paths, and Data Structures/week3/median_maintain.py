from queue import PriorityQueue

class MaintainMedian:

    def __init__(self):
        self.left_half = PriorityQueue()
        self.right_half = PriorityQueue()

    def add(self, num):
        if self.left_half.qsize() <= self.right_half.qsize():
            self.right_half.put((num, num))
            move_to_left = self.right_half.get()
            self.left_half.put((1/move_to_left[0], move_to_left[1]))
        else:
            self.left_half.put((1/num, num))
            move_to_right = self.left_half.get()
            self.right_half.put((1/move_to_right[0], move_to_right[1]))

    def median(self):
        return self.left_half.queue[0]


if __name__ == '__main__':
    mm = MaintainMedian()
    for n in range(1, 100):
        mm.add(n)
        algorithm_result = mm.median()[1]
        correct_result = n // 2 + n % 2
        assert algorithm_result == correct_result

