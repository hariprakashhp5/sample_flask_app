from flask import Flask, request, jsonify
from modules import logger

app = Flask("SampleApp")
LOG = logger.get_logger(__name__)


@app.route('/', methods=['GET'])
def main():
	LOG.info("hello world")
	return jsonify({'message': 'hello world!'})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3031)
