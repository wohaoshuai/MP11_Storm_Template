import storm
import redis


class TopNStoreBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        # redis configuration converted into a dictonary
        self._redis_conf = conf.get("redis")  # redis configuration converted into a dictonary
        storm.logInfo("Top N Store bolt instance starting...")

        # TODO
        # Connect to Redis using redis.Redis() with redis configuration in self._redis dictionary
        # Hint: Add necessary instance variables and classes if needed
        self._redis = redis.Redis(
            host=self._redis_conf['host'],
            port=self._redis_conf['port'],
            db=self._redis_conf['db'],
            password=self._redis_conf.get('password'),
        )
        

    def process(self, tup):
        # TODO
        # Task: save the top-N word to redis under the specified hash name
        top_N_words = tup.values[0]
        self._redis.hset("partDTopN", "top-N", top_N_words)

        storm.logInfo("Saved top-N words %s to Redis", top_N_words)

# Start the bolt when it's invoked
TopNStoreBolt().run()
