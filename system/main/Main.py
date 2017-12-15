#
# Copyright (C) 2017 The Nvwa Open Source Project


import time

from system.main.ConsoleCommunicate import ConsoleCommunicate
from system.main.Zygote import Zygote


class Main():
    __version__ = 'shitou'

    def __init__(self):
        self.o_consoleCommunicate = None
        self.s_cmd = ''


    def m_initMain(self):
        print "Welcome Nvwa System"
        print "Copyright (C) 2017 The Nvwa Open Source Project"
        print "Nvwa Version : " + Main.__version__

        self.o_consoleCommunicate = ConsoleCommunicate()
        # self.o_consoleCommunicate.m_initCommunicate()


        # o_zygote = Zygote()
        # o_zygote.m_initProcess()
        # create app process and service process
        Zygote.fork()

    def m_mainLoop(self):
        while True:
            # communicate with console
            # communicate with app
            # communicate with service

            # svclist

            # self.o_consoleCommunicate.m_execute()
            # self.o_consoleCommunicate.m_recvCmd()
            # self.o_consoleCommunicate.m_parseCmd()
            # self.s_cmd = self.o_consoleCommunicate.m_runCmd()
            print "m_mainLoop"
            if "pm" in self.s_cmd:
                print "pm"
            if 'am' in self.s_cmd:
                print "am"

            time.sleep(5)

            # self.o_consoleCommunicate.m_answerCmd()

    def m_exitMain(self):
        self.o_consoleCommunicate.m_close()
        print "Waiting App process and Service process exit"
        Zygote.join()
        print "Exiting Nvwa System"

    @staticmethod
    def main():
        print __file__
        m = Main()
        m.m_initMain()
        m.m_mainLoop()
        m.m_exitMain()

