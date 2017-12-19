#
# Copyright (C) 2017 The Nvwa Open Source Project


from system.main.Communicate import Communicate
from multiprocessing.connection import Listener
from array import array
from utils.Binder import Binder


class ConsoleCommunicate(Communicate):
    def __init__(self):
        super(ConsoleCommunicate, self).__init__()

    def m_init_temp(self):
        super(ConsoleCommunicate, self).m_init()
        self.o_binder.m_registerObj(self.__class__.__name__, self.__class__)
        # self.o_rm_consoleManager = None
        # self.o_console = None

    def m_getConsole(self):
        if self.o_rm_consoleManager is None:
            self.o_rm_consoleManager = self.o_binder.m_getRemoteManager('Console')
            self.o_console = self.o_rm_consoleManager.Console()
            return self.o_console
        else:
            return self.o_console

    def m_cmd_pm_install(self, s_package):
        self.o_packageManager.m_init()
        self.o_packageManager.m_pm_install(s_package)



    def m_on_cmd_pm_install(self, s_result):
        self.o_console = self.m_getConsole()
        self.o_console.m_on_cmd_pm_install(s_result)

    def m_cmd_pm_install_r(self):
        pass
    def m_on_cmd_pm_install_r(self, s_result):
        print s_result

    def m_cmd_pm_uninstall(self):
        pass
    def m_on_cmd_pm_uninstall(self, s_result):
        print s_result
    def m_cmd_pm_list(self):
        pass
    def m_on_cmd_pm_list(self, s_result):
        print s_result
    def m_cmd_am_start(self):
        s_app = 'Sample'
        self.o_activityManager.m_addAppTask(s_app)
        self.o_activityManager.m_runAppTasks()

    def m_on_cmd_am_start(self, s_result):
        self.o_console = self.m_getConsole()
        self.o_console.m_on_cmd_am_start(s_result)

    def m_cmd_am_pause(self):
        pass
    def m_on_cmd_am_pause(self, s_result):
        print s_result
    def m_cmd_am_stop(self):
        pass
    def m_on_cmd_am_stop(self, s_result):
        print s_result
    def m_cmd_am_restart(self):
        pass
    def m_on_cmd_am_restart(self, s_result):
        print s_result




    def m_destroy(self):
        if self.o_binder is not None:
            self.o_binder.m_unregisterObj()





