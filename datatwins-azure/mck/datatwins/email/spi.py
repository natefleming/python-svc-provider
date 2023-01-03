from abc import ABC, abstractmethod
from mck.datatwins.email import EmailServiceProvider
from mck.datatwins.logging import LoggingService, log, entering, exiting


class AwsEmailServiceProvider(EmailServiceProvider):

    LOG = LoggingService()

    @log(LOG, entering, exiting)
    def __init__(self):
        pass

    @log(LOG, entering, exiting)
    def send(self, message: str):
        self.LOG.info(message)
