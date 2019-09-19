import logging

formatter = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')


def get_logger(logger_name):
	logger = logging.getLogger(logger_name)
	logger.setLevel(logging.DEBUG)
	console = logging.StreamHandler()
	console.setLevel(logging.DEBUG)
	console.setFormatter(formatter)
	logger.addHandler(console)
	return logger
