#
# Copyright (C) 2017 The Nvwa Open Source Project


import time

from system.main.ConsoleCommunicate import ConsoleCommunicate
from system.main.Zygote import Zygote
from utils.Binder import Binder
from multiprocessing.managers import BaseManager
import Queue


class QueueManager(BaseManager):
    pass


class Main():
    __version__ = 'shitou'

    def __init__(self):
        pass

    def m_initMain(self):
        self.o_consoleCommunicate = None
        self.s_cmd = ''
        print "Welcome Nvwa System"
        print "Copyright (C) 2017 The Nvwa Open Source Project"
        print "Nvwa Version : " + Main.__version__

        # o_zygote = Zygote()
        # o_zygote.m_initProcess()
        # create app process and service process
        Zygote.fork()
        # wait for PackageManager and ActivityManager initial
        time.sleep(1)

        self.o_consoleCommunicate = ConsoleCommunicate()
        self.o_consoleCommunicate.m_init_temp()

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

            time.sleep(20)

            # self.o_consoleCommunicate.m_answerCmd()

    def m_exitMain(self):

        print 'shutdown all remote object'
        self.o_consoleCommunicate.m_destroy()
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

