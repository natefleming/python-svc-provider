from abc import ABC, abstractmethod

import structlog

LOG = structlog.getLogger()


class StorageServiceProvider(ABC):

    @abstractmethod
    def read_file(self, path: str):
        pass


class FileSystemStorageProvider(StorageServiceProvider):

    def __init__(self):
        LOG.info("FileSystemStorageProvider.__init__", scope='entering')
        LOG.info("FileSystemStorageProvider.__init__", scope='exiting')

    def read_file(self, path: str):
        LOG.info("FileSystemStorageProvider.read_file", scope='entering')
        LOG.info("FileSystemStorageProvider.read_file", scope='exiting')
