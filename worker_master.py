import redis 
import time 

red = redis.StrictRedis(host='localhost',
                        port=6379,
                        db=0)

queue = []

def str2bool(x):
    if x == b'True':
        return True
    if x == b'False':
        return False
    raise ValueError

while True:
    is_new = str2bool(red.get("is_new_product"))
    if is_new:
        taken_product = red.get("product")
        queue.append(taken_product)
        print("product {} has been in Queue".format(taken_product))
        red.set("is_new_product",str(False))

        is_ready_worker2 = str2bool(red.get('is_ready_worker2'))
        is_ready_worker3 = str2bool(red.get('is_ready_worker3'))

        product = queue.pop(0)
        if is_ready_worker2 == False: # previous product in worker2 was processed
            red.set("is_ready_worker2",str(True)) 
            red.set("product_worker2", product)
        
        if is_ready_worker3 == False: # previous product in worker3 was processed
                red.set("is_ready_worker3",str(True)) 
                red.set("product_worker3", product)