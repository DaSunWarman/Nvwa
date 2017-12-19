#
# Copyright (C) 2017 The Nvwa Open Source Project


import threading

from app.ActivityManager import ActivityManager
from content.PackageManager import PackageManager
import time


class AppProcess(object):
    _instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                cls.__lock.acquire()
                # double check
                if not cls._instance:
                    cls._instance = super(AppProcess, cls).__new__(cls, *args, **kwargs)
            finally:
                cls.__lock.release()
        return cls._instance


    @staticmethod
    def m_runAppProcess():
        print "App Process start"
        o_packageManager = PackageManager()
        o_packageManager.m_init()
        o_activityManager = ActivityManager()
        o_activityManager.m_init()



        while True:
            time.sleep(20)
            print "App Process runing"
        o_packageManager.m_destroy()
        o_activityManager.m_destroy()



