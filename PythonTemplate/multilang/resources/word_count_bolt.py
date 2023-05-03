import storm
from collections import Counter


class CountBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")

        if not hasattr(self, 'counts'):
            self.counts = Counter()
        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        word = tup.values[0]
        self.counts[word] += 1
        storm.logInfo("count of {}: {}".format(word, self.counts[word]))
        storm.emit([word, self.counts[word]])


# Start the bolt when it's invoked
CountBolt().run()
