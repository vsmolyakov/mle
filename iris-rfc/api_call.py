import requests
import json
import pandas as pd

url = "http://localhost:5000/predict"

data = pd.read_csv('./test-data.csv')

# Convert to JSON string
input_data = data.to_json()

# Set the content type
headers = {"Content-Type": "application/json"}

# Make the request and display the response
resp = requests.post(url, input_data, headers=headers)

print(resp.text)