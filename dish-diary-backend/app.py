from dotenv import load_dotenv
import os
from ai.openai_client import OpenAIClient
from flask import Flask, request, jsonify, send_from_directory, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
from models import db, FoodEntry

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dish_diary_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)  # Allow requests from frontend domain

# Create all database tables (including FoodEntry) if they do not exist
with app.app_context():
    db.create_all()

# Initialize OpenAI client
openai_client = OpenAIClient(api_key=os.getenv("API_KEY"))

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # Create the 'uploads' directory if it doesn't exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400    
    
    file = request.files['file']    
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Process the image right here        
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    uploaded_image_url = url_for('uploaded_file', filename=filename, _external=True)
    image_description = openai_client.process_image(image_url=uploaded_image_url)

    # Add the uploaded image to the top of the food diary list
    # Create a new FoodEntry instance and add it to the database
    new_entry = FoodEntry(image_url=uploaded_image_url, description=image_description)
    db.session.add(new_entry)
    db.session.commit()
    
    return jsonify({'message': 'File uploaded successfully', 'imageUrl': uploaded_image_url, "description": image_description}), 200

@app.route('/uploaded/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/food-diary', methods=['GET'])
def get_food_diary():    
    # Truncate the food diary list if it exceeds a certain length (optional)
    MAX_FOOD_ENTRIES = 10
    food_entries = FoodEntry.query.order_by(FoodEntry.id.desc()).limit(MAX_FOOD_ENTRIES).all()
    entries = [{'image_url': entry.image_url, 'description': entry.description} for entry in food_entries]
    response = jsonify(entries)
    return response
