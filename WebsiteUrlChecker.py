import requests

url = (input("Enter website URL:")
response = requests.get(url)

if response.status_code == 200:
    print(f"✅ {url} is online!")
else:
    print(f"❌ {url} is down!")
