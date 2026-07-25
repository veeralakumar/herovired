from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for username/password pairs
users = {}


@app.route('/')
def home():
    return "Welcome to the App"


@app.route('/health')
def health():
    return "App is running"


@app.route('/add', methods=['POST'])
def add_user():
    data = request.get_json(silent=True)
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Request must include 'username' and 'password'"}), 400

    username = data['username']
    password = data['password']
    users[username] = password
    return jsonify({"message": f"User '{username}' added successfully"}), 201


@app.route('/get/<username>', methods=['GET'])
def get_password(username):
    if username not in users:
        return jsonify({"error": f"Username '{username}' not found"}), 404
    return jsonify({"username": username, "password": users[username]}), 200


@app.route('/delete/<username>', methods=['DELETE'])
def delete_user(username):
    if username not in users:
        return jsonify({"error": f"Username '{username}' not found"}), 404
    del users[username]
    return jsonify({"message": f"User '{username}' deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
