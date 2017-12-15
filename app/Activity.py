#
# Copyright (C) 2017 The Nvwa Open Source Project
#

import sys

from content.Context import Context


class Activity(Context):
    def __init__(self):
        super(Activity, self).__init__()

    def onCreate(self):
        pass
    def onStart(self):
        pass
    def onResume(self):
        pass
    def onPause(self):
        pass
    def onStop(self):
        pass

    def onRestart(self):
        pass

    def onDestroy(self):
        pass