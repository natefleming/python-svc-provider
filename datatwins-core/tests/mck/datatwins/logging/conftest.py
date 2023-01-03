import sys
import os
import logging
import pytest
import pathlib

base_dir = pathlib.Path(__file__).parent.joinpath('..', '..', '..', '..').resolve()

sys.path.insert(0, str(base_dir))


from  mck.datatwins.logging import LoggingService
from  mck.datatwins.logging.spi import StructLogServiceProvider

@pytest.fixture(scope='session')
def struct_log_logging_service() -> LoggingService:
    return LoggingService()


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
