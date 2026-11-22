import json
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False

DICTIONARY_FILE = Path(__file__).resolve().parent / "dictionary.json"


def load_dictionary():
    with open(DICTIONARY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


@app.get("/translate/<word>")
def translate(word):
    dictionary = load_dictionary()
    word = word.lower()

    if word not in dictionary:
        return jsonify({"error": "Word not found"}), 404

    return jsonify({
        "English": word,
        "Finnish": dictionary[word]
    })


@app.get("/words")
def words():
    dictionary = load_dictionary()
    return jsonify(sorted(dictionary.keys()))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)