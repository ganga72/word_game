from flask import Blueprint, request, jsonify, session
from app.game import get_random_word, check_guess

bp = Blueprint("game", __name__)

@bp.route("/start", methods=["GET"])
def start():
    session["word"] = get_random_word()
    return jsonify({"message": "Game started"})

@bp.route("/guess", methods=["POST"])
def guess():
    data = request.json
    guess_word = data.get("guess")
    secret = session.get("word")

    if not secret:
        return jsonify({"error": "Game not started"}), 400

    result = check_guess(secret, guess_word)
    return jsonify({"result": result})
