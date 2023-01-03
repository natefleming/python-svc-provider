from .spi import LoggingServiceProvider, StructLogServiceProvider

from types import ModuleType
from typing import Callable

import importlib
import os
import structlog

LOG = structlog.getLogger()


def log(logger, pre, post):
    """ Wrapper """

    def decorate(func):
        """ Decorator """

        def call(*args, **kwargs):
            """ Actual wrapping """
            pre(logger, func)
            result = func(*args, **kwargs)
            post(logger, func)
            return result

        return call

    return decorate


def entering(logger, func):
    """ Pre function logging """
    logger.debug(func.__name__, scope="entering")


def exiting(logger, func):
    """ Post function logging """
    logger.debug(func.__name__, scope="exiting")


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

    cloud_platform = os.environ.get('CLOUD', 'default').lower()
    service_provider: LoggingServiceProvider = {
        'aws':
            service_provider_factory('mck.datatwins.logging.aws.spi',
                                     'AwsLoggingServiceProvider'),
        'azure':
            service_provider_factory('mck.datatwins.logging.azure.spi',
                                     'AzureLoggingServiceProvider'),
        'gcp':
            service_provider_factory('mck.datatwins.logging.gcp.spi',
                                     'GcpLoggingServiceProvider'),
        'default':
            lambda: DEFAULT_SERVICE_PROVIDER
    }.get(cloud_platform, DEFAULT_SERVICE_PROVIDER)()

    LOG.info("find_service_provider", scope='exiting')
    return service_provider


class LoggingService(object):

    def __init__(self, provider: LoggingServiceProvider = None):
        LOG.info("LoggingService.__init__", scope='entering')
        self._provider: LoggingServiceProvider = provider if provider else find_service_provider(
        )
        LOG.info("LoggingService.__init__", scope='exiting')

    def debug(self, message: str, **kwargs):
        return self._provider.info(message, **kwargs)

    def info(self, message: str, **kwargs):
        return self._provider.info(message, **kwargs)

    def warn(self, message: str, **kwargs):
        return self._provider.info(message, **kwargs)

    def error(self, message: str, **kwargs):
        return self._provider.info(message, **kwargs)
