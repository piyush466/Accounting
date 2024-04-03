import logging

class LogGen:

    @staticmethod
    def logger():
        logger  = logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)
        formatter=logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

        filehandle = logging.FileHandler(r"C:\Users\ASUS\PycharmProjects\pythonProject1\Logs\logs.log")

        filehandle.setFormatter(formatter)

        logger.addHandler(filehandle)

        return logger
