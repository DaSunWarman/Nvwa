#
# Copyright (C) 2017 The Nvwa Open Source Project
#


import threading

from service.RedRatServer.RedRatServer import RedRatServer


class ServiceManager(object):

    _instance = None
    __lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                cls.__lock.acquire()
                # double check
                if not cls._instance:
                    cls._instance = super(ServiceManager, cls).__new__(cls, *args, **kwargs)
            finally:
                cls.__lock.release()
        return cls._instance

    def __init__(self):
        self.svr = None

    def m_addServerTask(self, o_server):
        self.svr = o_server

    def m_getServerTasks(self):
        return self.svr

    def m_runServerTasks(self):
        self.svr.onCreate()
        self.svr.onStartCommand()
        self.svr.onBind()
        self.svr.onUnbind()
        self.svr.onDestroy()


class AppTask(object):
    def __init__(self):
        pass