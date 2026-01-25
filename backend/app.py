from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/api/characters')
def get_characters():
    characters = [
        "Altaïr Ibn-La'Ahad",
        "Ezio Auditore da Firenze",
        "Connor Kenway (Ratonhnhaké:ton)",
        "Edward Kenway",
        "Shay Patrick Cormac",
        "Arno Dorian",
        "Evie Frye",
        "Jacob Frye",
        "Bayek of Siwa",
        "Aya of Alexandria",
        "Kassandra",
        "Alexios",
        "Eivor Varinsdottir"
    ]
    return jsonify(characters)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
