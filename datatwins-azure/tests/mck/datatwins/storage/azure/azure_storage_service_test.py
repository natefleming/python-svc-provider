

from  mck.datatwins.storage import StorageService


def test_read_file(azure_storage_service: StorageService):
    azure_storage_service.read_file('foo')
    print("read_file")
