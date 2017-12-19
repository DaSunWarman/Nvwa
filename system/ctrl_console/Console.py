#
# Copyright (C) 2017 The Nvwa Open Source Project


from multiprocessing.connection import Listener
from array import array
from multiprocessing.connection import Client
from multiprocessing import Event
import threading
import multiprocessing
from utils.Binder import Binder
from multiprocessing.managers import BaseManager, BaseProxy
import Queue


class Console(object):
    '''
    pm install package
    pm install -r package
    pm uninstall package
    pm list

    am start
    am pause
    am stop
    am restart
    '''

    def m_initConsole(self):
        self.s_cmd = ''
        self.o_binder = Binder()
        self.o_binder.m_registerObj(self.__class__.__name__, self.__class__)
        self.o_rm_consoleCommunicate = self.o_binder.m_getRemoteManager('ConsoleCommunicate')
        self.o_consoleCommunicate = self.o_rm_consoleCommunicate.ConsoleCommunicate()

    def m_getInput(self):
        self.s_input = raw_input("nvwa:$")

    def m_parseCmd(self):
        self.s_cmd = self.s_input

    def m_cmd_pm_install(self, s_package):
        self.o_consoleCommunicate.m_init()
        self.o_consoleCommunicate.m_cmd_pm_install(s_package)

    def m_on_cmd_pm_install(self, s_result):
        print s_result

    def m_cmd_pm_install_r(self, s_package):
        self.o_consoleCommunicate.m_cmd_pm_install_r(s_package)

    def m_on_cmd_pm_install_r(self, s_result):
        print s_result

    def m_cmd_pm_uninstall(self, s_package):
        self.o_consoleCommunicate.m_cmd_pm_uninstall(s_package)

    def m_on_cmd_pm_uninstall(self, s_result):
        print s_result

    def m_cmd_pm_list(self):
        self.o_consoleCommunicate.m_cmd_pm_list()

    def m_on_cmd_pm_list(self, s_result):
        print s_result

    def m_cmd_am_start(self):
        # self.o_consoleCommunicate.m_init()
        self.o_consoleCommunicate.m_cmd_am_start()

    def m_on_cmd_am_start(self, s_result):
        print s_result

    def m_cmd_am_pause(self):
        self.o_consoleCommunicate.m_cmd_am_pause()

    def m_on_cmd_am_pause(self, s_result):
        print s_result

    def m_cmd_am_stop(self):
        self.o_consoleCommunicate.m_cmd_am_stop()

    def m_on_cmd_am_stop(self, s_result):
        print s_result

    def m_cmd_am_restart(self):
        self.o_consoleCommunicate.m_cmd_am_restart()

    def m_on_cmd_am_restart(self, s_result):
        print s_result


    def m_destroy(self):
        if self.o_binder is not None:
            self.o_binder.m_unregisterObj()


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    c = Console()
    c.m_initConsole()
    while True:
        c.m_getInput()
        c.m_parseCmd()
        # TODO
        s_package = 'Sample'

        if c.s_cmd == "exit":
            break
        elif c.s_cmd == 'install':
            c.m_cmd_pm_install(s_package)
        elif c.s_cmd == 'installr':
            c.m_cmd_pm_install_r(s_package)
        elif c.s_cmd == 'uninstall':
            c.m_cmd_pm_uninstall(s_package)
        elif c.s_cmd == 'list':
            c.m_cmd_pm_list()
        elif c.s_cmd == 'start':
            c.m_cmd_am_start()
        elif c.s_cmd == 'pause':
            c.m_cmd_am_pause()
        elif c.s_cmd == 'stop':
            c.m_cmd_am_stop()
        elif c.s_cmd == 'restart':
            c.m_cmd_am_restart()

    c.m_destroy()

