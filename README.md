# Dish Diary
Dish Diary is a web application that allows users to keep track of their food intake by uploading images of their meals and receiving descriptions generated by OpenAI's language model.

Dish Diary consists of two main components: 
- Flask backend
- React frontend

Backend: The Flask backend provides endpoints for uploading images of food, generating descriptions using OpenAI's API, and fetching food diary entries.

Frontend: The React frontend allows users to interact with the application, upload images, and view their food diary entries.

## Features
Upload images of food and receive descriptions generated by OpenAI's language model.

## Setup
### Pre-requisites
Before you begin, ensure you have the following installed on your local machine:

- Python and Pip
- npm
- Git

## Installation
1. Clone this repository:

```
git clone https://github.com/alvinjiang1/dish-diary.git
```
2. Navigate to the project directory:
```
cd dish-diary
```
3. Install dependencies for both the backend and frontend:

### Install backend dependencies
```
cd dish-diary-backend
pip install -r requirements.txt
```

### Install frontend dependencies
```
cd ../dish-diary-frontend
npm install
```
## Usage
### Start the backend development server:

1. Navigate to the backend directory
```
cd dish-diary-backend
```

2. Set environment variables
```
export API_KEY=<YOUR_OPENAI_API_KEY>
export DATABASE_URL="sqlite:///dish_diary_database.db"
```

3. Run the Flask application
```
flask run
```

### Start the frontend development server:
1. Navigate to the frontend directory
```
cd ../dish-diary-frontend
```

2. Start the development server
```
npm start
```

## Deployment
Work in Progress. (Unfortunately I was unable to deploy to heroku within the allocated time)
