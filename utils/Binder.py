#
# Copyright (C) 2017 The Nvwa Open Source Project


import multiprocessing
from multiprocessing.managers import BaseManager, BaseProxy


class RemoteManager(BaseManager):
    pass


class RemoteProxy(BaseProxy):
    pass


class Binder(object):
    def m_getRemoteManager(self, s_clsName):
        RemoteManager.register(s_clsName)
        o_manager = RemoteManager(address=r'\\.\pipe\nvwa' + s_clsName, authkey=s_clsName)
        o_manager.connect()
        return o_manager

    def m_registerObj(self, s_clsName, o_cls):
        RemoteManager.register(typeid=s_clsName, callable=o_cls)
        self.o_manager = RemoteManager(address=r'\\.\pipe\nvwa' + s_clsName, authkey=s_clsName)
        self.o_manager.start()

    def m_unregisterObj(self):
        self.o_manager.shutdown()




