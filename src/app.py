"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member is None:
            return jsonify({"error": "Miembro no encontrado"}), 400
        return jsonify(member), 200
    except Exception as e:
        return jsonify({"error": "Server error", "message": str(e)}), 500
    
@app.route('/members', methods=['POST'])
def add_member():
    try:
        new_member = request.json
        if not new_member or 'first_name' not in new_member or 'age' not in new_member or 'lucky_numbers' not in new_member:
            return jsonify({"error": "Datos incompletos"}), 400
        
        member = jackson_family.add_member(new_member)
        return jsonify(member), 201
    except Exception as e:
        return jsonify({"error": "Server error", "message": str(e)}), 500
    
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        if jackson_family.delete_member(member_id):
            return jsonify({"message": "Miembro eliminado"}), 200
        else:
            return jsonify({"error": "Miembro no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": "Server error", "message": str(e)}), 500
    

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    try:
        data = request.json
        member = jackson_family.get_member(member_id)
        if member is None:
            return jsonify({"error": "Miembro no encontrado"}), 404

        for key, value in data.items():
            if key != "id":
                member[key] = value

        if "last_name" not in member or not member["last_name"]:
            member["last_name"] = jackson_family.last_name

        return jsonify(member), 200
    except Exception as e:
        return jsonify({"error": "Server error", "message": str(e)}), 500

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
