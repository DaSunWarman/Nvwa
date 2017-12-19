#
# Copyright (C) 2017 The Nvwa Open Source Project
#

import threading
from utils.Binder import Binder


class ActivityManager(object):
    _instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                cls.__lock.acquire()
                # double check
                if not cls._instance:
                    cls._instance = super(ActivityManager, cls).__new__(cls, *args, **kwargs)
            finally:
                cls.__lock.release()
        return cls._instance

    def __init__(self):
        pass

    def m_init(self):
        self.app = None
        self.o_binder = Binder()
        self.o_binder.m_registerObj(self.__class__.__name__, self.__class__)

    def m_addAppTask(self, s_app):
        import importlib
        packageModule = importlib.import_module('packages.' + s_app + '.src.' + s_app)
        o_package = eval('packageModule.' + s_app + '()')
        self.app = o_package
    def m_getAppTasks(self):
        return self.app

    def m_runAppTasks(self):

        self.app.onCreate()
        self.app.onStart()
        self.app.onResume()
        self.app.onPause()
        self.app.onStop()
        self.app.onRestart()
        self.app.onDestroy()

    def m_destroy(self):
        if self.o_binder is not None:
            self.o_binder.m_unregisterObj()


class AppTask(object):
    def __init__(self):
        pass