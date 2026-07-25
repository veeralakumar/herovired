from flask import Flask, jsonify

app = Flask(__name__)

# In-memory vote storage: {candidate_name: vote_count}
votes = {}


@app.route('/')
def home():
    return "Welcome to the App"


@app.route('/health')
def health():
    return "App is running"


@app.route('/vote/<name>', methods=['GET'])
def vote(name):
    try:
        # .get(name, 0) returns 0 if this is the first time we've seen this
        # candidate - that's how a dict handles "new key" without a KeyError
        votes[name] = votes.get(name, 0) + 1
        return jsonify({"message": f"Vote recorded for '{name}'", "current_count": votes[name]}), 200
    except Exception as e:
        return jsonify({"error": "Failed to record vote", "details": str(e)}), 500


@app.route('/results', methods=['GET'])
def results():
    try:
        return jsonify(votes), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch results", "details": str(e)}), 500


@app.route('/reset', methods=['GET'])
def reset():
    try:
        votes.clear()
        return jsonify({"message": "All votes have been reset"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to reset votes", "details": str(e)}), 500


@app.errorhandler(404)
def handle_404(e):
    return jsonify({
        "error": "The requested URL does not exist on this server",
        "available_endpoints": {
            "GET /": "Welcome message",
            "GET /health": "Health check",
            "GET /vote/<name>": "Cast a vote for a candidate",
            "GET /results": "See current vote counts",
            "GET /reset": "Clear all votes (V2 feature)"
        }
    }), 404


if __name__ == '__main__':
    app.run(debug=True, port=5002)
