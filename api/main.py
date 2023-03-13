from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import json
import random
import requests

app = Flask(__name__)
CORS(app)

app.config.from_object(__name__)
CORS(app, resources={
     r"/collaborators/*": {"origins": "http://localhost:8080"}})


collaborator_list = []


@app.route('/collaborators', methods=['GET'])
def get_collaborators():
    global collaborator_list
    collaborator_list = []

    occupations_list = ["Marketing", "Dev", "Design", "Gestão"]

    response = requests.get('https://randomuser.me/api/?results=20')
    data = response.json()
    for result in data['results']:
        collaborator = {
            'image': result['picture']['large'],
            'name': f"{result['name']['first']} {result['name']['last']}",
            'occupation': occupations_list[random.randint(0, 3)],
            'work_quality': round(random.uniform(3, 5), 1),
            'effort': round(random.uniform(3, 5), 1),
            'ponctuality': round(random.uniform(3, 5), 1),
            'creativity': round(random.uniform(3, 5), 1),
            'goals_delivery': round(random.uniform(3, 5), 1),
        }

        collaborator_list.append(collaborator)

    return jsonify(collaborator_list)

if __name__ == "__main__":
    app.run(debug=True)
