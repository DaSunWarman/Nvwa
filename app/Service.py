#
# Copyright (C) 2017 The Nvwa Open Source Project
#

from content.Context import Context


class Service(Context):

    def __init__(self):
        super(Service, self).__init__()

    def getApplication(self):
        pass

    def onCreate(self):
        pass
    def onStartCommand(self):
        pass
    def onBind(self):
        pass
    def onUnbind(self):
        pass
    def onDestroy(self):
        pass

