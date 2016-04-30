""" Message 'Channel' - Send / Receive channels
"""

import abc

__version__ = "0.1"

## ############################################################
##
class Closeable(Object):

    def __init__(self):
        self.__closed = False

    def isClosed(self):
        try:
            ## defense against __init__ being bypassed
            self.__closed
        except:
            self.__closed = False
        return self.__closed
        
    def close(self):
        self.__closed = True
        

class AbstractSendChannel(Closeable):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def send(self, buf):
        """send buf in the channel"""

        
class AbstractRecvChannel(Closeable):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_reactor(self, reactor):
        """Set the reactor for this channel"""

        
class AbstractBiChannel(AbstractSendChannel, AbstractRecvChannel):
    __metaclass__ = abc.ABCMeta

    #@abc.abstractmethod
    #def get_receiver(self):
    #    """Return a concrete ChannelReceiver"""

    

## ############################################################
##
class ChannelReactor(Object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def recv(self, raw):
        """Invoked when a message arrives"""


        
