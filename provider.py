from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    # Simulate a database lookup
    if username == 'pat':
        return jsonify({'username': 'pat', 'fullname': 'Pat Dorsy'})
    elif username == 'ted':
        return jsonify({'username': 'ted', 'fullname': 'Ted Lawson'})
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(port=5003)
