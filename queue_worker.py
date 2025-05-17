import os
from redis import Redis
from rq import Worker, Queue
#from rq.connection import Connection

listen = ['default']
redis_conn = Redis()

if __name__ == '__main__':
    #with Connection(redis_conn):
    queues = [Queue(name, connection=redis_conn) for name in listen]
    worker = Worker(queues, connection=redis_conn)
    worker.work()
