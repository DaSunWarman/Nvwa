import sys
sys.path.append("E:\\Work\\PycharmProjects\\Nvwa\\shitou\\frameworks\\base\\core\\python")

print sys.path


from nvwa.content.Context import Context
c =Context()


class Activity(Context):
    def __init__(self):
        pass

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