#
# Copyright (C) 2017 The Nvwa Open Source Project


import threading
import time
from multiprocessing import Process
from app.AppProcess import AppProcess
from app.ServiceProcess import ServiceProcess



class Zygote(object):
    _instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                cls.__lock.acquire()
                # double check
                if not cls._instance:
                    cls._instance = super(Zygote, cls).__new__(cls, *args, **kwargs)
            finally:
                cls.__lock.release()
        return cls._instance

    _o_appProcess = None
    _o_serviceProcess = None
    _o_sp = None
    _o_ap = None

    @staticmethod
    def m_initProcess():
        Zygote._o_appProcess = AppProcess()
        Zygote._o_serviceProcess = ServiceProcess()

    @staticmethod
    def m_runAppProcess():
        for i in range(10):
            print i
            print "m_runAppProcess"
            # time.sleep(1)
        # Zygote._o_appProcess.m_runAppProcess()

    @staticmethod
    def m_runServiceProcess():
        for i in range(10):
            print i
            print "__m_runServiceProcess"
            # time.sleep(2)
        # Zygote._o_serviceProcess.m_runServiceProcess()

    @staticmethod
    def fork():
        # sp = Process(target=Zygote.m_runServiceProcess, name='ServiceProcess', args=())
        Zygote._o_sp = Process(target=f_runServiceProcess, name='ServiceProcess', args=())
        Zygote._o_sp.start()
        # ap = Process(target=Zygote.m_runAppProcess, name='AppProcess', args=())
        Zygote._o_ap = Process(target=f_runAppProcess, name='AppProcess', args=())
        Zygote._o_ap.start()

    @staticmethod
    def join():
        Zygote._o_sp.join()
        Zygote._o_ap.join()

def f_runServiceProcess():
    # Zygote._o_serviceProcess.m_runServiceProcess()
    ServiceProcess.m_runServiceProcess()
def f_runAppProcess():
    # Zygote._o_appProcess.m_runAppProcess()
    AppProcess.m_runAppProcess()

