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
    try:
        data = request.get_json(silent=True)
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Request must include 'username' and 'password'"}), 400

        username = data['username']
        password = data['password']
        users[username] = password
        return jsonify({"message": f"User '{username}' added successfully"}), 201

    except Exception as e:
        return jsonify({"error": "Failed to add user", "details": str(e)}), 500


@app.route('/get/<username>', methods=['GET'])
def get_password(username):
    try:
        if username not in users:
            return jsonify({"error": f"Username '{username}' not found"}), 404
        return jsonify({"username": username, "password": users[username]}), 200

    except Exception as e:
        return jsonify({"error": "Failed to retrieve user", "details": str(e)}), 500


@app.route('/delete/<username>', methods=['DELETE'])
def delete_user(username):
    try:
        if username not in users:
            return jsonify({"error": f"Username '{username}' not found"}), 404
        del users[username]
        return jsonify({"message": f"User '{username}' deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": "Failed to delete user", "details": str(e)}), 500


# Global fallback for anything not caught above (e.g. unexpected server errors)
@app.errorhandler(500)
def handle_500(e):
    return jsonify({"error": "Internal server error"}), 500


@app.errorhandler(404)
def handle_404(e):
    return jsonify({
        "error": f"The URL '{request.path}' does not exist on this server",
        "hint": "Check the URL and HTTP method you used",
        "available_endpoints": {
            "GET /": "Welcome message",
            "GET /health": "Health check",
            "POST /add": "Add a user - body: {\"username\": \"...\", \"password\": \"...\"}",
            "GET /get/<username>": "Retrieve a stored password by username",
            "DELETE /delete/<username>": "Delete a stored user by username"
        }
    }), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
