from dotenv import load_dotenv
import os
from ai.openai_client import OpenAIClient
from flask import Flask, request, jsonify, send_from_directory, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
from models import db, FoodEntry

app = Flask(__name__)
load_dotenv()

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

# Initialise Database
db.init_app(app)

# Here we allowed incoming requests from all domains. When we deploy to production,
# the `origin` parameter should be set to strictly allow requests from the 
# frontend domain.
CORS(app) 

# Initialize OpenAI client
openai_client = OpenAIClient(api_key=os.getenv("API_KEY"))

# Create all database tables (including FoodEntry) if they do not exist
with app.app_context():
    db.create_all()

 # Create the 'uploads' directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER']) 


@app.route('/upload', methods=['POST'])
def upload_file():    
    """
    Uploads a file and adds a new entry to the food diary.

    Returns:
        JSON response containing information about the uploaded file.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400    
    
    file = request.files['file']    
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Secure filename to prevent path traversal attacks      
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Save the file and generate image url
    file.save(filepath)    
    uploaded_image_url = url_for('uploaded_file', filename=filename, _external=True)
    
    # Use the OpenAIClient to process the image at `uploaded_image_url`
    image_description = openai_client.process_image(image_url=uploaded_image_url)

    # Create new FoodEntry and add it to databse
    new_entry = FoodEntry(image_url=uploaded_image_url, description=image_description)
    db.session.add(new_entry)
    db.session.commit()
    
    return jsonify({'message': 'File uploaded successfully', 
                    'imageUrl': uploaded_image_url, "description": image_description}), 200

@app.route('/uploaded/<filename>')
def uploaded_file(filename):
    """
    Retrieves an uploaded file by filename.

    Args:
        filename (str): The filename of the uploaded file.

    Returns:
        The uploaded file.
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/food-diary', methods=['GET'])
def get_food_diary():    
    """
    Retrieves food diary entries.

    Returns:
        JSON response containing food diary entries.
    """

    
    # Here we make the assumption that a user will not exceed 21 meals in a week.
    # That way, we limit the query to 21 entries, such that it will show all
    # the meals consumed in a week
    MAX_FOOD_ENTRIES = 21
    food_entries = FoodEntry.query.order_by(FoodEntry.id.desc()).limit(MAX_FOOD_ENTRIES).all()
    entries = [{'image_url': entry.image_url, 'description': entry.description} for entry in food_entries]
    response = jsonify(entries)
    return response
