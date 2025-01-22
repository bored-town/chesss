import random

class BalancedShuffler:
    def __init__(self, numbers):
        self.numbers = numbers
        self.queue = []
        self._reshuffle()

    def _reshuffle(self):
        self.queue = self.numbers[:]
        random.shuffle(self.queue)

    def get_next(self):
        if not self.queue:
            self._reshuffle()
        return self.queue.pop(0)
