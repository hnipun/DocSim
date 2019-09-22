import logging
from logging import StreamHandler
from doc_sim.utilities import Config


class Logger(object):
    """Utility class can be used to log information

    This is a convenient for Python's logging object.
    Logger class provides common interfaces such as
    `info`, 'debug`, and etc. for logging information.
    Read `LOGGING` section of the `config.josn' for
    configuration options of the Logging class.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            cls._instance.logger = logging.getLogger()
            cls._instance.logger.setLevel(logging.INFO)

            cls._instance.logger.addHandler(cls._instance._init_streaming_handler())

        return cls._instance

    @staticmethod
    def _init_streaming_handler():
        """

        """
        streaming = StreamHandler()
        log_formatter = logging.Formatter(Config().Logging().read('FORMATTER'))
        streaming.setFormatter(log_formatter)
        return streaming

    def info(self, msg):
        """ Info method of the logging class

        Use this method for logging INFO messages.

        Arguments:
            msg: The message which is going to log.

        Returns:
            None
        """
        self._instance.logger.info(msg)

    def debug(self, message):
        """Debug method of the logging class

        Use this method for logging DEBUG messages.

        Arguments:
            msg: The message which is going to log.

        Returns:
            None
        """
        self._instance.logger.debug(message)

    def error(self, message):
        """Error method of the logging class

        Use this method for logging ERROR messages.

        Arguments:
            msg: The message which is going to log.

        Returns:
            None
        """
        self._instance.logger.error(message)

    def critical(self, message):
        """critical method of the logging class

        Use this method for logging CRITICAL messages.

        Arguments:
            msg: The message which is going to log.

        Returns:
            None
        """
        self._instance.logger.critical(message)

    def exception(self, exception):
        """ exception method of the logging class

        Use this method for logging python exceptions.

        Arguments:
            exception: The exception which is going to log.

        Returns:
            None
        """
        self._instance.logger.exception(exception)
