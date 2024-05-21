from flask import Flask, request, jsonify
from collections import Counter
import string

app = Flask(__name__, static_url_path='', static_folder='frontend')

@app.route("/")
def indexPage():
    return app.send_static_file("index.html")

@app.route("/api/process", methods=["POST"])
def process_text():
    data = request.get_json()
    input_text = data.get("text", "")
    
    # Buchstaben zählen
    input_text = input_text.lower()
    input_text = ''.join(filter(lambda char: char in string.ascii_lowercase, input_text))
    letter_counts = Counter(input_text)
    total_letters = sum(letter_counts.values())
    
    # Buchstabenhäufigkeit berechnen
    letter_frequency = {char: count / total_letters for char, count in letter_counts.items()}
    response_text = f"Buchstabenhäufigkeit: {letter_frequency}"
    
    return jsonify({"message": response_text})

if __name__ == "__main__":
    app.run(debug=True)