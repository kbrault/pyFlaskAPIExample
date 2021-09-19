from flask import Flask, abort, jsonify
import json
app = Flask(__name__)

players = [
    {
        "id": 1,
        "firstname": "Lebron",
        "lastname": "James",
        "nickname": "The King"
    },
    {
        "id": 2,
        "firstname": "Earvin",
        "lastname": "Johson",
        "nickname": "Magic"
    },
    {
        "id": 3,
        "firstname": "Julius",
        "lastname": "Erving",
        "nickname": "Dr. J"
    }]

@app.route('/players/')
def getPlayers():
    try:
        return jsonify(players)
    except ValueError:
        abort(400)


@app.route('/player/<id>')
def getPlayer(id):
    try:
        idPlayer = int(id)
        result = list(filter(lambda x: x["id"] == idPlayer, players))

        if result:
            # return 200 json result
            return jsonify(result)

        # unknown id
        else:
            abort(404)

    # not an int(id)
    except ValueError:
        abort(400)
