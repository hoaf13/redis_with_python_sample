import redis 
import time

red = redis.StrictRedis(host='localhost',
                        port=6379,
                        db=0)

def str2bool(x):
    if x == b'True':
        return True 
    if x == b'False':
        return False
    raise ValueError

while True:
    if red.get('is_ready_worker2') is None:
        red.set('is_ready_worker2', str(False))
    is_ready = str2bool(red.get('is_ready_worker2'))
    if is_ready: # existed product
        taken_product = red.get('product_worker2')
        print("worker2 is processing product: {}".format(taken_product))
        red.set('is_ready_worker2', str(False)) # product has been processed
        time.sleep(1)
        