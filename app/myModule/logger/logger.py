
import os
import logging

class Logger:

    def __init__(self):
        self.logger = ""
    
    def create_logger(self, name, level, format, logFile):

        if not os.path.isfile(logFile):
            f = open(logFile, 'w')
            f.close()
        
        # loggerの設定
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter(format)																				
        file_handler = logging.FileHandler(logFile)				
        file_handler.setFormatter(formatter)																				
        self.logger.addHandler(file_handler) 