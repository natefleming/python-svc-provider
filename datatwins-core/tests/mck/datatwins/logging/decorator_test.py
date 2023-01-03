

from  mck.datatwins.logging import LoggingService, log, entering, exiting


def test_info(struct_log_logging_service: LoggingService):
  
    @log(struct_log_logging_service, entering, exiting)
    def foo():
        print("foo")

    foo()

