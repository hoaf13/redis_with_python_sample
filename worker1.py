import redis 
import time 
import json

red = redis.StrictRedis(host='localhost',
                        port=6379,
                        db=0)

product = 100

def str2bool(x):
    if x == b'True':
        return True 
    if x == b'False':
        return False
    raise ValueError
    
while True:
    if red.get('is_new_product') is None:
        red.set('is_new_product', str(False))
    is_used = not str2bool(red.get('is_new_product'))
    if is_used:
        ans = dict()
        ans['id'] = product
        ans['value'] = product
        ans = json.dumps(ans)
        product += 1 
        red.set("product", ans)
        red.set("is_new_product", str(True))
        print("worker1 has public product: {}".format(ans))
        time.sleep(0.1)
