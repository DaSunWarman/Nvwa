#
# Copyright (C) 2017 The Nvwa Open Source Project
#


import threading
from packages.Sample.src.Sample import Sample

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
        self.d_packageDict = {}

    def m_pm_install(self, package):
        package = Sample()
        d_appDict = {'Sample': package}
        self.d_packageDict.update(d_appDict)

    def m_pm_r_install(self, package):
        pass

    def m_pm_uninstall(self, package):
        self.d_packageDict.pop(str(package), 'Package not find')

    def m_pm_list(self):
        return self.d_packageDict.keys()

    def m_getPackage(self, package):
        return self.d_packageDict.get(package, 'Package not find')

