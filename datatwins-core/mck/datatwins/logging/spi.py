from abc import ABC, abstractmethod

import structlog


class LoggingServiceProvider(ABC):

    @abstractmethod
    def info(self, message: str, **kwargs):
        pass


class StructLogServiceProvider(LoggingServiceProvider):

    LOG = structlog.getLogger()

    def __init__(self):
        self.LOG.info("StructLogServiceProvider.__init__", scope='entering')
        self.LOG.info("StructLogServiceProvider.__init__", scope='exiting')

    def info(self, message: str, **kwargs):
        self.LOG.info("StructLogServiceProvider.info", **kwargs)
        self.LOG.info(message)
        self.LOG.info("StructLogServiceProvider.info", **kwargs)
