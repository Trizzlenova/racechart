
from itertools import count
# from sleepy import buzzergen


# print('Hello, World!')

def add(a, b):
  return a + b

def subt(a, b):
  return a - b

def mult(a, b):
  return a * b

import time

while True:
  # function here
  time.sleep(5)
  # function here
  time.sleep(5)
  # function here
  break

# class Async:
#   def __init__(self, func, args):
#     self.func = func
#     self.args = args

#   def inlined_async(func):
#     @wraps(func)
#     def wrapper(*args):
#       f = func(*args)
#       result_queue = Queue()
#       result_queue.put(None)
#       while True:
#         result = result_queue.get()
#         try:
#           a = f.send(result)
#           apply_async(a.func, a.args, callback=result_queue.put)
#         except StopIteration:
#           break
#     return wrapper

#   def add(x, y):
#     return x + y

#   @inlined_async
#   def test():
#     r = yield Async(add, (2,3))
#     print(r)
#     r = yield Async(add, ('hello', 'world'))
#     print(r)
#     for n in range(10):
#       r = yield Async(add, (n, n))
#       print(r)
#     print('Goodbye')


# Playing around with workers


# def worker():
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         do_work(item)
#         q.task_done()
