from .spi import LoggingServiceProvider, StructLogServiceProvider

from types import ModuleType
from typing import Callable

import importlib
import os
import structlog

LOG = structlog.getLogger()


def service_provider_factory(module_name: str,
                             class_name: str) -> LoggingServiceProvider:

    def create():
        LOG.info("service_provider_factory.create", scope='entering')
        m: ModuleType = importlib.import_module(module_name)
        clazz = m.__getattr__(m, class_name)
        service_provider = clazz()
        LOG.info("service_provider_factory.create", scope='exiting')
        return service_provider

    return create


def find_service_provider() -> Callable[[], LoggingServiceProvider]:
    LOG.info("find_service_provider", scope='entering')
    DEFAULT_SERVICE_PROVIDER = StructLogServiceProvider()

    cloud_platform = os.environ.get('CLOUD', 'filesystem').lower()
    service_provider: LoggingServiceProvider = {
        'aws':
            service_provider_factory('mck.datatwins.storage.aws.spi',
                                     'AwsLoggingerviceProvider'),
        'azure':
            service_provider_factory('mck.datatwins.storage.azure.spi',
                                     'AzureLoggingServiceProvider'),
        'gcp':
            service_provider_factory('mck.datatwins.storage.gcp.spi',
                                     'GcpLoggingServiceProvider'),
        'local':
            lambda: DEFAULT_SERVICE_PROVIDER
    }.get(cloud_platform, 'local')()

    LOG.info("find_service_provider", scope='exiting')
    return service_provider


class LoggingService(object):

    def __init__(self, provider: LoggingServiceProvider = None):
        LOG.info("StorageService.__init__", scope='entering')
        self._provider = provider if provider else find_service_provider()
        LOG.info("StorageService.__init__", scope='exiting')

    def info(self, message: str):
        return self._provider.info(message)
