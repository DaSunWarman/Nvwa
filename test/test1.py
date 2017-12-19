from multiprocessing.managers import BaseManager, BaseProxy
import Queue
import multiprocessing
class MyM(BaseManager):pass

class MyP(BaseProxy):
    _exposed = ('m_init', 'out', 'b')

    def m_init(self):
        return self

    def out(self):
        return self._callmethod('next')

    def b(self):
        return self._callmethod('__next__')
import  threading


class A():
    a = 1
    # def __init__(self):
    #     self.b = 2


    # def m_init(self):
    #     self.b = 0
    #     self.b += 1
    @classmethod
    def out(cls):
        print A.a
        A.a += 1
        # print self.b
        # self.b.p()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    MyM.register('A', callable=A)
    m = MyM(address=r'\\.\pipe\aa', authkey='abracadabra')
    # m.start()
    a = A()
    # a.m_init()
    a.out()
    # m.shutdown()
    m.start()
    a.out()
    # s = m.get_server()
    # s.serve_forever()
    # m.start()
    while True:
        pass