

from  mck.datatwins.logging import LoggingService


def test_info(struct_log_logging_service: LoggingService):
    struct_log_logging_service.info('foo')
    print("test_info")
