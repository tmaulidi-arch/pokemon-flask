from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Pokémon Flask service is running", try_this="/pokemon/pikachu")


@app.route("/pokemon/<name>")
def pokemon(name):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}", timeout=10)
    if r.status_code != 200:
        return jsonify(error="Pokémon not found"), 404
    data = r.json()
    abilities = [a["ability"]["name"] for a in data["abilities"]]
    return jsonify(
        name=data["name"],
        abilities=abilities,
        types=[t["type"]["name"] for t in data["types"]],
        message=f"I am {data['name']} and I have {abilities[0]}.",
    )


if __name__ == "__main__":
    app.run(debug=True)
