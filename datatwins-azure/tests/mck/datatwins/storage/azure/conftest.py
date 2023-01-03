from __future__ import absolute_import

import sys
import os
import logging
import pytest
import pathlib

#base_dir = pathlib.Path(__file__).parent.joinpath('..', '..', '..', '..', '..').resolve()
#core_dir = pathlib.Path(__file__).parent.joinpath('..', '..', '..', '..', '..', '..', 'datatwins-core').resolve()

#from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['CLOUD'] = 'azure'
#sys.path.insert(0, str(base_dir))
#sys.path.insert(0, str(core_dir))







from mck.datatwins.storage import StorageService
#import mck.datatwins.storage.azure.spi as spi

#from mck.datatwins.storage.azure.spi import AwsStorageServiceProvider

@pytest.fixture(scope='session')
def azure_storage_service() -> StorageService:
    return StorageService()

