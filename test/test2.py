from multiprocessing.connection import Client
from array import array

# address = ('localhost', 6000)
address = r'\\.\pipe\PipeConsole'
conn = Client(address, authkey='nvwa')

print conn.recv()                 # => [2.25, None, 'junk', float]

print conn.recv_bytes()            # => 'hello'

arr = array('i', [0, 0, 0, 0, 0])
print conn.recv_bytes_into(arr)     # => 8
print arr                         # => array('i', [42, 1729, 0, 0, 0])

conn.close()