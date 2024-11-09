from _typeshed import Incomplete

def get_log_level():
    """Return the global LOG level."""

class CatLogEngine:
    """The log engine.

    Engine to filter the logs in the terminal according to the level of severity.

    Attributes
    ----------
    LOG_LEVEL : str
        Level of logging set in the `.env` file.

    Notes
    -----
    The logging level set in the `.env` file will print all the logs from that level to above.
    Available levels are:

        - `DEBUG`
        - `INFO`
        - `WARNING`
        - `ERROR`
        - `CRITICAL`

    Default to `INFO`.

    """
    LOG_LEVEL: Incomplete
    def __init__(self) -> None: ...
    def show_log_level(self, record):
        """Allows to show stuff in the log based on the global setting.

        Parameters
        ----------
        record : dict

        Returns
        -------
        bool

        """
    def default_log(self):
        """Set the same debug level to all the project dependencies.

        Returns
        -------
        """
    def get_caller_info(self, skip: int = 3):
        '''Get the name of a caller in the format module.class.method.

        Copied from: https://gist.github.com/techtonik/2151727

        Parameters
        ----------
        skip :  int
            Specifies how many levels of stack to skip while getting caller name.

        Returns
        -------
        package : str
            Caller package.
        module : str
            Caller module.
        klass : str
            Caller classname if one otherwise None.
        caller : str
            Caller function or method (if a class exist).
        line : int
            The line of the call.


        Notes
        -----
        skip=1 means "who calls me",
        skip=2 "who calls my caller" etc.

        An empty string is returned if skipped levels exceed stack height.
        '''
    def __call__(self, msg, level: str = 'DEBUG') -> None:
        """Alias of self.log()"""
    def debug(self, msg) -> None:
        """Logs a DEBUG message"""
    def info(self, msg) -> None:
        """Logs an INFO message"""
    def warning(self, msg) -> None:
        """Logs a WARNING message"""
    def error(self, msg) -> None:
        """Logs an ERROR message"""
    def critical(self, msg) -> None:
        """Logs a CRITICAL message"""
    def log(self, msg, level: str = 'DEBUG') -> None:
        """Log a message

        Parameters
        ----------
        msg :
            Message to be logged.
        level : str
            Logging level."""
    def welcome(self) -> None:
        """Welcome message in the terminal."""

log: CatLogEngine