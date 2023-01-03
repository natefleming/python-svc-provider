from .spi import EmailServiceProvider, SmtpEmailServiceProvider
from mck.datatwins.logging import LoggingService, log, entering, exiting
from types import ModuleType
from typing import Callable

import importlib
import os
import structlog

LOG = LoggingService()


@log(LOG, entering, exiting)
def service_provider_factory(module_name: str,
                             class_name: str) -> EmailServiceProvider:

    @log(LOG, entering, exiting)
    def create():
        m: ModuleType = importlib.import_module(module_name)
        clazz = m.__getattr__(m, class_name)
        service_provider = clazz()
        return service_provider

    return create


@log(LOG, entering, exiting)
def find_service_provider() -> Callable[[], EmailServiceProvider]:
    LOG.info("find_service_provider", scope='entering')
    DEFAULT_SERVICE_PROVIDER = SmtpEmailServiceProvider()

    cloud_platform = os.environ.get('CLOUD', 'default').lower()
    service_provider: EmailServiceProvider = {
        'aws':
            service_provider_factory('mck.datatwins.email.aws.spi',
                                     'AwsEmailServiceProvider'),
        'azure':
            service_provider_factory('mck.datatwins.email.azure.spi',
                                     'AzureEmailServiceProvider'),
        'gcp':
            service_provider_factory('mck.datatwins.email.gcp.spi',
                                     'GcpEmailServiceProvider'),
        'default':
            lambda: DEFAULT_SERVICE_PROVIDER
    }.get(cloud_platform, DEFAULT_SERVICE_PROVIDER)()

    LOG.info("find_service_provider", scope='exiting')
    return service_provider


class EmailService(object):

    @log(LOG, entering, exiting)
    def __init__(self, provider: EmailServiceProvider = None):
        self._provider: EmailServiceProvider = provider if provider else find_service_provider(
        )

    @log(LOG, entering, exiting)
    def send(self, message: str):
        return self._provider.send(message)
