import storm
import redis

class WordCountStoreBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._redis_conf = conf.get("redis")  # redis configuration converted into a dictonary
        storm.logInfo("Word Count Store bolt instance starting...")

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
        # Task: save word count pair to redis under the specified hash name

        word = tup.values[0]
        count = tup.values[1]
        hash_name = self._redis_conf['hashKey']
        self._redis.hset(hash_name, word, count)
        storm.logInfo("Saved word {} count {} to Redis".format(word, count))

# Start the bolt when it's invoked
WordCountStoreBolt().run()
