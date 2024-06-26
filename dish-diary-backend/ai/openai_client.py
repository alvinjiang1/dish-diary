import os
import base64
import requests

class OpenAIClient:
    """
    Client for interacting with the OpenAI API for image processing.

    Attributes:
        api_key (str): The API key used for authentication.
        base_url (str): The base URL of the OpenAI API.
    """
    def __init__(self, api_key):
        """
        Initializes the OpenAIClient with the provided API key.

        Args:
            api_key (str): The API key used for authentication.
        """
        self.api_key = api_key
        self.base_url = 'https://api.openai.com/v1/chat/completions'

    def encode_image(self, image_url):
        """
        Encodes an image from the specified URL to a base64-encoded string.

        Args:
            image_url (str): The URL of the image to encode.

        Returns:
            str: The base64-encoded string representing the image.
        """
        response = requests.get(image_url)
        if response.status_code == 200:
            encoded_string = base64.b64encode(response.content).decode('utf-8')
            return encoded_string
        else:
            # Handle any errors, such as failed request or invalid URL
            print("Failed to fetch image from URL:", image_url) 
            return None

    def process_image(self, image_url):
        """
        Processes an image from the specified URL using the OpenAI API.

        Args:
            image_url (str): The URL of the image to process.

        Returns:
            str: The description of the image content.
        """
        encoded_image = self.encode_image(image_url)
        if encoded_image is None:
            return None
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            "model": "gpt-4-vision-preview",                        
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What’s in this image?"},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
                    ],
                }
            ],
            "max_tokens": 300
        }        
        response = requests.post(self.base_url, headers=headers, json=payload)
        # Visualise the response (Remove for production)
        print(response.json())
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return None
