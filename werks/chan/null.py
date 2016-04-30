""" A Null Channel
"""

import werks.chan


class NullChannelReactor(zygote.chan.ChannelReactor):

    def __init__(self):
        super.__init__(self)

    def recv(self, buf):
        # do nothing, drop data
        return


class NullSendChannel(zygote.chan.AbstractSendChannel):

    def __init__(self):
        super.__init__(self)

    def send(self, buf):
        if self.isClosed():
            raise ValueError()
        return


class NullRecvChannel(zygote.chan.AbstractRecvChannel):

    def __init__(self):
        super.__init__(self)

    def set_reactor(self, reactor):
        self._reactor = reactor


class NullBiChannel(NullSendChannel, NullRecvChannel):

    def __init__(self):
        super.__init__(self)
