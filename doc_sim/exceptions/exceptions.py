class DocSimException(Exception):
    """DenialException

    This is the top-level exception in
    the denial prediction service.
    """
    pass


class ConfigException(DocSimException):
    """ConfigException

    This exception is raised when exceptions
    happens inside configuration file reading logic.
    """
    pass


class DatabaseException(DocSimException):
    """DatabaseException

    This exception is raised when exception happens
    inside database access logic.
    """
    pass


class ModelException(DocSimException):
    """ModelException

    This exception is raised when exception happens
    inside model access logic.
        """
    pass
