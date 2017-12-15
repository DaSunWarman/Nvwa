import multiprocessing
import multiprocessing
import time
import random
import sys

# print 'Testing callback:'
def mul(a, b):
    time.sleep(0.5*random.random())
    return a * b

def pow3(x):
    return x ** 3

if __name__ == '__main__':
    multiprocessing.freeze_support()

    PROCESSES = 4
    print 'Creating pool with %d processes\n' % PROCESSES
    pool = multiprocessing.Pool(PROCESSES)


    A = []
    B = [56, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

    r = pool.apply_async(mul, (7, 8), callback=A.append)
    r.wait()

    r = pool.map_async(pow3, range(10), callback=A.extend)
    r.wait()

    if A == B:
        print '\tcallbacks succeeded\n'
    else:
        print '\t*** callbacks failed\n\t\t%s != %s\n' % (A, B)
