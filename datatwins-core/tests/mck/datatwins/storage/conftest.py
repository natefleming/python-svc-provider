import sys
import os
import logging
import pytest
import pathlib

base_dir = pathlib.Path(__file__).parent.joinpath('..', '..', '..', '..').resolve()

#from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
sys.path.insert(0, str(base_dir))


from  mck.datatwins.storage import StorageService
from  mck.datatwins.storage.spi import FileSystemStorageProvider

@pytest.fixture(scope='session')
def file_system_storage_service() -> StorageService:
    return StorageService()


#@pytest.fixture(scope='session')
#def spark():
#    spark = SparkSession \
#        .builder \
#        .master('local') \
#        .appName('honeycomb-testing') \
#        .getOrCreate()
#    logger = logging.getLogger('py4j')
#    logger.setLevel(logging.WARN)
#    yield spark
#    spark.stop()
