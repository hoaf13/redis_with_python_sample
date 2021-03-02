# Redis with Python 
----

Avoid being bottlenecked in the system, redis (be like memcached) is used to created some worker to deal with the above problem. 
 

### How to use
 - Install redis-py in anaconda and redis service in your local.
 - Run serial files: worker1.py -> worker_master.py -> work2.py -> worker3.py.

### Explain
 - **worker_master**: has a Queue to aim storage from worker1 and distribute product to worker2 , worker3, ... 
 - **worker1**: push product to the Queue in worker master.
 - **worker2**, **worker3**: aim to avoid being bottlenecked, you can create more. 
