from flask import Flask, render_template, request, jsonify

from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    messages = data.get("messages", [])

    if not messages:
        return jsonify({
            "error": "No messages provided"
        }), 400

    try:

        assistant_response = get_response(messages)

        return jsonify({
            "response": assistant_response
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)