# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Define the root route
@app.route('/')
def home():
    routes = {
        "Available Routes": [
            "/",
            "/api/v1.0/precipitation",
            "/api/v1.0/stations",
            "/api/v1.0/tobs",
            "/api/v1.0/<start>",
            "/api/v1.0/<start>/<end>"
        ]
    }
    return routes

if __name__ == '__main__':
    app.run(debug=True)

#################################################
# Define the route to return the precipitation data as JSON
@app.route('/api/v1.0/precipitation')
def get_precipitation_data():
    # Convert the precipitation data to a dictionary with date as the key and prcp as the value
    precipitation_dict = {}
    for date, prcp in precipitation_data:
        precipitation_dict[date] = prcp
    
    # Return the JSON representation of the precipitation dictionary
    return jsonify(precipitation_dict)
if __name__ == '__main__':
    app.run(debug=True)

###################################################
# Define the route to return the list of stations as JSON
@app.route('/api/v1.0/stations')
def get_stations():
    # Return the list of stations as JSON
    return jsonify(stations_data)

if __name__ == '__main__':
    app.run(debug=True)

###################################################
# Define the route to return the temperature observations for the most active station for the previous year as JSON
@app.route('/api/v1.0/tobs')
def get_tobs():
    # Query the dates and temperature observations of the most active station for the previous year
    # Assume you have the necessary logic to retrieve this data and store it in 'tobs_data'
    
    # Return the JSON list of temperature observations for the previous year
    return jsonify(tobs_data)

if __name__ == '__main__':
    app.run(debug=True)

###################################################
# Define the route to calculate TMIN, TAVG, and TMAX for a specified start date
@app.route('/api/v1.0/<start>')
def get_temperatures_start(start):
    # Perform calculations for TMIN, TAVG, and TMAX for dates greater than or equal to the start date
    # Store the results in 'temperature_data'
    
    return jsonify(temperature_data)

# Define the route to calculate TMIN, TAVG, and TMAX for a specified start and end date range
@app.route('/api/v1.0/<start>/<end>')
def get_temperatures_start_end(start, end):
    # Perform calculations for TMIN, TAVG, and TMAX for dates within the specified range
    # Store the results in 'temperature_data'
    
    return jsonify(temperature_data)

if __name__ == '__main__':
    app.run(debug=True)
