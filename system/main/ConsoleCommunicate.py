#
# Copyright (C) 2017 The Nvwa Open Source Project


from system.main.Communicate import Communicate
from multiprocessing.connection import Listener
from array import array


class ConsoleCommunicate(Communicate):
    def __init__(self):
        super(ConsoleCommunicate, self).__init__()
        self.address = ''
        self.listener = None
        self.conn = None
        self.s_cmd = ''
        self.s_answer = ''

    def m_initCommunicate(self):
        self.address = r'\\.\pipe\PipeConsole'
        self.listener = Listener(self.address, family='AF_PIPE', authkey='nvwa')
        self.conn = self.listener.accept()
        print 'connection accepted from', self.listener.last_accepted

    def m_recvCmd(self):
        self.s_cmd = self.conn.recv()

    def m_parseCmd(self):
        self.s_cmd = self.s_cmd

    def m_runCmd(self):
        print self.s_cmd
        return self.s_cmd

    def m_answerCmd(self):
        self.s_answer = 'Success'
        self.conn.send(self.s_answer)

    def m_execute(self):
        self.m_recvCmd()
        self.m_parseCmd()
        self.m_runCmd()
        self.m_answerCmd()


    def m_close(self):
        if self.conn != None:
            self.conn.close()
        if self.listener != None:
            self.listener.close()

    def __del__(self):
        self.m_close()


