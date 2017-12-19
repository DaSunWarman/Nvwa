from multiprocessing.managers import BaseManager
class QueueManager(BaseManager): pass

QueueManager.register('A')
m = QueueManager(address=r'\\.\pipe\aa', authkey='abracadabra')
m.connect()

a = m.A()

# a.m_init()
a.out()