from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    # Process the location data (e.g., store it, use it, etc.)
    print(f"Received Location: Latitude={latitude}, Longitude={longitude}")

    return jsonify({"status": "success", "message": "Location received successfully"})

if __name__ == '__main__':
    app.run(debug=True)
