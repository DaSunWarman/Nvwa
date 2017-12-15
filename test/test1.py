from multiprocessing.connection import Listener
from array import array

# address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
address = r'\\.\pipe\PipeConsole'
listener = Listener(address, family='AF_PIPE', authkey='nvwa')

conn = listener.accept()
print 'connection accepted from', listener.last_accepted

conn.send('hello')

conn.send_bytes('hello')

conn.send_bytes(array('i', [42, 1729]))

conn.close()
listener.close()