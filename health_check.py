import requests, sys

if requests.get("https://myapp.azurewebsites.net/health").status_code != 200:
    sys.exit("Health check failed")
