#
# Copyright (C) 2017 The Nvwa Open Source Project
#


from app.Service import Service


class RedRatServer(Service):
    def __init__(self):
        super(RedRatServer, self).__init__()
        self.s_tag = 'RedRatService'

    def getApplication(self):
        print self.s_tag + ' getApplication'

    def onCreate(self):
        print self.s_tag + ' onCreate'
    def onStartCommand(self):
        print self.s_tag + ' onStartCommand'
    def onBind(self):
        print self.s_tag + ' onBind'
    def onUnbind(self):
        print self.s_tag + ' onUnbind'
    def onDestroy(self):
        print self.s_tag + ' onDestroy'