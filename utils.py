# 3. Helper Function
import re


def calculate_word_lengths(text: str):
    # Split text into words, considering non-alphabetic chars as delimiters
    words = re.findall(r'\b\w+\b', text)

    # Calculate the length of each word
    word_lengths = {word: len(word) for word in words}

    return word_lengths

import requests

if __name__ == "__main__":
    # Step 1: Get the authentication token
    data = {'username': 'abin', 'password': 'secret'}
    token_response = requests.post("http://127.0.0.1:8000/token", data=data)

    # Check if token request was successful
    if token_response.status_code == 200:
        token = token_response.json()['access_token']
        print("Token received:", token)
    else:
        print("Failed to get token:", token_response.status_code)

    # Step 2: Upload a PDF using the token
    file_path = r"C:\Stored Files\Abin\Machine Learning\Projects\Pycharm\pdf-file-api\test\test_file_01.pdf"  # Ensure this file exists on your system

    headers = {
        "Authorization": f"Bearer {token}",
        "content_type": "application/pdf"
    }
    with open(file_path, "rb") as file:
        files = {"file": (file_path, file, "application/pdf")}
        upload_response = requests.post("http://127.0.0.1:8000/upload-pdf/", headers=headers, files=files)

    # Check if the upload request was successful
    if upload_response.status_code == 200:
        print("Word lengths from PDF:", upload_response.json())
    else:
        print("Failed to upload PDF:", upload_response.status_code, upload_response.text)
