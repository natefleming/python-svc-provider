from abc import ABC, abstractmethod
from mck.datatwins.storage.spi import StorageServiceProvider
import structlog

LOG = structlog.getLogger()


class AwsStorageServiceProvider(StorageServiceProvider):

    def __init__(self):
        LOG.info("AwsStorageServiceProvider.__init__", scope='entering')
        LOG.info("AwsStorageServiceProvider.__init__", scope='exiting')

    def read_file(self, path: str):
        LOG.info("AwsStorageServiceProvider.read_file", scope='entering')
        LOG.info("AwsStorageServiceProvider.read_file", scope='exiting')
