#
# Copyright (C) 2017 The Nvwa Open Source Project


import os
from utils.Binder import Binder

class Communicate(object):
    def __init__(self):
        pass

    @classmethod
    def m_init(cls):
        cls.o_binder = Binder()
        cls.o_rm_packageManager = cls.o_binder.m_getRemoteManager('PackageManager')
        cls.o_rm_activityManager = cls.o_binder.m_getRemoteManager('ActivityManager')
        cls.o_packageManager = cls.o_rm_packageManager.PackageManager()
        cls.o_activityManager = cls.o_rm_activityManager.ActivityManager()
