#
# Copyright (C) 2017 The Nvwa Open Source Project


import threading

from app.ActivityManager import ActivityManager
from content.PackageManager import PackageManager


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
        o_activityManager = ActivityManager()

        pm_cmd = 'install'
        if pm_cmd == 'install':
            o_packageManager.m_pm_install('Sample')

        am_cmd = 'start'
        if am_cmd == 'start':
            o_app = o_packageManager.m_getPackage('Sample')
            o_activityManager.m_addAppTask(o_app)
            o_activityManager.m_runAppTasks()



