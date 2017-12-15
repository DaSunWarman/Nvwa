#
# Copyright (C) 2017 The Nvwa Open Source Project


import threading
from service.RedRatServer.RedRatServer import RedRatServer


class ServerManager(object):

    _instance = None
    __lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                cls.__lock.acquire()
                # double check
                if not cls._instance:
                    cls._instance = super(ServerManager, cls).__new__(cls, *args, **kwargs)
            finally:
                cls.__lock.release()
        return cls._instance

    def __init__(self):
        self.d_serverDict = {}

    def m_svr_install(self, s_server):
        o_server = RedRatServer()
        d_svrDict = {s_server: o_server}
        self.d_serverDict.update(d_svrDict)

    def m_svr_r_install(self, s_server):
        pass

    def m_svr_uninstall(self, s_server):
        self.d_serverDict.pop(s_server, 'Server not find')

    def m_svr_list(self):
        return self.d_serverDict.keys()

    def m_getServer(self, s_server):
        return self.d_serverDict.get(s_server, 'Server not find')

