from abc import ABC, abstractmethod
from mck.datatwins.logging import LoggingServiceProvider
import structlog


class AwsLoggingServiceProvider(LoggingServiceProvider):

    LOG = structlog.getLogger()

    def __init__(self):
        self.LOG.info("AwsLoggingServiceProvider.__init__", scope='entering')
        self.LOG.info("AwsLoggingServiceProvider.__init__", scope='exiting')

    def info(self, message: str, **kwargs):
        self.LOG.info("AwsLoggingServiceProvider.info", **kwargs)
        self.LOG.info(message)
        self.LOG.info("AwsLoggingServiceProvider.info", **kwargs)
