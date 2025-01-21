#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False  # Optional, to make the JSON output more readable

# Initialize database and migrations
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return jsonify({'message': 'Flask SQLAlchemy Lab 1'}), 200

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    earthquake = Earthquake.query.get(id)
    
    if earthquake:
        return jsonify({
            'id': earthquake.id,
            'location': earthquake.location,
            'magnitude': earthquake.magnitude,
            'year': earthquake.year
        })
    else:
        return jsonify({'message': f'Earthquake {id} not found.'}), 404

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    # Query earthquakes where magnitude is greater than or equal to the provided value
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    # Prepare response data
    earthquake_data = [
        {
            'id': eq.id,
            'location': eq.location,
            'magnitude': eq.magnitude,
            'year': eq.year
        } for eq in earthquakes
    ]
    
    # Return the count of earthquakes and the list of earthquake data with key 'quakes'
    return jsonify({
        'count': len(earthquake_data),
        'quakes': earthquake_data  # Changed to 'quakes' as expected by tests
    })

if __name__ == '__main__':
    app.run(port=5555, debug=True)
