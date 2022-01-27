import storm
import redis

class WordCountStoreBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._redis = conf.get("redis")  # retrive redis configuration into a dictonary
        storm.logInfo("Word Count Store bolt instance starting...")

        # TODO
        # Create a redis.StrictRedis instance using the redis configuration in self._redis
        # Hint: Add necessary instance variables and classes if needed


    def process(self, tup):
        # TODO 
        # Task: save word count pair to redis under the specified hash name
        pass
        # End

# Start the bolt when it's invoked
WordCountStoreBolt().run()
