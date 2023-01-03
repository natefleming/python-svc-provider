from .spi import StorageServiceProvider, FileSystemStorageProvider

from types import ModuleType
from typing import Callable

import importlib
import os
import structlog

LOG = structlog.getLogger()

# load config providers from resource
#from json import load
#from pkg_resources import resource_stream

#def load_schema():
#    return load(resource_stream("example", "data/schema.json"))


def service_provider_factory(module_name: str,
                             class_name: str) -> StorageServiceProvider:

    def create():
        LOG.info("service_provider_factory.create",
                 scope='entering',
                 module_name=module_name,
                 class_name=class_name)
        m: ModuleType = importlib.import_module(module_name)
        clazz = m.__getattr__(m, class_name)
        service_provider = clazz()
        LOG.info("service_provider_factory.create", scope='exiting')
        return service_provider

    return create



def find_service_provider() -> Callable[[], StorageServiceProvider]:
    LOG.info("find_service_provider", scope='entering')
    DEFAULT_SERVICE_PROVIDER = FileSystemStorageProvider()

    cloud_platform = os.environ.get('CLOUD', 'default').lower()
    LOG.info(f"cloud_platform: {cloud_platform}")
    service_provider: StorageServiceProvider = {
        'aws':
            service_provider_factory('mck.datatwins.storage.aws.spi',
                                     'AwsStorageServiceProvider'),
        'azure':
            service_provider_factory('mck.datatwins.storage.azure.spi',
                                     'AzureStorageServiceProvider'),
        'gcp':
            service_provider_factory('mck.datatwins.storage.gcp.spi',
                                     'GcpStorageServiceProvider'),
        'default':
            lambda: DEFAULT_SERVICE_PROVIDER
    }.get(cloud_platform, DEFAULT_SERVICE_PROVIDER)()

    LOG.info("find_service_provider", scope='exiting')
    return service_provider


class StorageService(object):

    def __init__(self, provider: StorageServiceProvider = None):
        LOG.info("StorageService.__init__", scope='entering')
        self._provider = mck.datatwins.storage.azure.spi.AwsStorageServiceProvider()
       # self._provider = provider if provider else find_service_provider()
        LOG.info("StorageService.__init__", scope='exiting')

    def read_file(self, path: str):
        return self._provider.read_file(path)
