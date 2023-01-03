from abc import ABC, abstractmethod
from mck.datatwins.logging import LoggingService, log, entering, exiting


class EmailServiceProvider(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class SmtpEmailServiceProvider(EmailServiceProvider):

    LOG = LoggingService()

    @log(LOG, entering, exiting)
    def __init__(self):
        pass

    @log(LOG, entering, exiting)
    def send(self, message: str):
        self.LOG.info(message)
