

from  mck.datatwins.storage import StorageService


def test_read_file(file_system_storage_service: StorageService):
    file_system_storage_service.read_file('foo')
    print("read_file")
