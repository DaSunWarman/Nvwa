#
# Copyright (C) 2017 The Nvwa Open Source Project


from multiprocessing.connection import Listener
from array import array
from multiprocessing.connection import Client


class Console(object):
    def __init__(self):
        self.address = ''
        self.listener = None
        self.conn = None
        self.s_cmd = ''

    def m_initConsole(self):
        self.address = r'\\.\pipe\PipeConsole'
        self.conn = Client(self.address, authkey='nvwa')

    def m_getInput(self):
        self.s_input = raw_input("nvwa:$")

    def m_parseCmd(self):
        self.s_cmd = self.s_input


    def m_sendCmd(self):
        self.conn.send(self.s_cmd)


    def m_recvAnswer(self):
        print self.conn.recv()

    def m_close(self):
        if self.conn != None:
            self.conn.close()
        if self.listener != None:
            self.listener.close()

    def __del__(self):
        self.m_close()


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    c = Console()
    c.m_initConsole()
    while True:
        c.m_getInput()
        c.m_parseCmd()
        if c.s_cmd == "exit":
            break

        c.m_sendCmd()
        c.m_recvAnswer()

    c.m_close()

