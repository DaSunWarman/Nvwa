#
# Copyright (C) 2017 The Nvwa Open Source Project
#


import threading
from packages.Sample.src.Sample import Sample
from utils.Binder import Binder


class PackageManager(object):

    _instance = None
    __lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                cls.__lock.acquire()
                # double check
                if not cls._instance:
                    cls._instance = super(PackageManager, cls).__new__(cls, *args, **kwargs)
            finally:
                cls.__lock.release()
        return cls._instance

    def __init__(self):
        pass

    def m_init(self):
        self.d_packageDict = {}
        self.o_binder = Binder()
        self.o_binder.m_registerObj(self.__class__.__name__, self.__class__)

    def m_pm_install(self, s_package):
        import importlib
        packageModule = importlib.import_module('packages.'+ s_package + '.src.'+ s_package)
        o_package  = eval('packageModule.' + s_package + '()')

        d_appDict = {s_package: o_package}
        self.d_packageDict.update(d_appDict)

    def m_pm_r_install(self, s_package):
        pass

    def m_pm_uninstall(self, s_package):
        self.d_packageDict.pop(s_package, 'Package not find')

    def m_pm_list(self):
        return self.d_packageDict.keys()

    def m_getPackage(self, s_package):
        return self.d_packageDict.get(s_package, 'Package not find')

    def m_destroy(self):
        if self.o_binder is not None:
            self.o_binder.m_unregisterObj()

