# Imports
import requests

# VAT no.
vat = 'DK31656206'

# HTTP request
response = requests.get("https://api.vatcomply.com/vat?vat_number=" + vat)

# Print
print("API Status Code: %s", (response.status_code))
print("JSON: %s", (response.json()))
