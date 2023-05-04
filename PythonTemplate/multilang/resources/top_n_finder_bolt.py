import heapq
from collections import Counter

import storm


class TopNFinderBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")

        # TODO:
        # Task: set N
        self._N = 10
        self._top_N = []
        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        '''
        TODO:
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
              the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
        '''
        # End
        word, count = tup.values
        counter = Counter({word: count})

        # Add the new word to the top N list
        for w, freq in counter.items():
            if len(self._top_N) < self._N:
                heapq.heappush(self._top_N, (freq, w))
            elif freq > self._top_N[0][0]:
                heapq.heappushpop(self._top_N, (freq, w))

        # Emit the current top N words
        if len(self._top_N) == self._N:
            top_words = ", ".join([tup[1] for tup in sorted(self._top_N, reverse=True)])
            storm.logInfo("count of {}".format(top_words))
            storm.emit([top_words])


# Start the bolt when it's invoked
TopNFinderBolt().run()
