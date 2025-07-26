from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    command = request.args.get('command')
    if command == 'password':
        # Determine size parameter or default to 20
        size_param = request.args.get('size')
        try:
            size = int(size_param) if size_param else 20
        except (ValueError, TypeError):
            size = 20
        # Generate random alphanumeric password
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(size))
        return jsonify(password=password)
    return jsonify(message="Hello, world!")

if __name__ == '__main__':
    # Enable debug mode for development
    app.run(debug=True)
