#
# Copyright (C) 2017 The Nvwa Open Source Project


from system.main.Communicate import Communicate


class ConsoleCommunicate(Communicate):
    def __init__(self):
        super(ConsoleCommunicate, self).__init__()

    def m_init(self):
        super(ConsoleCommunicate, self).m_init()