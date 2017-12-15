# #
# # Copyright (C) 2017 The Nvwa Open Source Project
# #
#
# import time
# import random
#
# from multiprocessing import Process, Queue, current_process, freeze_support
#
# def mul(a, b):
#     time.sleep(0.5*random.random())
#     return a * b
# task_queue = Queue()
# TASKS1 = [(mul, (i, 7)) for i in range(20)]
# for task in TASKS1:
#         task_queue.put(task)
#
# for func, args in iter(task_queue.get, 'STOP'):
#     print func, args

#iter and generator
#the first try
#=================================
i = iter('abcd')
print i.next()
print i.next()
print i.next()

s = {'one':1,'two':2,'three':3}
print s
m = iter(s)
print m.next()
print m.next()
print m.next()