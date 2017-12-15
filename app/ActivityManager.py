#
# Copyright (C) 2017 The Nvwa Open Source Project
#

import threading


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
        self.app = None

    def m_addAppTask(self, app):
        self.app = app
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


class AppTask(object):
    def __init__(self):
        pass