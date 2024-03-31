import os
import base64
import requests

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openai.com/v1'

    # Function to encode the image
    def encode_image(self, image_url):        
        response = requests.get(image_url)
        if response.status_code == 200:
            encoded_string = base64.b64encode(response.content).decode('utf-8')
            return encoded_string
        else:
            # Handle any errors, such as failed request or invalid URL
            print("Failed to fetch image from URL:", image_url) 
        return None

    def process_image(self, image_url):        
        encoded_image = self.encode_image(image_url)
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
        response = requests.post(f'{self.base_url}/chat/completions', headers=headers, json=payload)
        print(response.json())
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return None