import time
from redis_cache.rediscache import  cache_it_pickle
import redis
c= redis.StrictRedis()

@cache_it_pickle()
def read_f_(x):

    time.sleep(5)

    return {1:'3',2:'4'}
%time read_f_(3)
