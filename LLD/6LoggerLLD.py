#based on chain of responsibility design pattern 

from abc import ABC, abstractmethod

# Abstract Handler
class LogHandler(ABC):
    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    @abstractmethod
    def handle_log(self, level, message):
        pass

# Concrete Handlers
class InfoLogHandler(LogHandler):
    def handle_log(self, level, message):
        if level == 'info':
            print(f"INFO: {message}")
        elif self._successor:
            self._successor.handle_log(level, message)

class WarningLogHandler(LogHandler):
    def handle_log(self, level, message):
        if level == 'warning':
            print(f"WARNING: {message}")
        elif self._successor:
            self._successor.handle_log(level, message)

class ErrorLogHandler(LogHandler):
    def handle_log(self, level, message):
        if level == 'error':
            print(f"ERROR: {message}")
        elif self._successor:
            self._successor.handle_log(level, message)

# Logger
class Logger:
    def __init__(self):
        self._handler_chain = ErrorLogHandler()
        self._handler_chain.set_successor(WarningLogHandler())
        self._handler_chain.set_successor(InfoLogHandler())
        

    def log_message(self, level, message):
        self._handler_chain.handle_log(level, message)

# Example usage
if __name__ == "__main__":
    logger = Logger()
    # logger.log_message('info', 'This is an informational message.')
    print()
    logger.log_message('warning', 'This is a warning message.')
    print()
    # logger.log_message('error', 'This is an error message.')
