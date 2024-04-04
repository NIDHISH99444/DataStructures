class Logger:
    _instance =None
    def __new__(cls):
        if cls._instance is None:
            print("onetime")
            cls._instance =super().__new__(cls)
        return cls._instance
    

    def log(self, level, message):
        if level == 'debug':
            self._logger.debug(message)
        elif level == 'info':
            self._logger.info(message)
        elif level == 'warning':
            self._logger.warning(message)
        elif level == 'error':
            self._logger.error(message)
        elif level == 'critical':
            self._logger.critical(message)

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.log('info', 'This is an informational message.')
    logger.log('error', 'This is an error message.')
