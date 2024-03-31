from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data for storing food diary entries (replace with database later)
food_entries = []

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload logic here
    # For now, just print the uploaded file details
    file = request.files['file']
    print('Uploaded file:', file.filename)        
    # Handle backend logic here
    return jsonify({'message': 'File uploaded successfully'})

@app.route('/food-diary', methods=['GET'])
def get_food_diary():
    # Dummy data for now
    return jsonify(food_entries)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
