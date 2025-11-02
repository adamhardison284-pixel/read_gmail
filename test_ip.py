import requests

# API endpoint (replace with your own)
url = "https://ip-score.com/fulljson"

# Optional query parameters
params = {
}

# Optional headers (for example, if the API needs a key or token)
headers = {
}
for x in range(4):
    try:
        # Send GET request
        response = requests.get(url, headers=headers, params=params)
    
        # Check if the request was successful
        response.raise_for_status()
    
        # Parse JSON response
        data = response.json()
    
        # Print the result
        print("✅ Success! Response data:")
        print(data.ip)
    
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
