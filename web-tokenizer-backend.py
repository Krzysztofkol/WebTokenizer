from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import tiktoken
import logging
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/')
def serve_frontend():
    return send_file('web-tokenizer-frontend.html')

@app.route('/tokenize', methods=['POST'])
def tokenize():
    logger.debug("Received tokenize request")
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            logger.warning("No text provided in request")
            return jsonify(error="No text provided"), 400

        text = data['text']
        encoding = tiktoken.get_encoding('cl100k_base')  # Use cl100k_base for gpt-3.5-turbo
        tokens = encoding.encode(text)
        token_count = len(tokens)
        char_count = len(text)

        logger.info(f"Tokenized text. Tokens: {token_count}, Characters: {char_count}")
        return jsonify(tokens=token_count, characters=char_count)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    logger.info("Starting the Flask server on port 2137")
    app.run(host='0.0.0.0', port=2137, debug=True)