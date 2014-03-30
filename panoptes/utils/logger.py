import logging


def do_logging(Class, level='debug'):
    """ 
    The class decorator. Adds the self.logger to the class. Note that 
    log level can be passwed in with decorator so different classes can
    have different levels 
    """
    do_logging.log.info("Adding logging to: {}".format(Class.__name__))
    setattr(Class, 'logger', do_logging.log)
    return Class

def set_log_level(level='debug'):
    def decorator(Class):
        do_logging.log.logger.setLevel(log_levels.get(level))
        return Class
    return decorator


log_levels = {
    'debug': logging.DEBUG,
    'error': logging.ERROR,
    'info': logging.INFO,
}


class Logger():

    """
        Sets up the logger for our program. The do_logging class decorator allows this to be
        applited to classes within a project
    """

    def __init__(self,
                 log_file='panoptes.log',
                 profile='PanoptesLogger',
                 log_level='debug',
                 log_format='%(asctime)23s %(levelname)8s: %(message)s',
                 ):

        self.logger = logging.getLogger(profile)
        self.file_name = log_file

        self.logger.setLevel(log_levels[log_level])

        self.log_format = logging.Formatter(log_format)

        # Set up file output
        self.log_fh = logging.FileHandler(self.file_name)
        self.log_fh.setLevel(log_levels[log_level])
        self.log_fh.setFormatter(self.log_format)
        self.logger.addHandler(self.log_fh)

    def debug(self, msg):
        """ Send a debug message """

        self.logger.debug(msg)

    def info(self, msg):
        """ Send an info message """

        self.logger.info(msg)

    def error(self, msg):
        """ Send an error message """

        self.logger.error(msg)

    def warning(self, msg):
        """ Send an warning message """

        self.logger.warning(msg)

    def critical(self, msg):
        """ Send an critical message """

        self.logger.critical(msg)

    def exception(self, msg):
        """ Send an exception message """

        self.logger.exception(msg)

do_logging.log = Logger()
