import requests

url = "https://exito.azure-api.net/hostname"

payload = "{\n\t\"Hola\":\"World\"\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "307bd294-d7c3-4325-a225-490178814d78"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)