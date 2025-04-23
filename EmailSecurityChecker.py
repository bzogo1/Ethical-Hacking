import requests

email = input("Enter your email: ")
response = requests.get(f"https://haveibeenpwned.com/api/v2/breachedaccount/{email}")

if response.status_code == 200:
    print("Your email has been found in a breach! Change your passwords.")
else:
    print("Your email is safe (so far).")
