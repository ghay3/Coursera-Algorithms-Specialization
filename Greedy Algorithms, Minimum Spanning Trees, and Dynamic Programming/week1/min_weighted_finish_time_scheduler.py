from collections import namedtuple

Task = namedtuple('Task', 'weight time func')


class Scheduler:

    def __init__(self, tasks):
        self.tasks = sorted(tasks, key=lambda t: t.weight / t.time, reverse=True)

    def run(self):
        t, finish_time_sum = 0, 0
        for task in self.tasks:
            task.func()
            t += task.time
            finish_time_sum += task.weight * t
        print('weighted finish time:', t)


if __name__ == '__main__':
    tasks = [
        Task(weight=3, time=1, func=lambda: print('1')),
        Task(weight=2, time=2, func=lambda: print('2')),
        Task(weight=1, time=3, func=lambda: print('3')),
    ]
    Scheduler(tasks).run()