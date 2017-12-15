#
# Copyright (C) 2017 The Nvwa Open Source Project


import threading
from app.ServiceManager import ServiceManager
from content.ServerManager import ServerManager
import time

class ServiceProcess(object):

    _instance = None
    __lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                cls.__lock.acquire()
                # double check
                if not cls._instance:
                    cls._instance = super(ServiceProcess, cls).__new__(cls, *args, **kwargs)
            finally:
                cls.__lock.release()
        return cls._instance

    @staticmethod
    def m_runServiceProcess():
        print "Service Process start"
        o_serverManager = ServerManager()
        o_serviceManager = ServiceManager()

        o_serverManager.m_svr_install('RedRatServer')

        svr_cmd = 'RedRatServer'
        if svr_cmd == 'RedRatServer':

            o_svr = o_serverManager.m_getServer('RedRatServer')
            o_serviceManager.m_addServerTask(o_svr)
            o_serviceManager.m_runServerTasks()


