#
# Copyright (C) 2017 The Nvwa Open Source Project
#

from app.Activity import Activity


class Sample(Activity):
    
    def __init__(self):
        super(Sample, self).__init__()
        self.s_tag = 'Sample'

    def onCreate(self):
        print self.s_tag + ' onCreate'

    def onStart(self):
        print self.s_tag + ' onStart'

    def onResume(self):
        print self.s_tag + ' onResume'

    def onPause(self):
        print self.s_tag + ' onPause'

    def onStop(self):
        print self.s_tag + ' onStop'

    def onRestart(self):
        print self.s_tag + ' onRestart'

    def onDestroy(self):
        print self.s_tag + ' onDestroy'


